from Loan import Loan

usr_principal = float(input("Enter principal amount: "))

usr_interest_rate = float(input("Enter interest rate as percentage: ")) / 100

usr_period_input = input("Enter interest period frequency per year (365, 12, 6, 1): ")

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


loan1 = Loan(principal= usr_principal, interest_rate= usr_interest_rate, period=int(usr_period_input),
             num_periods= usr_num_periods)
print(loan1.loan_interest())

