class Account:
    def __init__(self,name,balance,min_balance):
        self.name=name
        self.balance=balance
        self.min_balance=min_balance
        
    def deposite(self,amount):
        self.balance+=amount
        
    def withdraw(self,amount):
        if  self.balance-amount >= self.min_balance:
            self.balance-=amount
        else:
            print("Sorry Insufficient Funds")
    def printStatement(self):
        print("Account Balance:-",self.balance)
        
class Current(Account):
    def __init__(self,name,balance):
        super().__init__(name, balance, min_balance=-1000)
    def __str__(self):
        return "{}'s Current Account with Balance :{}".format(self.name,self.balance)
    
class Saving(Account):
    def __init__(self,name,balance):
        super().__init__(name, balance, min_balance=0)
    def __str__(self):
        return "{}'s Current Account with Balance :{}".format(self.name,self.balance) 
        
c=Saving("ASHISH",10000)
print(c)
c.deposite(5000)
c.printStatement()
c.withdraw(2000) 
c.withdraw(500)
print(c)

c2=Current("AJIT",50000)
c2.deposite(10000)
print(c2)
c2.withdraw(27000)
print(c2)        
        
        