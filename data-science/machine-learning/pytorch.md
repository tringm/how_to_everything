## CNN with Pytorch
1. Sources:
    * https://medium.freecodecamp.org/an-intuitive-guide-to-convolutional-neural-networks-260c2de0a050
1. Parameters for cnn layer:
    * Kernel Size: the size of the filter.
    * Kernel Type: the values of the actual filter. Some examples include identity, edge detection, and sharpen.
    * Stride: the rate at which the kernel passes over the input image. A stride of 2 moves the kernel in 2-pixel increments.
    * Padding: we can add layers of 0s to the outside of the image in order to make sure that the kernel properly passes over the edges of the image.
    * Output Layers: how many different kernels are applied to the image.
1. Good sources:
    * [CNN (pytorch)](https://blog.algorithmia.com/convolutional-neural-nets-in-pytorch/)
    * Other functions:
        * ReLu: defacto activation function at the time Max(0, input)
        * Max Pooling: highest value of the pool
            * E.g: 4*4 matrix with maxpooling2d(2*2) becomes 2*2
1. An [attempt](https://www.kaggle.com/sdelecourt/cnn-with-pytorch-for-mnist) with ~95% accuracy
1. [My implementation](./src/CNN_MNIST.py) ~97% accuracy


## RNN



## Errors

1. RuntimeError: Trying to backward through the graph a second time, but the buffers have already been freed. Specify retain_graph=True when calling backward the first time
    * This error can be caused by initializing a hidden state in RNN

    ```python
        self.hidden = self.init_hidden()

    def init_hidden(self):
        return (Variable(torch.zeros(self.n_layers, BATCH_SIZE, self.hidden_dim)),
                Variable(torch.zeros(self.n_layers, BATCH_SIZE, self.hidden_dim)))
    ```

    and calling hidden in ```forward()```:

    ```python
    lstm_out, self.hidden = self.lstm(embeds, self.hidden)
    ```

    * Fix: Adding ```retain_graph=True``` to ```loss.backwarrd()```
    ```python
    loss.backward(retain_graph=True)
    ```
    * ***NOTE***:
        * Initialize hidden state makes the model learn a good initial state as well, so it needs to back-propagate all the way to the hidden layer. This is for giving "cue" to the model to go to a certain direction under certain circumstances. This advanced method can make the model much slow
        * Instead, just call ```self.lstm(embeds)```, without mentioning ```self.hidden```
