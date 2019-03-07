## Torchtext - Somewhat usefull NLP tool

### Build vocab
Torchtext offers build vocab tool. However, this can be cumbersome since torchtext requires to creates its own type dataset. Still, this is quite easy if the data is loaded directly from file.
1. Declaring the field
    * Load of these thing is still quite unclear at this point (e.g: sequential, use_vocab). The most important thing is the tokenize. The tokenize is a function, it can be a tokenizer for text data, or just a list (This is an useful tricks for loading already tokenized text, example below). A good combination could be spacy for nlp.
        ```Python
        from torchtext.data import Field
        import spacy

        tokenize1 = lambda x: x.split()

        spacy_analyzer = spacy.load('en',disable=['parser', 'tagger', 'ner'])
        def tokenize2(sentence):
          return [w.text.lower() for w in spacy_analyzer(sentence)]

        text_field = Field(sequential=True, tokenize=some_tokenize, lower=True)
        label_field = Field(sequential=False, use_vocab=False)
        ```    
        * ```sequential=True``` tell torchtext that the data is in form of sequence and not discrete.
        * ```'use_vocab=True'``` This attribute tells torchtext to create the vocabulary
        * ```'pad_token=None'``` Padding token or None
        * ```'unk_token=None'``` Out of vocab token or None
    * Next, fields will be stored to be used when creating torchtext dataset:
        ```python
        fields = [
          ('haha', None),
          ('hehe', label_field)
          ('hoho', text_field)
        ]
        ```
1. Create dataset from files:
    * Sample:
        ```python
        train, val = data.TabularDataset.splits(path='./data',
                                                format='csv',
                                                train='traindf.csv',
                                                validation='valdf.csv',
                                                fields=fields,
                                                skip_header=True)
        ```
    * Parameters:
        * ```path='./data'```: Path to folder. Torchtext can even load from folder
        * ```format='csv'```
        * ```train='traindf.csv'``` Name of train file. The final path will become ./data/traindf.csv. Similarly, ```validation=```
        * ```fields=train_val_fields``` Tell torchtext how the coming data will be processed
        * ```skip_header=True```
1. Build vocab:
    ```Python
    text_field.build_vocab(train, val)
    ```
    * Useful methods:
        * String to index ```text_field.vocab.stoi['some_string']```
        * Index to string ```text_field.vocab.itos[147]```
1. ***TRICKS***:
    * Build vocab from a list of tokenized sentence (list of tokens):
        ```python
        def build_vocab_from_sentences_tokens(sentences_tokens):
            token_field = data.Field(tokenize=list, init_token='<root>')
            fields = [('tokens', token_field)]
            examples = [data.Example.fromlist([t], fields) for t in sentences_tokens]
            torch_dataset = data.Dataset(examples, fields)
            token_field.build_vocab(torch_dataset)
            return token_field.vocab
        ```
        * Use list as tokenize
        * Create dataset from example
