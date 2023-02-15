Test Fixtures
=

- Test Fixtures allow for re-use of setup and teardown code across tests.
- The "pytest.fixture" decorator is applied to functions that are decorators.
- Individual unit tests can specify which fixtures they want executed
- The `autouse` parameter can be set to true to automatically execute a fixture before each test.

```py
@pytest.fixture():
def math():
  return Math()

def test_Add(math):
  assert math.add(1,1) == 2
```
Test Fixture Teardown
=

- Test Fixtures can each have their own optional teardown code which is called after a fixture goes out of scope.
- There are two methods for specifying teardown code. The `yield` keyword and the request-context object's `addfinalizer`

Test Fixture Teardown - Yeild
-

- When the `yield` keyword is used the code after the yeild is executed after the fixture goes out of scope.
- The `yeild` keyword is a replacement for the return keyword so any return values are also specified in the yeild statement.

```py
@pytest.fixture():
def setup():
  print("Setup!")
  yield
  print("Teardown!")
```
Test Fixture Teardown - addfinalizer
-

- With the addfinalizer method a teardown method is aded via the request-context's addfinalizer method.
- Multiple finalization functions can be specified.

```py
@pytest.fixture():
def setup(request):
  print("Setup!")
  def teardown:
    print("Teardown!")
  request.addfinalizer(teardown)
```

Test Fixtures Scope
=

- Test Fixtures can have the following four different scopes which specify how often the fixture will be called:
  - Function - Run the fixture once for each test
  - Class - Run the fixture once for each class of tests
  - Module - Run once when the module goes in scope
  - Session -  The fixture is run when pytest starts