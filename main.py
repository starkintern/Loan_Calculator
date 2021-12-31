def loan_interest(principal, interest_rate, period, num_periods):
    return (principal * (1 + (interest_rate / period)) ** (period * num_periods)) - principal


usr_principal = int(input("Enter principal amount: "))

usr_interest_rate = float(input("Enter interest rate in percentage: ")) / 100

usr_period = int(input("Enter interest period (Day, month, or year): "))

usr_num_periods = int(input("Enter number of interest periods: "))

interest = loan_interest(principal=usr_principal, interest_rate=usr_interest_rate, period=usr_period,
                         num_periods=usr_num_periods)


print(f"You will owe ${interest:.2f} in interest")
