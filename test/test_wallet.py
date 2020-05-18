import pytest
from app import *

#@pytest.mark.parametrize("add,spent,remaining",[
#        (10,5,5),
#        (20,10,10)
#ßß])

@pytest.fixture
def empty_wallet():
        '''Returns a Wallet instance with a zero balance'''
        # returns an empty wallet
        return Wallet()

@pytest.fixture
def wallet():
        '''Returns a Wallet instance with a 20 balance'''
        # returns an empty wallet
        return Wallet(20)

def test_default_initial_amount(empty_wallet):
    assert empty_wallet.balance == 0

def test_spend_cash(wallet):
    wallet.spend_cash(10)
    assert wallet.balance == 10

def test_add_cash(wallet):
    wallet.add_cash(10)
    assert wallet.balance == 30

def test_insufficient_amount_exception(wallet):
    with pytest.raises(InsufficientAmount):
        wallet.spend_cash(100)

#def test_fixture_mark_parameterized(add,spent,remaining):
#        mywallet = Wallet()
#        mywallet.add_cash(add)
#        mywallet.spend_cash(spent)
#        assert mywallet.balance == remaining


