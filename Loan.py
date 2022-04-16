class Loan:
    def __init__(self, principal, interest_rate, period, num_periods):
        self.num_periods = num_periods
        self.period = period
        self.interest_rate = interest_rate
        self.principal = principal

    def loan_interest(self):
        return (self.principal * (1 + (self.interest_rate / self.period))
                ** (self.period * self.num_periods)) - self.principal


def loan_total(_loan_list):
    total = 0
    for i in _loan_list:
        total += i


_loan_list = []
usr_input = input("Would you like to enter a loan? ")

while usr_input != "no":
    usr_principal = input("Please enter your total loan amount: ")
    usr_interest_rate = input("Please enter your loan interest rate as a percentage: ")
    usr_period = input("Please enter your interest period frequency per year (365, 12, 6, 1): ")
    usr_num_periods = input("Please enter how many years you have accrued interest for: ")

    _loan_list.append(Loan(usr_principal, usr_interest_rate, usr_period, usr_num_periods))

    usr_input = input("Would you like to enter another loan? ")


class Budget:
    def __init__(self, income, expenses):
        self.income = income
        self.expenses = expenses
        self.budget = self.income - self.expenses


if __name__ == '__main__':
    loan1 = Loan(principal=15000, interest_rate=0.05, period=3, num_periods=12)
    print(f"Loan total: ${loan1.loan_interest():.2f}")
    print(f"Interest rate: {loan1.interest_rate:.2%}")
