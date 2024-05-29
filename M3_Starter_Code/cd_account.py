from Account import Account 

def create_cd_account(balance, interest_rate, months):
    """Creates a CD account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial CD account balance.
        interest_rate (float): The APR interest rate for the CD account.
        months (int): The length of months for the CD.

    Returns:
        float: The updated CD account balance after adding the interest earned.
        And returns the interest earned.
    """
    cd_account_instance = CDAccount(balance, interest_rate)
    updated_balance, interest_earned = cd_account_instance.calculate_interest(months)
    cd_account_instance.set_balance(updated_balance)
    cd_account_instance.set_interest(interest_earned)
    return updated_balance, interest_earned

class Account:
    def __init__(self, balance, interest=0):
        self.balance = balance
        self.interest = interest / 100  # Convert interest rate from percentage to decimal

    def set_balance(self, updated_balance):
        self.balance = updated_balance

    def set_interest(self, interest_earned):
        self.interest = interest_earned / self.balance if self.balance != 0 else 0

class CDAccount(Account):
    def __init__(self, balance, interest_rate):
        super().__init__(balance, interest_rate)

    def calculate_interest(self, months):
        interest_earned = self.balance * self.interest * (months / 12)
        updated_balance = self.balance + interest_earned
        return updated_balance, interest_earned

# Input from the user
balance = float(input("Enter the initial balance of the account: "))
interest_rate = float(input("Enter the interest rate for the CD account (in percentage): "))
months = int(input("Enter the number of months: "))

# Create a CD account and calculate interest
updated_balance, interest_earned = create_cd_account(balance, interest_rate, months)

# Print account details
print("Account details:")
print("Initial Balance:", balance)
print("Interest Rate:", interest_rate, "%")
print("Updated Balance:", updated_balance)
print("Interest Earned:", interest_earned)