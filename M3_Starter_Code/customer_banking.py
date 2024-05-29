
    # Import the create_cd_account and create_savings_account functions
from cd_account import create_cd_account
from savings_account import create_savings_account

# Define the main function
def main():
    # Prompting the user to set the savings balance
    savings_balance = float(input("Enter the savings balance: "))

    # Prompting the user to set the interest rate
    interest_rate = float(input("Enter the interest rate (in percentage): "))

    # Prompting the user to set the number of months
    months = int(input("Enter the number of months: "))

    # Calling the create_savings_account function and passing in the variables
    savings_account = create_savings_account(savings_balance, interest_rate, months)

    # Calculating interest earned
    interest_earned = savings_account.calculate_interest()

    # Printing out the interest earned and updated savings account balance
    print(f"Interest earned on savings account: ${interest_earned:.2f}")
    print(f"Updated savings account balance with interest earned: ${savings_account.balance:.2f}\n")

    # Prompting the user to set the CD balance
    cd_balance = float(input("Enter the CD balance: "))

    # Prompting the user to set the interest rate for CD
    cd_interest_rate = float(input("Enter the interest rate for CD (in percentage): "))

    # Prompting the user to set the number of months for CD
    cd_months = int(input("Enter the number of months for CD: "))

    # Calling the create_cd_account function and passing the obtained variables
    cd_account = create_cd_account(cd_balance, cd_interest_rate, cd_months)

    # Calculating interest earned for CD account
    cd_interest_earned = cd_account.calculate_interest()

    # Printing out the interest earned and updated CD account balance
    print(f"Interest earned on CD account: ${cd_interest_earned:.2f}")
    print(f"Updated CD account balance with interest earned: ${cd_account.balance:.2f}")

if __name__ == "__main__":
    main()