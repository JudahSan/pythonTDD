Using the assert Statement
=

- Pytest allows the use of the built in python assert statement for performing verifications in a unit test.
- Comparison on all of the python data types can be performed using the standard comparison operators.: <,>, <=,>=, ==, and !=
- Pytest expands on the message returned from assert failures to provide more context in the last results.

```py

def test_IntAssert():
  assert 1 == 1
def test_StrAssert():
  assert "str" == "str"
def test_floatAssert():
  assert 1.0 == 1.0
def test_arrayAssert():
  assert [1,2,3] == [1,2,3]
def test_dictAssert():
  assert {"1":1} = {"1":1}
```

Comparing Floating Point Values
-

- Validating floating point valies can sometimes be difficult as internally the value is a binary fractions (i.e. 1/3 is internally 0.3333...)
- Because of this some floating point comparisons that would be expected to pass fail.
- The pytest "approx" function can be used to verify that two floating point values are "approximately" equivalent to each other with a default tolerance of 1e-6

```py
# Failing test
def test_BadFloatCompare():
  assert (0.1+0.2) == 0.3

# Passing test
def test_GoodFloatCompare():
  val = 0.1 + 0.2
  assert val == approx(0.3)

```

Verifying Exceptions
-

- In some cases we want to verify that a function throws an exception under certain conditions.
- Pytest provides the "raises" helper to perform this verification using the "with" keyword. 
- If the specified exception is not raised in the code blocks specified after the "raises" line then the test fails.

```py
def test_Exception():
  with raises(ValueError)
    raise ValueError
```