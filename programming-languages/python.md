# Python guide for beginner

## Tricks:
### Set string as variable name:
1. Use dictionary
1. Use it in a class:
    ```python
    setattr(self, name, value)
    ```

### Set up new logging level
```python
logging.VERBOSE = 5
logging.addLevelName(logging.VERBOSE, "VERBOSE")
logging.Logger.verbose = lambda inst, msg, *args, **kwargs: inst.log(logging.VERBOSE, msg, *args, **kwargs)
logging.LoggerAdapter.verbose = lambda inst, msg, *args, **kwargs: inst.log(logging.VERBOSE, msg, *args, **kwargs)
logging.verbose = lambda msg, *args, **kwargs: logging.log logging.VERBOSE, msg, *args, **kwargs)
```
## Preprocessing
### LabelEncoder (with sklearn)
Converting a column from string to int, and save encoder
```python
from sklearn import preprocessing

label_encoders = preprocessing.LabelEncoder().fit(my_column)

classes = list(label_encoders.classes_)

transformed_column = label_encoders.transform(some_column)

reverse = label_encoders.inverse_transform(transformed_column)
```
## Using Pandas
### Load by more than 1 whitespace
```python
pd.read_csv(path, names = list_of_column_names, sep='\s+')
```
### Drop columns
```python
df = df.drop(columns = list('name1', 'name2'))
df = df.drop(list(indexes), axis=)
```
### Replace Nan
```python
df.fillna(value_to_be_replaced, inplace=True/False)
```
### Selecting columns based on type:
1. Number
    ```python
    number_columns = table.select_dtypes(include=['int64', 'float64'])
    ```
1. String
    ```python
    string_columns = table.select_dtypes(include=['object'])
    ```

### Grouped dfs by some shared id
Grouped by id, combined columns to list

```python
grouped = df.groupby(['id'], as_index=False/True).agg(lambda x: x.tolist())
grouped = df.groupby(['id'], as_index=False/True).sum()
```
### One hot encoding for list
```python
one_hot_df = pd.get_dummies(grouped['RXDDRGID'].apply(pd.Series).stack()).sum(level=0)
```
### Merged to existing df
```python
grouped = pd.concat([grouped, drug_id_dummies], axis=1)
```
### Merge
on = id to be merge
how = {left, right, outer, inner}
```python
Y.merge(X, how='right', on='SEQN')
```
If doesn't want to add columns (basically filter by matching id)
```python
Y.merge(X, how='right', on='SEQN').drop(columns=[column for column in list(X.columns) if column != 'SEQN'])
```
### Request object to dataframe
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
