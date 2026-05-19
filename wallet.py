class Wallet:
    """
    A class representing a wallet.

    Attributes:
        balance (float): The balance in the wallet.
    """
    def __init__(self, balance):
        """
        Initialisation of Wallet class

        Args:
            balance (float): The first number.
        """
        self.balance = balance

    def set_balance(self, val):
        self.balance = self.balance + val

    def get_balance(self):
        return self.balance

    def remove_balance(self, val):
        """
        Substracts a value from balance

        Args:
            val (float): Value to be substracted from balance.

        Returns:
            float: The substraction of balance and val
        """
        self.balance = self.balance - val
