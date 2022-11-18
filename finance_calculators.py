import math
# This project is a program that allows the user to access two different financial calculators:
# an investment calculator and a home loan repayment calculator.
# The user is be allowed to choose which calculation they want to do.

# Ask the user for their choice (investment or bond) 
choice = input('''Choose either 'investment or 'bond' from the menu below to proceed:
    
investment - to calculate the amount of interest you'll earn on your investment 
bond       - to calculate the amount you'll have to pay on a home loan \n''').lower()

# Error message for incorrect selection
error = "Ooopss. Something went wrong. Try again."

# Calculate and display total interest for investment formula
if choice == "investment":
    deposit = float(input("Enter the amount you want to deposit: \n"))
    interest_rate = float(input("Enter the interest rate %: \n"))
    num_years = float(input("Enter the number of years you are planning investing: \n"))
    interest = input("Do you prefer 'simple' or 'compound' interest? Type your choice here: \n").lower()
    # Calculate and display the total earnings for "simple" investment category
    if interest == "simple":
       total_simple = round(float(deposit * (1 + (interest_rate/100) * num_years)), 2)
       print(f'''Based on your selection:

Initial Deposit              £{deposit} 
Interest Rate                 {interest_rate} % 
Investing Years               {num_years} 

Total Earnings               £{total_simple} ''')
    # Calculate and display total earnings for "compound" investment category
    elif interest == "compound":
        total_compound = round(deposit * math.pow(1 + (interest_rate/100), num_years), 2)
        print(f'''Based on your selection:

Initial Deposit              £{deposit} 
Interest Rate                 {interest_rate} % 
Investing Years               {num_years} 

Total Earnings               £{total_compound} 
''')
    else:
        print(error)

# Calculate and display total bond repayment formula
elif choice == "bond":
    house_price = float(input("Enter the value of the house: \n"))
    annual_interest_rate = float(input("Enter the annual interest rate: \n"))
    monthly_interest_rate = float((annual_interest_rate /100) / 12) 
    bond_period = int(input("Enter the number of months the bond will be repaid: \n"))
    repayment = round((monthly_interest_rate * house_price) / (1 - (1 + monthly_interest_rate) ** (- bond_period)), 2)
    print(f'''Based on your selection: 
    
House Price                £{house_price} 
Interest Rate               {annual_interest_rate} %
Repayment Time              {bond_period}

Montly Repayment           £{repayment}
    ''')

else:
    print(error)
