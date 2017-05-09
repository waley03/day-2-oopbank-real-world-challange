pen = 0
pen2 = 0


class BankAccount:


  def __init__(self, initial_balance):
        """Creates an account with the given balance."""
        self.money = initial_balance
  def deposit(self, amount):
        """Deposits the amount into the account."""
        self.money += amount
        return self.money

  def withdraw(self, amount):
        """
        Withdraws the amount from the account.  Each withdrawal resulting in a
        negative balance also deducts a penalty fee of 5 dollars from the balance.
        """
        global pen, pen2
        penalty = 5

        if self.money - amount < 0:
            self.money -= (amount + penalty)
            if self == account1:
                pen += 5
            elif self == account2:
                pen2 += 5
        else:
            self.money -= amount
        return self.money

  def get_balance(self):
        """Returns the current balance in the account."""
        return self.money

  def get_fees(self):
        """Returns the total fees ever deducted from the account."""
        global pen, pen2
        if self == account1:
            return pen
        elif self == account2:
            return pen2
