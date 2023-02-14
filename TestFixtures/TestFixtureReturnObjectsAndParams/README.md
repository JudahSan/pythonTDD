Text Fixture Return Objects and Params
=

- Test ficture can optionally return data which can be used int he test.
- The optionsl "params" array argument in the fixture decorator can be used to specify the data returned to the test.
- When a "params" argument is specified then the test will be called one time with each value specified.

```py
@pytest.fixture(params=[1,2])
def setupData(request):
  return request.params

def test1(setupData):
  print(setupData)
```