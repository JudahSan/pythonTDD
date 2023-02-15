# TODO

XUnit Style Setup/Teardown functions will execute code before and after:

- Test Modules

```py
def setup_module():
def teardown_module():
```
- Test Functions

```py
def setup_function():
def teardown_function():
```
- Test Classes

```py
def setup_class()
def teardown_class()
```

- Test Methods in Test Classes

```py
def setup_method():
def teardown_method():
```

```
pytest -v -s
```