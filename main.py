from Loan import Loan, Budget, loan_total
import datetime
import calendar

if __name__ == '__main__':
    timedelta = datetime.timedelta
    today = datetime.date.today()
    days_in_current_month = calendar.monthrange(today.year, today.month)[1]
    days_till_end_month = days_in_current_month - today.day
    start_date = today + datetime.timedelta(days=days_till_end_month + 1)
    end_date = start_date

    days_in_current_month = calendar.monthrange(end_date.year, end_date.month)[1]
    end_date = end_date + datetime.timedelta(days=days_till_end_month)

    usr_principal = float(input("Please enter your loan amount: "))

    usr_interest_rate = float(input("Please enter your interest rate as percentage: ")) / 100

    usr_period_input = input("Please enter your interest period frequency per year (365, 12, 6, 1): ")

    # match usr_period_input.lower:
    #     case "day" | "days" | "365":
    #         usr_period_input = 365
    #     case "month" | "months" | "12":
    #         usr_period_input = 12
    #     case "semi-annually" | "bi-annually" | "6":
    #         usr_period_input = 6
    #     case "year" | "years" | "1":
    #         usr_period_input = 1
    usr_num_periods = int(input("Please enter the number of years for your loan to accrue interest: "))

    loan1 = Loan(principal=usr_principal, interest_rate=usr_interest_rate, period=int(usr_period_input),
                 num_periods=usr_num_periods)
    print(f"You will have accrued ${loan1.loan_interest():.2f} in loan interest")

    # The Loop below allows the user to create a list of their loans
    #   by inputting the 4 pieces of data that make up each loan. Once they are finished entering loans,
    #   they will type "no" and the Loop will end and the _loan_list will be created and can then
    #   be iterated over by the loan_total function to sum the loans.

    _loan_list = []
    usr_input = input("Would you like to enter a loan? ")

    while "no" not in usr_input.lower():
        usr_principal = int(input("Please enter your total loan amount: "))
        usr_interest_rate = int(input("Please enter your loan interest rate as a percentage: "))
        usr_period = int(input("Please enter your interest period frequency per year (365, 12, 6, 1): "))
        usr_num_periods = int(input("Please enter how many years you have accrued interest for: "))

        _loan_list.append(Loan(usr_principal, usr_interest_rate, usr_period, usr_num_periods))

        usr_input = input("Would you like to enter another loan? ")

    budget1 = Budget(int(input("Please enter your monthly income: ")),
                     int(input("Please enter your monthly expenses: ")))

    # TODO: I need code that takes loan total created in Loan.py
    #   and subtracts budget1 away until loan_total == 0
    #   The question remains, how do I implement that, using a loop or another method?
    #   It needs to happen every month until the loan_total == 0
    #   Double check conversation with Alec about returns and instances/classes,
    #   how do I use "total" that is returned from the loan_total function in main.py?
