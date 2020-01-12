## Techniques

1. Handling mini batch (for NLP):

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

## Troubleshotting

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
