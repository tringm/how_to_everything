# Deeper deeper deeper

## CNN
1. Good for: Image processing
    * FFNN have no parameter sharing across the saptial dimension (similar dot, upper corner dot vs lower corner dot => different)
    * CNN uses filter => small section of image at a time
    * Image K , filter I => I * K
    * General architecture:
    ![image](./img/cnn.png)
1. Techniques:
    * Padding: Add zeros at the boundary
    * Stride: The rate at which kernal passes over the input
        * Greater stride -> faster (less dot product) but lower resolution
    * Pooling layer: Downsampling, can improve the result by increasing spatial tolerance
        * Max Pooling: Good when data is sparse (e.g: After ReLU)
        * Average Pooling: Work worse

## RNN
1. Sources:
    * https://towardsdatascience.com/recurrent-neural-networks-and-lstm-4b601dd822a5
1. Good for: sequential data (Time series, NLP) and predict what coming next
    * A RNN has short-term memory (can be combine with long term memory -> LSTM) to takes into consideration of prev. input
    * Backpropagation through time: Doing back backpropagation through an unrolled RNN. Unrolled RNN is RNN as a sequence of NN (sync the information cycles through a loop, not only feed forward)
    * Gradients:
        * Exploding gradient: Too high importance of a weight => truncate or squash the gradient
        * Vanishing gradient: Gradients are too small and the model stop learning => LSTM
    * Long-Short term memory(LSTM):
        * LSTM remember information based on its importance. It can read, write, and delete information. The assignment of importance of information happens through weight, learned by the algo.
        * Kinda like a gated architecture
            ```
            h[t] = a(h[t-1],x[t]) * h[t-1] + b(h[t-1],x[t]) * i(x[t])
            ```
            a determines how much of the old state we want to retain and b determins how much of the current state we want to remember

## Handling mini batch (for NLP)

Doing mini-batch with words as input can be problematic, synce words can be different in length. A trick is to use padding, to make sure that all words in the same batch is in similar length. Also, adjust the batch so that the first dimension is the maximum length of batch, instead of batch size.  
For instance, if ```BATCH_SIZE = 5```, and the word lengths are [5, 3, 6, 7, 4]. Then padding so that we have a tensor of shape ```(7, 5)```.
This is useful because if we use embedding, for instance,
```python
self.embedding_dim = 30
self.embedding_layer = nn.Embedding(self.character_set_size, self.embedding_dim)
```
then the output of the embedding layer would be of shape ```(7, 5, 30)```. Hence the input of the next layer can be
```python
self.lstm = nn.LSTM(self.embedding_dim, self.hidden_dim)
```
