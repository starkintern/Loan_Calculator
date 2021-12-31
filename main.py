def loan_interest(principal, interest_rate, period, num_periods):
    return (principal * (1 + (interest_rate / period)) ** (period * num_periods)) - principal


usr_principal = float(input("Enter principal amount: "))

usr_interest_rate = float(input("Enter interest rate as percentage: ")) / 100

usr_period = input("Enter interest period frequency per year (365, 12, 6, 1): ")

match usr_period.lower:
    case "day" | "days" | "365":
        usr_period = 365
    case "month" | "months" | "12":
        usr_period = 12
    case "semi-annually" | "bi-annually" | "6":
        usr_period = 6
    case "year" | "years" | "1":
        usr_period = 1

usr_num_periods = int(input("Enter number of years to accrue interest: "))

interest = loan_interest(principal=usr_principal, interest_rate=usr_interest_rate, period=int(usr_period),
                         num_periods=usr_num_periods)

print(f"You will owe ${interest:.2f} in interest")
