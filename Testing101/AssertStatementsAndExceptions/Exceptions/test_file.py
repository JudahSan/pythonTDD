import pytest 
from pytest import raises

def raisesValueException():
  pass
  raise ValueError

def test_exception():
  with raises(ValueError):
    raisesValueException()