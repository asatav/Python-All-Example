import sys
class Customer:
    '''Customer class with bank Application.'''
    bankname='SATAV CO OP BANK'
def __init__(self,name,balance=0.0):
    self.name=name 
    self.balance=balance 
def deposite(self,amt):
    self.balance=self.balance+amt 
    print("Balance after deposit:",self.balance)
def withdraw(self,amt):
    if amt>self.balance:
        print("Insufficient funds..cannot perform the operation")
        sys.exit()
    self.balance=self.balance-amt
    print("Balance after withdraw",self.balance)
print("Wlcome to",Customer.bankname)
name=input('Enter your name:')
c=Customer()
while True:
    print('d=Deposite\nw-Withdraw\ne-Exit')
    option=input('Choose your option:')
    if option=='d' or option=='D':
       amt=float(input('Enter Amount:'))
       c.deposite(amt)
    elif option =='w' or option =='W':
       amt=float(input('Enter Amount:'))
       c.withdraw(amt)
    elif option =='e' or option =='E':
         print("Thanks For Banking....")
         sys.exit()
    else:
        print("Invakid Option...Plz choose valid option.")
        
 