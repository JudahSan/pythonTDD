import pytest 
from Checkout import Checkout

@pytest.fixture()
def checkout():
  checkout = Checkout()
  checkout.addItemPrice("a", 1)
  checkout.addItemPrice("b",3)
  return checkout

# # Test 1
# # Removed because of duplication
# def test_CanInstantiateCheckout():
#   co = Checkout()

# # Old Test 2
# def test_CanAddItemPrice():
#   # Refactored to test fixture
#   co = Checkout()
#   co.addItemPrice("a", 1)

# # Refactored step 4 by removing unnecessary tests
# def test_CanAddItemPrice(checkout):
#   checkout.addItemPrice("a", 1)

# def test_CanAddItem(checkout):
#   # co = Checkout()
#   checkout.addItem("a")

def test_CanCalcTotal(checkout):
  checkout.addItem("a")
  assert checkout.calcTotal() == 1

def test_GetCorrectTotalWithMultipleItems(checkout):
  checkout.addItem("a")
  checkout.addItem("b")
  assert checkout.calcTotal() == 4

def test_CanAddDiscount(checkout):
  checkout.addDiscount("a", 3, 2)

# skip test
# @pytest.mark.skip
def test_canApplyDiscountRule(checkout):
  checkout.addDiscount("a", 3, 2)
  checkout.addItem("a")
  checkout.addItem("a")
  checkout.addItem("a")
  assert checkout.calcTotal() == 2