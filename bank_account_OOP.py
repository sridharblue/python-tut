class Account:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self,depo):
        self.balance = self.balance + depo
        print(f'{depo}$ has been deposited, your updated balance is {self.balance}$')
    
    def withdraw(self,widra):
        updated_bal = self.balance - widra
        if updated_bal < 0:
            print(f'Entered amount ({widra}$) is higher than your current account balance {self.balance}$')
              
        else:
            print(f'{widra}$ has been withdrawn, your updated balance is {updated_bal}$')
            self.balance = updated_bal
            
    def __str__(self):
        return f'Account owner: {self.owner}\nAccount balance: {self.balance}'

a = Account('Jose' , 100)   
print(a)
print(a.deposit(50))
print(a)
print(a.withdraw(200))

