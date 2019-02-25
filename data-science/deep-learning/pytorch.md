## CNN network for MNIST
1. Good sources:
    * [Overview](https://blog.algorithmia.com/convolutional-neural-nets-in-pytorch/)
    * Essentially, convolution = applying filter to the image that has been feature engineered (into matrix) with:
        * Kernel Size: the size of the filter.
        * Kernel Type: the values of the actual filter. Some examples include identity, edge detection, and sharpen.
        * Stride: the rate at which the kernel passes over the input image. A stride of 2 moves the kernel in 2-pixel increments.
        * Padding: we can add layers of 0s to the outside of the image in order to make sure that the kernel properly passes over the edges of the image.
        * Output Layers: how many different kernels are applied to the image.
    * Other functions:
        * ReLu: defacto activation function at the time Max(0, input)
        * Max Pooling: highest value of the pool
            * E.g: 4*4 matrix with maxpooling2d(2*2) becomes 2*2
1. An [attempt](https://www.kaggle.com/sdelecourt/cnn-with-pytorch-for-mnist) with ~95% accuracy
1. [My implementation](./src/CNN_MNIST.py)
