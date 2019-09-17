## Discounted cumulative gain

Measure the usefulness (gain) of a document based on its position in the result list. Gain is accumulated from the top of the result list to the bottom, the gain is discounted at lower ranks.

**Note**:
- Requires relevancy metric in the test dataset (e.g: Cranfield)
- Assumption:
  - Highly relevant documents are more useful when when have higher ranks
  - Highly relevant documents are more useful than marginally relevant documents
