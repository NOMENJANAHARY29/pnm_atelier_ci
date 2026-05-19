class Wallet:
    """
    A class representing a wallet.

    Attributes:
        balance (float): The balance in the wallet.
    """
    def __init__(self, balance):
        self.balance = balance

    def set_balance(self, val):
        self.balance = self.balance + val

    def get_balance(self):
        return self.balance

    def remove_balance(self, val):
        self.balance = self.balance - val
