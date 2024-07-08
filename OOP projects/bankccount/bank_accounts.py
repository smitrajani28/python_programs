class BalanceException(Exception):
    pass
class BankAccount:
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.name = acctName
        print(f"\n Account '{self.name}' created.\n Balance : ${self.balance:.2f}")
    
    def getBalance(self):
        print(f"\n Account '{self.name}' balance = ${self.balance:.2f}")

    def deposit(self, Amount):
        self.balance += Amount
        print(f"\ndeposit Completed...\n${Amount} debited.. Balance = ${self.balance}")
    def viableTransaction(self, Amount):
        if Amount <= self.balance:
            return
        else:
            raise BalanceException(f"\n Sorry... You don't have suffiecient balance")

    def withdraw(self, Amount):
        try:
            self.viableTransaction(Amount)
            self.balance -= Amount
            print(f"\nwithdraw Completed...\n${Amount} credited..")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")

    def Transfer(self,Amount,Account):
        try:
            print("\n*********************\n\nBegining Transaction")
            self.viableTransaction(Amount)
            self.withdraw(Amount)
            Account.deposit(Amount)
            print("Transaction Complete")
            self.getBalance()
        except BalanceException as error:
            print("Transaction interrupted : {error}")

class InterestRewardAccount(BankAccount):
    def deposit(self, Amount):
        self.balance += (Amount * 1.05)
        print("deposit complete...")
        self.getBalance()

class SavingsAccount(InterestRewardAccount):
    def __init__(self, initialAmount, acctName):
        super().__init__(initialAmount,acctName)
        self.fee = 5
    def withdraw(self,Amount):
        try:
            self.viableTransaction(Amount)
            self.balance -= (Amount + self.fee)
            print("\nwithdraw complete... ${Amount} credited..")
            self.getBalance()
        except BalanceException as error:
            print(f"withdraw intrrupted : {error}")