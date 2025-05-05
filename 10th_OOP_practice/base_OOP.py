import pytest

def test_balance(self):
    assert self > 0

class BankAccount:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def info(self):
        print(self)

    def __str__(self):
        return f"Держатель: {self.owner} \nБаланс: {self.balance}"

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Ошибка при вводе суммы")
        self.balance += amount
        print(f'Баланс пополнен на сумму {amount}.\n'
              f'Текущий баланс пользователя {self.owner}: {self.balance}.')

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Ошибка при вводе суммы")
        self.balance -= amount
        print(f'С баланса списана сумма {amount}.\n'
              f'Текущий баланс пользователя {self.owner}: {self.balance}.')

    def get_balance(self):
        print(f'Текущий баланс пользователя {self.owner}: {self.balance}.')



class SavingAccount(BankAccount):

    def __init__(self, owner, balance=0, interest_rate = 0.05):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        self.balance *= (1+self.interest_rate)
        print(f'На баланс начислено {self.interest_rate*100} процента(-ов).\n'
              f'Текущий баланс пользователя {self.owner}: {self.balance}.')

class CheckingAccount(BankAccount):

    def __init__(self, owner, balance=0):
        super().__init__(owner, balance)

    def withdraw(self, amount):
        self.balance -= amount
        print(f'С баланса списана сумма {amount}.\n'
              f'Текущий баланс пользователя {self.owner}: {self.balance}.')


smpl_user = SavingAccount("Петька")

smpl_user.deposit(500)

smpl_user.withdraw(100)

smpl_user.apply_interest()

smpl_user.info()

smpl_user.deposit(1000)

smpl_user_2 = CheckingAccount("Унал")

smpl_user_2.withdraw(100)

test_balance(smpl_user.balance)

