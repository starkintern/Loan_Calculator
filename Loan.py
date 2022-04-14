class Loan:
    def __init__(self, principal, interest_rate, period, num_periods):
        self.num_periods = num_periods
        self.period = period
        self.interest_rate = interest_rate
        self.principal = principal

    def loan_interest(self):
        return (self.principal * (1 + (self.interest_rate / self.period))
                ** (self.period * self.num_periods)) - self.principal


if __name__ == '__main__':
    loan1 = Loan(principal=15000, interest_rate=0.05, period=3, num_periods=12)
    print(f"Loan total: ${loan1.loan_interest():.2f}")
    print(f"Interest rate: {loan1.interest_rate:.2%}")
