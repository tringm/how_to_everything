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

### Pandas
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

1. Vectorization operation on a slice of df:
  * Use index
    ```Python
    use_usd = (sales_table['CUR_CODE'] == 'USD')
    sales_table.loc[use_usd, 'ITEM_VAL_SALE'] = sales_table['ITEM_VAL_SALE'] * usd_to_eur_rate
    ```

1. Map value of a column:
  * Map ```%Key_Store``` of sales_table to ```Country (GA)``` of store table
    ```python
    store_to_region = dict(zip(store_table['%Key_Store'], store_table['Country (GA)']))
    sale_store_country = sales_table['%Key_Store'].map(store_to_region)
    ```

1. Concatenate string columns:
  * Use col.str:
    ```Python
    article_number = sales_table['%Key_Item']
    sales_table['ITEM_RU'] = article_number.str.cat(sale_store_country, sep='_')
    ```

1. Replace string column with some value + Convert string column to numeric
  * Use col.str
    ```python
    article_retail_unit['Price Euro (incl. VAT)'].str.replace(',', '.').astype(float)
    ```

### Speed up
1. Fast flatten list
  * Use itertools
    ```python
    list(itertools.chain(*listoflists))
    ```


### Requests
1. Running async requests:
  * Use asyncio
    ```Python
    class AitoClient:
      def __init__(self, url, rw_key, ro_key):
          self.url = url
          self.rw_key = rw_key
          self.ro_key = ro_key
          self.logger = logging.getLogger("AitoClient")

      def async_request(self, request_methods: [str], paths: [str], data: [], use_rw_key=False):
          async def fetch(session, req_method, url, d):
              if isinstance(d, str):
                  d = json.loads(d)
              logger.info(f"{req_method} to url {url} with data: {d}")
              async with session.request(method=req_method, url=url, json=d, headers=headers) as response:
                  res_json = await response.json()
                  logger.info(f"Got response: {res_json}")
                  return res_json

          async def run():
              async with ClientSession() as session:
                  tasks = [fetch(session, request_methods[i], full_paths[i], data[i])
                           for i in range(len(request_methods))]
                  logger.info(f"task {tasks}")
                  responses = await asyncio.gather(*tasks)
                  return responses

          logger = self.logger

          headers = {'Content-Type': 'application/json'}
          if use_rw_key and self.rw_key:
              headers['x-api-key'] = self.rw_key
          if not use_rw_key and self.ro_key:
              headers['x-api-key'] = self.ro_key

          full_paths = [self.url + p for p in paths]
          loop = asyncio.get_event_loop()
          responses = loop.run_until_complete(run())
          return responses
    ```
