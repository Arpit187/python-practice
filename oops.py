class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient amount")
        else:
            self.__balance -= amount

    def display(self):
        return self.__balance


account = BankAccount("Arpit", 11000)

account.deposit(2000)
account.withdraw(3000)

print(account.display())
        
        

        




