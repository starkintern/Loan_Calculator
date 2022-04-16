from Loan import Loan, Budget, loan_total, _loan_list
import datetime
import calendar

timedelta = datetime.timedelta
today = datetime.date.today()
days_in_current_month = calendar.monthrange(today.year, today.month)[1]
days_till_end_month = days_in_current_month - today.day
start_date = today + datetime.timedelta(days=days_till_end_month + 1)
end_date = start_date

usr_principal = float(input("Enter principal amount: "))

usr_interest_rate = float(input("Enter interest rate as percentage: ")) / 100

usr_period_input = input("Enter interest period frequency per year (365, 12, 6, 1): ")

usr_income_input = float(input("Enter your monthly income: "))

usr_expenses_input = float(input("Enter your monthly expenses: "))

match usr_period_input.lower:
    case "day" | "days" | "365":
        usr_period_input = 365
    case "month" | "months" | "12":
        usr_period_input = 12
    case "semi-annually" | "bi-annually" | "6":
        usr_period_input = 6
    case "year" | "years" | "1":
        usr_period_input = 1
usr_num_periods = int(input("Enter number of years to accrue interest: "))

loan1 = Loan(principal=usr_principal, interest_rate=usr_interest_rate, period=int(usr_period_input),
             num_periods=usr_num_periods)
print(loan1.loan_interest())

while usr_principal > 0:
    if loan_total > Budget:

    days_in_current_month = calendar.monthrange(end_date.year, end_date.month)[1]
    end_date = end_date + datetime.timedelta(days=days_till_end_month)
