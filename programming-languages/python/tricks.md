## Tricks:
### Misc

1.  Set string as variable name:
    -   Use dictionary
    -   Use it in a class:
        ```python
        setattr(self, name, value)
        ```

1.  Groupby list of tuples:

    -   **_NOTE_**: This does not work with tuple of string
    -   Use `itertools.groupby`

        ```Python
        from itertools import groupby
        from operator import itemgetter
        a = [(1, 2), (1, 3), (2, 4), (2, 5)]

        [(k, list(zip(*g))) for k, g in groupby(a, operator.itemgetter(0))]
        # => [(1, [(1, 1), (2, 3)]), (2, [(2, 2), (4, 5)])]

        [(k, list(list(zip(*g))[1])) for k, g in groupby(a, operator.itemgetter(0))]
        # => [(1, [2, 3]), (2, [4, 5])]
        ```

### Logging

1.  Set up new logging level

    ```python
    logging.VERBOSE = 5
    logging.addLevelName(logging.VERBOSE, "VERBOSE")
    logging.Logger.verbose = lambda inst, msg, *args, **kwargs: inst.log(logging.VERBOSE, msg, *args, **kwargs)
    logging.LoggerAdapter.verbose = lambda inst, msg, *args, **kwargs: inst.log(logging.VERBOSE, msg, *args, **kwargs)
    logging.verbose = lambda msg, *args, **kwargs: logging.log logging.VERBOSE, msg, *args, **kwargs)
    ```

1.  Remove existing logging settings:

    ```python
    for handler in logging.root.handlers[:]:
      logging.root.removeHandler(handler)
    ```

### Preprocessing

1.  LabelEncoder (with sklearn)

    Converting a column from string to int, and save encoder

    ```python
    from sklearn import preprocessing

    label_encoders = preprocessing.LabelEncoder().fit(my_column)

    classes = list(label_encoders.classes_)

    transformed_column = label_encoders.transform(some_column)

    reverse = label_encoders.inverse_transform(transformed_column)
    ```

### Speed up

1.  Fast flatten list

    -   Use itertools
        ```python
        list(itertools.chain(*listoflists))
        ```
