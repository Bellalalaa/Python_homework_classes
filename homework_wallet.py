#!/usr/bin/python3

class Money:
    exchangelist = {
        'USD': {'USD': 1.0, 'EUR': 0.89, 'RUB': 57.0, 'AMD': 398.0},
        'EUR': {'USD': 1.12, 'EUR': 1.0, 'RUB': 64.0, 'AMD': 446.0},
        'RUB': {'USD': 0.017, 'EUR': 0.0156, 'RUB': 1.0, 'AMD': 6.98},
        'AMD': {'USD': 0.0025, 'EUR': 0.00224, 'AMD': 1.0, 'RUB': 0.143},
    }

    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency
        if currency not in Money.exchangelist:
            raise ValueError("The currency you entered doesn't exist")

    def change_currency(self, which_cur):
        rate = Money.exchangelist[self.currency][which_cur]
        converted_amount = self.amount * rate
        return Money(converted_amount, which_cur)

    def add(self, user_input):
        if self.currency == user_input.currency:
            total = self.amount + user_input.amount
        else:
            converted = user_input.change_currency(self.currency)
            total = self.amount + converted.amount
        return Money(total, self.currency)

    def subtract(self, user_input):
        if self.currency == user_input.currency:
            total = self.amount - user_input.amount
        else:
            converted = user_input.change_currency(self.currency)
            total = self.amount - converted.amount
        return Money(total, self.currency)

    def mult(self, num):
        return Money(self.amount * num, self.currency)

    def divide(self, num):
        return Money(self.amount / num, self.currency)

    def if_equal(self, user):
        conver = user.change_currency(self.currency)
        return self.amount == conver.amount

    def __str__(self):
        return f"{self.amount} {self.currency}"

def main():
    a = Money(100, 'USD')
    b = Money(45000, 'AMD')

    print("a + b =", a.add(b))
    print("a - b =", a.subtract(b))
    print("a * 2 =", a.mult(2))
    print("a / 4 =", a.divide(4))
    print("a == b?", a.if_equal(b))

if __name__ == "__main__":
    main()

