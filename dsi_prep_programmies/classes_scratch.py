class customer:
    """[summary]
    """

    def __init__(self, name, amount, balance=1000):
        self.name = name
        self.balance = balance
        self.amount = amount

    def withdraw(self):
        new_balance = self.balance - self.amount
        if self.amount > self.balance:
            return f'withdraw failure. {amount} is too much, you broke bitch.'
        return f'success. new balance is: {new_balance}'

    def deposit(self):
        new_balance = self.balance + self.amount
        return f'{new_balance}, nice deposit, but you still broken, nigga.'

class dog():
    """[summary]
    """
    def __init__(self, name, age, num_legs=4, tail_size='long'):
        self.name = name
        self.age = age
        self.num_legs = num_legs
        self.tail_size = tail_size

    def roll_over(self):
        pass

    def sit(self):
        pass

    def lay(self):
        pass

    def fetch(self):
        pass

def main():
    """[summary]
    """
    amount = int(input('please enter the amount: '))
    scott = customer('scott', amount)
    #print(scott.withdraw())
    amount = int(input('please enter the amount: '))
    scott = customer('scott', amount)
    #print(scott.deposit())
    spot = dog('spot', 2)

if __name__ == '__main__':
    main()