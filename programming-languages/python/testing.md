## Testing

### Unittest
1. [Generic test setup](samples/test_setup.py):
    - ***NOTE***:
        - The test set up use 2 global variables DEFAULT_INPUT_FOLDER, DEFAULT_OUTPUT_FOLDER from a config file which is initialized during execution of test runner
1. [Generic test runner](samples/test_runner.py)

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
                raise ValueError(f"Either {out_f} or {exp_f} does not exist")
            if not out_f.is_file() or not exp_f.is_file():
                raise ValueError(f"Either {out_f} or {exp_f} is not a file" % (str(out_f), str(exp_f)))
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
1. Interactive test compare with meld:
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
