Specifying What Tests Should Run
-

- By default PyTest will automatically discover and run all tests in all properly named modules from the current working directory and sub-directories.
- There are several command line arguments for controlling which discovered tests actually are executed.
  - moduleName - simply specify the module name to run only the tests in that module.
  - DirectoryName/ - Runs any tests found in the specified directory.
  - `-k` expression - Marches tests found that match the evaluatable expression in the string. The string values can include module, class and function names (i.e. "TestClass and TestFunction").
  - `-m` "expression" - Matches tests found that have a "pytest.mark" decorator that matches the specified expression
  - `-v` Report in verbose mode.
  - `-q` Run in quite mode (can be helpful when running hundreds or thousands of test at once).
  - `-s` Don't capture console output (show print statements on the console).
  - `--ignore` Ignore the specified path when discovering test.
  - `--maxfail` Stop after the specified number of failures.