# Python guide for beginner

## Tools

### Python package manger pipenv

1.  Sources:
    -   <https://docs.python-guide.org/dev/virtualenvs/>
2.  Install pipenv
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
        source ~/.bashrc
        ```

1.  Installing packages
    -   Similar to pip:
        ```
        pipenv install packages
        ```
2.  [Adding pipenv to Pycharm Project](https://www.jetbrains.com/help/pycharm/pipenv.html)
    -   If pipenv not automatically found, point it to the executable file. E.g:`/home/tri/.local/bin/pipenv`

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

### Speed up

1.  Fast flatten list

    -   Use itertools
        ```python
        list(itertools.chain(*listoflists))
        ```

### Requests

1.  Running async requests:

    -   Use asyncio

        ```Python
        def async_request(self, request_methods: [str], paths: [str], data: [], use_rw_key=False):
            async def fetch(session, req_method, url, query):
                async with session.request(method=req_method, url=url, json=query, headers=headers) as response:
                    res_json = await response.json()
                    return res_json

            async def run():
                async with ClientSession() as session:
                    tasks = [fetch(session, request_methods[i], urls[i], queries[i])
                             for i in range(len(request_methods))]
                    responses = await asyncio.gather(*tasks)
                    return responses

            headers = {'Content-Type': 'application/json'}
            loop = asyncio.get_event_loop()
            responses = loop.run_until_complete(run())
            return responses
        ```

    -   It's also possible to group multiple tasks together:
        ```python
        async def run():
            async with ClientSession() as session:
                task1 = asyncio.gather(*[fetch(session, request_methods[i], full_paths[i], data[i])
                         for i in range(len(request_methods))])
                task2 = ...
                task3 = ...
                tasks = [task1, task2, task3]
                responses = await asyncio.gather(*tasks)
                return responses
        ```

## Testing

### Unittest
1.  To create timer for test method, use set up and tear down for a new TestCase:
    ```python
    class TestCaseTimer(unittest.TestCase):
        def setUp(self) -> None:
            self._started_at = time.time()

        def tearDown(self) -> None:
            self._elapsed = time.time() - self._started_at
    ```

1. To implement a testcase that compare file:
    ```Python
    class TestCaseCompare(TestCaseTimer):
        def file_compare(self, out_f: Path, exp_f: Path, msg=None):
            if not out_f.exists() or not exp_f.exists():
                raise ValueError("Either %s or %s does not exist" % (str(out_f), str(exp_f)))
            if not out_f.is_file() or not exp_f.is_file():
                raise ValueError("Either %s or %s is not a file" % (str(out_f), str(exp_f)))
            if not msg:
                self.assertTrue(filecmp.cmp(str(out_f), str(exp_f), shallow=False),
                                f"out file {str(out_f)} does not match exp file {str(exp_f)}")
            else:
                self.assertTrue(filecmp.cmp(str(out_f), str(exp_f), shallow=False), msg)
    ```
    Combine with ```@setUpClass``` to initialize in and out folder:
    ```Python
    class TestCaseCompare(TestCaseTimer):
        def setUpClass(cls):
            cls.input_folder = root_path() / 'test' / 'io' / 'in'
            cls.output_folder = root_path() / 'test' / 'io' / 'out'
            cls.out_file = {}
            cls.exp_file = {}
            cls.in_file = {}
    ```
1. To compare test result, e.g: exp file and out file, with meld, implement a TextTestResult class:
    ```Python
    class TestResultCompareFileMeld(unittest.TextTestResult):
        def addFailure(self, test, err):
            super().addFailure(test, err)
            if hasattr(test, 'out_file') and hasattr(test, 'exp_file'):
                method_id = test.id().split('.')[-1]
                if method_id in test.out_file and method_id in test.exp_file:
                    cont = True
                    while cont:
                        res = input("[d]iff, [c]ontinue or [f]reeze? ")
                        if res == "f":
                            os.rename(test.out_file[method_id], test.exp_file[method_id])
                            cont = False
                        elif res == "c":
                            cont = False
                        elif res == "d":
                            os.system("meld " + str(test.exp_file[method_id]) + " " + str(test.out_file[method_id]))

        def addError(self, test, err):
            super(TestResultCompareFileMeld, self).addError(test, err)
    ```
    Then use TestRunner with this TestResult class:
    ```python
    runner = unittest.TextTestRunner(verbosity=2, resultclass=TestResultCompareFileMeld)
    ```

1. Log test metrics to stream of TestResult:
    ```Python
    class TestResultLogMetrics(unittest.TextTestResult):
        def addSuccess(self, test):
            super().addSuccess(test)
            with (root_path() / 'test' / 'io' / 'out' / 'metrics.log').open(mode='a+') as f:
                f.write(f"{test.id()}, success, {test._elapsed:5f}\n")
                #or
                self.stream.write('...')
        def addFailure(self, test, err):
            super().addFailure(test, err)
            with (root_path() / 'test' / 'io' / 'out' / 'metrics.log').open(mode='a+') as f:
                f.write(f"{test.id()}, fail, {test._elapsed:5f}\n")
    ```

### Coverage

1.  Combine coverage with unittest to see how weel the tests covers:
    ```Python
      coverage run test.py all
      coverage report
    ```
1.  To ignore coverage on library packages, add a `.coveragerc` file that contains:
        [run]
        omit =
          */site-packages/*
