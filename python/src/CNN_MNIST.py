import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

import torchvision
import torchvision.datasets as datasets

import matplotlib.pyplot as plt
import matplotlib.cm as cm

from random import shuffle

from plotting import *

torch.set_num_threads(20)

N_EPOCHS = 20
BATCH_SIZE=50
IMG_WIDTH = 28
N_CLASSES = 10
TEST_EVERY = 1
STATUS_EVERY = 1
LR = 0.001

# --- MNIST initialization ---
# torchvision.datasets.MNIST outputs a set of PIL images
# We transform them to tensors
transform2tensor = torchvision.transforms.ToTensor()

mnist_trainset = datasets.MNIST(root='../data', train=True, download=True, transform=transform2tensor)
mnist_testset  = datasets.MNIST(root='../data', train=False, download=True, transform=transform2tensor)

print('Train set size: %d' % (len(mnist_trainset)))
print('Test set size: %d' % (len(mnist_testset)))

# Create Pytorch data loaders
train_loader = torch.utils.data.DataLoader(mnist_trainset, batch_size=BATCH_SIZE, shuffle=True)
test_loader = torch.utils.data.DataLoader(mnist_testset, batch_size=BATCH_SIZE, shuffle=False)

#--- model ---
class ConvNet(nn.Module):
    def __init__(self,
                 img_width,
                 n_classes):
        super(ConvNet, self).__init__()
        self.conv1 = nn.Sequential(
            nn.Conv2d(
                in_channels=1,
                out_channels=16,
                kernel_size=5,
                stride=1,
                padding=2
            ),                              # output shape (16, 28, 28)
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2)     # choose max value in 2x2 area => output shape (16, 14, 14)
        )
        self.conv2 = nn.Sequential(
            nn.Conv2d(
                in_channels=16,
                out_channels=32,
                kernel_size=5,
                stride=1,
                padding=2
            ),                              # output shape (32, 14, 14)
            nn.ReLU(),
            nn.MaxPool2d(2)                 # output shape (32, 7, 7)
            )
        self.fc1 = nn.Linear(32 * 7 * 7, img_width*img_width)
        self.fc2 = nn.Linear(img_width*img_width, n_classes)

    def forward(self, x):
        out = self.conv1(x)
        out = self.conv2(out)
        out = out.view(out.size(0), -1)
        out = F.relu(self.fc1(out))
        out = F.dropout(out, 0.5, training=self.training)
        out = F.relu(self.fc2(out))
        return F.log_softmax(out, dim=1)

# --- evaluation function ---
def evaluate(dataset_loader,model):
    correct = 0
    total = 0

    model.eval()
    for i, (eval_images, eval_labels) in enumerate(dataset_loader):
        eval_images = eval_images.view(BATCH_SIZE, IMG_WIDTH*IMG_WIDTH)
        log_probs = model(eval_images)
        _, predicted = torch.max(log_probs, dim=1)
        total += eval_labels.size(0)
        correct += torch.eq(predicted,eval_labels).sum().item()

    return 100.0 * correct / total

model = ConvNet(IMG_WIDTH, N_CLASSES)
print(model)
optimizer = optimizer = torch.optim.Adam(model.parameters(), lr=0.0001)
loss_function = nn.NLLLoss()


for epoch in range(N_EPOCHS):
    model.train()
    total_loss = 0
    for i, (images, labels) in enumerate(train_loader):
        optimizer.zero_grad()
        output = model(images)
        loss = loss_function(output, labels)
        total_loss += loss
        loss.backward()
        optimizer.step()

    if ((epoch+1) % TEST_EVERY) == 0:
        train_acc = evaluate(train_loader,model)
        test_acc = evaluate(test_loader,model)

        print('epoch: %d, loss: %.2f, train acc: %.2f%%, test acc: %.2f%%' %
              (epoch+1, total_loss, train_acc, test_acc))

    elif ((epoch+1) % STATUS_EVERY) == 0:
        print('epoch: %d, loss: %.2f' % (epoch+1, total_loss))
