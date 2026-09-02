class BankAccount:
    # Constructor that initialises when object is created
    def __init__(self):
        self.balance = 0    #Attribute with 0 starting amount
        self.accountOpen = False

    # Method
    def get_balance(self):
        if self.accountOpen :
            return self.balance
        else :
            raise ValueError('account not open')

    def open(self):
        if self.accountOpen == False:
            self.balance = 0
            self.accountOpen = True
        else :
            raise ValueError('account already open')

    def deposit(self, amount):
        if self.accountOpen :
            current_balance = self.balance

            if ( amount > 0 ) :
                current_balance += amount
                self.balance = current_balance
            else :
                    raise ValueError('amount must be greater than 0')
        else :
            raise ValueError('account not open')

    def withdraw(self, amount):
        if self.accountOpen :
            current_balance = self.balance

            if amount <= current_balance:
                if ( amount > 0 ) :
                    current_balance -= amount
                    self.balance = current_balance
                else :
                    raise ValueError('amount must be greater than 0')
            else :
                raise ValueError('amount must be less than balance')
        else :
            raise ValueError('account not open')

    def close(self):
        if self.accountOpen :
            self.accountOpen = False
            self.balance = 0
        else :
            raise ValueError('account not open')
