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

1.  Replace Nan

    ```python
    df.fillna(value_to_be_replaced, inplace=True/False)
    ```

1.  Selecting columns based on type:
    -   Number
        ```python
        number_columns = table.select_dtypes(include=['int64', 'float64'])
        ```
    -   String
        ```python
        string_columns = table.select_dtypes(include=['object'])
        ```

1.  Grouped dfs by some shared id

    Grouped by id, combined columns to list

    ```python
    grouped = df.groupby(['id'], as_index=False/True).agg(lambda x: x.tolist())
    grouped = df.groupby(['id'], as_index=False/True).sum()
    ```

1.  One hot encoding for list

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

    -   With url:
        ```python
        pd.read_csv(url)
        ```
    -   With request response:

        ```python
        import requests
        import pandas as pd
        import io

        request = requests.post(url, data = 'haha')
        df = pd.read_csv(io.StringIO(request.content.decode('utf-8')))
        ```

1.  Vectorization operation on a slice of df:

    -   Use index
        ```Python
        use_usd = (sales_table['CUR_CODE'] == 'USD')
        sales_table.loc[use_usd, 'ITEM_VAL_SALE'] = sales_table['ITEM_VAL_SALE'] * usd_to_eur_rate
        ```

1.  Map value of a column:

    -   Map `%Key_Store` of sales_table to `Country (GA)` of store table
        ```python
        store_to_region = dict(zip(store_table['%Key_Store'], store_table['Country (GA)']))
        sale_store_country = sales_table['%Key_Store'].map(store_to_region)
        ```

1.  Concatenate string columns:

    -   Use col.str:
        ```Python
        article_number = sales_table['%Key_Item']
        sales_table['ITEM_RU'] = article_number.str.cat(sale_store_country, sep='_')
        ```

1.  Replace string column with some value + Convert string column to numeric

    -   Use col.str
        ```python
        article_retail_unit['Price Euro (incl. VAT)'].str.replace(',', '.').astype(float)
        ```
