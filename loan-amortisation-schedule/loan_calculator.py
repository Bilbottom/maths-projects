import pandas as pd


class AmortizationCalculator(object):
    """
    A class which calculates the repayment schedule for a fixed-rate loan
    """
    def __init__(self, principal, interest_rate, period):
        self.principal = principal
        self.interest_rate = interest_rate
        self.period = period
        self.schedule = pd.DataFrame(columns=('period_id', 'amortization_amount', 'interest', 'principal', 'balance'))

    def calculate_amortization_amount(self):
        """
        Returns the fixed periodical amortization amount
        """
        x = (1 + self.interest_rate) ** self.period
        return self.principal * (self.interest_rate * x) / (x - 1)

    def amortization_schedule(self):
        """
        Generate the amortization schedule and writes it to a DataFrame class variable
        """
        amortization_amount = self.calculate_amortization_amount()
        number = 1
        balance = self.principal
        while number <= self.period:
            interest = balance * self.interest_rate
            principal = amortization_amount - interest
            balance = balance - principal
            # yield number, amortization_amount, interest, principal, balance if balance > 0 else 0
            self.schedule = self.schedule.append(
                {
                    'period_id': number,
                    'amortization_amount': amortization_amount,
                    'interest': interest,
                    'principal': principal,
                    'balance': max(balance, 0)
                },
                ignore_index=True
            )
            number += 1
