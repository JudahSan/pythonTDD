
class TestClass:
  @classmethod
  def setup_class(cls):
    print("Setup TestClass!")

  @classmethod
  def teardown_class(cls):
    print("Teardown TestClass!")

  def setup_method(self, method):
    if method == self.test1:
      print("\nSetting up test1!")
    elif method == self.test2:
      print("\nSetting up test2!")
    else:
      print("\nSetting up unknown test!")

  def teardown_method(self, method):
    if method == self.test1:
      print("\nTearing up test1!")
    elif method == self.test2:
      print("\nTearing up test2!")
    else:
      print("\nTearing up unknown test!")

  def test1():
    print("Executing test1!")
    assert True

  def test2():
    print("Executing test2!")
    assert True