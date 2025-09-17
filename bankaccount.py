# TODO create class BankAccount
class BankAccount:
    def __init__(self, balance=0):
        self.b = balance

    def deposit(self, add):
        self.b+=add

    def withdraw(self, remove):
        if remove>self.b:
            return "Insufficient Funds"
        else:
            self.b-=remove
            return None

    def get_balance(self):
        return self.b
if __name__ == "__main__":
    # create BankAccount below this
    pass