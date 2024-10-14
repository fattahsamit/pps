class BankAccount:
    def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.account_id = account_id
        self.account_type = account_type
        self.pin = pin
        self.balance = balance
    
    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        self.balance = self.balance - amount
    
    def display_balance(self):
        print("Current Account Balance:", self.balance)


my_account = BankAccount('Fattah', 'Samit', 8535421075, 'Savings', 1234, 200.00)
my_account.deposit(96)
my_account.withdraw(25)
my_account.display_balance()