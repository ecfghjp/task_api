

class Wallet:
    def __init__(self,balance=0):
        self.balance = balance
    
    def add_cash(self,cash): 
        self.balance+=cash
    
    def spend_cash(self,cash):
        if self.balance < cash:
            raise InsufficientAmount('Top up your wallet')
        self.balance-=cash

class InsufficientAmount(Exception):
    pass
    