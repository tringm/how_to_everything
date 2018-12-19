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

Number

```python
number_columns = table.select_dtypes(include=['int64', 'float64'])
```

String

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
