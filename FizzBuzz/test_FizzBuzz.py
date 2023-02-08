import pytest 

def fizzBuzz( value ):
  if isMultiple(value, 3):
    if isMultiple(value, 5):
      return "FizzBuzz"
    return "Fizz"
  if isMultiple(value, 5):
    return "Buzz"
  return str(value)
  

def isMultiple( value, mod):
  return (value % mod) == 0

def checkFizBuzz(value, expectedRetVal):
  retVal = fizzBuzz(value)
  assert retVal == expectedRetVal

def test_return1With1PassedIn():
  checkFizBuzz(1, "1")

def test_return2With2PassedIn():
  checkFizBuzz(2, "2")

def test_returnsFizzWith3PassedIn():
  checkFizBuzz(3, "Fizz")

def test_returnsBuzzWith5PassedIn():
  checkFizBuzz(5, "Buzz")

def test_returnsFizzWith6PassedIn():
  checkFizBuzz(6, "Fizz")

def test_returnsBuzzWith10PassedIn():
  checkFizBuzz(10, "Buzz")

def test_returnsFizzBuzzWith15PassedIn():
  checkFizBuzz(15, "FizzBuzz")