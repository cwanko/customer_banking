"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE

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
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    # ADD YOUR CODE HERE

class Account:
    def __init__(self, balance, interest=0):
        self.balance = balance
        self.interest = interest / 100  # Convert interest rate from percentage to decimal

balance = float(input("Enter the initial balance of the account: "))
interest = float(input("Enter the interest rate for the CD account (in percentage): "))

account_instance = Account(balance)

print("Account details:")
print("Balance:", account_instance.balance)
print("Interest Rate:", account_instance.interest * 100, "%")

    # Calculate interest earned
    # ADD YOUR CODE HERE
interest_earned = account_instance.calculate_interest()

    # Update the CD account balance by adding the interest earned
    # ADD YOUR CODE HERE

class cd_account(Account):
    def __init__(self, balance, interest):
        super().__init__(balance, interest)

    def updated_balance(self):
        interest_earned = self.calculate_interest()
        self.balance += interest_earned
        return self.balance, interest_earned

cd_account_instance = cd_account(balance, interest)

# Calculate and update balance with interest earned

updated_balance, interest_earned = cd_account_instance.updated_balance()

print("Updated balance of the CD account:",updated_balance)

    # Pass the updated_balance to the set balance method using the instance of the CDAccount class.
    # ADD YOUR CODE HERE

def set_balance(self, updated_balance):
        self.balance = updated_balance


    # Pass the interest_earned to the set interest method using the instance of the CDAccount class.
    # ADD YOUR CODE HERE

def set_interest(self, interest_earned):
        self.interest = interest_earned / self.balance
        return self.interest

_, interest_earned = cd_account_instance.update_balance()
updated_interest_rate = cd_account_instance.set_interest(interest_earned)

    # Return the updated balance and interest earned.
     # ADD YOUR CODE HERE

print("Updated balance of the cd_account:", updated_balance)
print("Interest earned on the cd_account:", interest_earned)
