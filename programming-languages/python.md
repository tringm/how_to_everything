# Python guide for beginner

## Tools
### Python package manger pipenv
1. Sources:
    * https://docs.python-guide.org/dev/virtualenvs/
1. Install pipenv
```
$ pip install --user pipenv
```
This does a user installation to prevent breaking any system-wide packages. If pipenv isn’t available in your shell after installation, you’ll need to add the user base’s binary directory to your PATH.
    * Finding user base binary directory
    ```
    python -m site --user-base
    ```
    E.g: ```/home/tri/.local```.
    * Add ```/bin``` to the end, and add it to PATH.
    ```
    vim ~/.bashrc
    ```
    add to .bashrc
    ```bash
    export PATH="$PATH/home/tri/.local/bin"
    ```
    ```
    source ~/.bashrc
    ```
1. Installing packages
    * Similar to pip:
    ```
    pipenv install packages
    ```
1. [Adding pipenv to Pycharm Project](https://www.jetbrains.com/help/pycharm/pipenv.html)
    * If pipenv not automatically found, point it to the executable file. E.g:```/home/tri/.local/bin/pipenv```



## Tricks:
### Misc
1. Set string as variable name:
  * Use dictionary
  * Use it in a class:
      ```python
      setattr(self, name, value)
    ```
1. Groupby list of tuples:
  * ***NOTE***: This does not work with tuple of string
  * Use ```itertools.groupby```
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
1. Remove existing logging settings:
  ```python
  for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)
  ```

### Preprocessing
1. LabelEncoder (with sklearn)

  Converting a column from string to int, and save encoder
  ```python
  from sklearn import preprocessing

  label_encoders = preprocessing.LabelEncoder().fit(my_column)

  classes = list(label_encoders.classes_)

  transformed_column = label_encoders.transform(some_column)

  reverse = label_encoders.inverse_transform(transformed_column)
  ```

### Using Pandas
1.  Load by more than 1 whitespace
  ```python
  pd.read_csv(path, names = list_of_column_names, sep='\s+')
  ```
1.  Drop columns
  ```python
  df = df.drop(columns = list('name1', 'name2'))
  df = df.drop(list(indexes), axis=)
  ```
1. Replace Nan
  ```python
  df.fillna(value_to_be_replaced, inplace=True/False)
  ```
1. Selecting columns based on type:
  * Number
      ```python
      number_columns = table.select_dtypes(include=['int64', 'float64'])
      ```
  * String
      ```python
      string_columns = table.select_dtypes(include=['object'])
      ```

1. Grouped dfs by some shared id

  Grouped by id, combined columns to list

  ```python
  grouped = df.groupby(['id'], as_index=False/True).agg(lambda x: x.tolist())
  grouped = df.groupby(['id'], as_index=False/True).sum()
  ```
1. One hot encoding for list
  ```python
  one_hot_df = pd.get_dummies(grouped['RXDDRGID'].apply(pd.Series).stack()).sum(level=0)
  ```
1.  Merged to existing df
  ```python
  grouped = pd.concat([grouped, drug_id_dummies], axis=1)
  ```
1.  Merge

  on = id to be merge
  how = {left, right, outer, inner}
  ```python
  Y.merge(X, how='right', on='SEQN')
  ```
  If doesn't want to add columns (basically filter by matching id)
  ```python
  Y.merge(X, how='right', on='SEQN').drop(columns=[column for column in list(X.columns) if column != 'SEQN'])
  ```
1.  Request object to dataframe
  * With url:
      ```python
      pd.read_csv(url)
      ```
  * With request response:
      ```python
      import requests
      import pandas as pd
      import io

      request = requests.post(url, data = 'haha')
      df = pd.read_csv(io.StringIO(request.content.decode('utf-8')))
      ```
### Speed up
1. Fast flatten list
  * Use itertools
    ```python
    list(itertools.chain(*listoflists))
    ```
