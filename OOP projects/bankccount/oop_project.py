from bank_accounts import *

smit = BankAccount(500000, 'smit')
karan = BankAccount(700000, 'karan')

smit.getBalance()
karan.getBalance()

smit.deposit(5000)
karan.deposit(7000)

smit.withdraw(50000)
karan.withdraw(800000)

smit.Transfer(5000, karan)
karan.Transfer(500000, smit)

pratik = InterestRewardAccount(900000, "pratik")
pratik.getBalance()
pratik.deposit(10000)
pratik.Transfer(500,smit)

rahul = SavingsAccount(900000, "rahul")
rahul.withdraw(800000)