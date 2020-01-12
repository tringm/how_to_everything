## Recurrent Neural Network (RNN)
### Sources:
  * https://towardsdatascience.com/recurrent-neural-networks-and-lstm-4b601dd822a5
  * https://towardsdatascience.com/illustrated-guide-to-recurrent-neural-networks-79e5eb8049c9

### Intro:
  * Effective with ***sequential data*** (Time series, NLP) and predict what coming next
  * A RNN has short-term memory (can be combine with long term memory -> LSTM) to takes into consideration of prev. input
  * Backpropagation through time: Doing back backpropagation through an unrolled RNN. Unrolled RNN is RNN as a sequence of NN (sync the information cycles through a loop, not only feed forward)

### Limitation: Vanishing gradient -> Short term memory:
  * Gradients shrinks as the model back propagates down through each time step, hence the earlier layers are barely updated and the model doesn't learn from the long range dependency.
  * *Exploding gradient*: Too high importance of a weight => truncate or squash the gradient

### Variation: Long-Short term memory(LSTM)
LSTM remembers information based on its importance. It can read, write, and delete information. The assignment of importance of information happens through weight, learned by the algo.
* Gated architecture
  ```
  h[t] = a(h[t-1],x[t]) * h[t-1] + b(h[t-1],x[t]) * i(x[t])
  ```
  a determines how much of the old state we want to retain and b determines how much of the current state we want to remember

* Example:
  * Translation machine, [Text summarization](https://www.analyticsvidhya.com/blog/2019/06/comprehensive-guide-text-summarization-using-deep-learning-python/): A LSTM encoder => internal state (h, c) => A LSTM decoder

* Limitation:
  * Only works for short sequence: The encoder encodes the entire sequence into a fixed length vector then the decoder looks at the entire sequence for the prediction => solution = [Attention Mechanism]

* ***Attention Mechanism***:
  * Sources:
    * https://lilianweng.github.io/lil-log/2018/06/24/attention-attention.html
