"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE
from Account import Account 

# Define a function for the Savings Account
class savings_account:

 def __init__(self, balance, interest):
    self.balance = balance
    self.interest = interest/100

    """Creates a savings account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        float: The updated savings account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    # ADD YOUR CODE HERE

balance = float(input("Enter the initial balance of the account: "))
interest = float(input("Enter the interest rate for the account (in percentage): "))

account_instance = Account(balance, interest)

print("Account details:")
print("Balance:", account_instance.balance)
print("Interest Rate:", account_instance.interest*100, "%")


    # Calculate interest earned
     # ADD YOUR CODE HERE

def interest_earned(balance, interest_rate, months):
    savings_account = Account(balance, interest_rate)
    
    interest_earned = (balance * interest_rate * months) / 12 
    new_balance = balance + interest_earned
    
    savings_account.set_balance(new_balance)
    savings_account.set_interest(interest_earned)
    
    return new_balance, interest_earned


# Take user input for the balance and interest rate
balance = float(input("Enter the initial balance of the account: "))
interest = float(input("Enter the interest rate for the account (in percentage): "))

account_instance = Account(balance, interest)

# Calculate interest earned
def calculate_interest(self):
        interest_earned = self.balance * self.interest
        return interest_earned
interest_earned = account_instance.calculate_interest()

# Print the details of the account
print("Account details:")
print("Balance:", account_instance.balance)
print("Interest Rate:", account_instance.interest * 100, "%")
print("Interest Earned:", interest_earned)


    # Update the savings account balance by adding the interest earned
    # ADD YOUR CODE HERE
class savings_account(Account):
    def __init__(self, balance, interest):
        super().__init__(balance, interest)

    def update_balance(self):
        interest_earned = self.calculate_interest()
        self.balance += interest_earned

        account_instance.update_balance()

print("Updated balance of the savings account:", account_instance.balance)

    # Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE

def set_balance(self, updated_balance):
        new_balance = float(input("Enter the new balance for the savings account: "))
        self.balance = updated_balance
        account_instance.set_balance(new_balance)


    # Pass the interest_earned to the set interest method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE

def set_interest(self, interest_earned):
     self.interest = interest_earned / self.balance
     account_instance.set_interest(interest_earned)

    # Return the updated balance and interest earned.
    # ADD YOUR CODE HERE

class saving_account (Account):
    def __init__(self, balance, interest):
        super().__init__(balance, interest)

    def update_balance(self):
        interest_earned = self.calculate_interest()
        updated_balance = self.balance + interest_earned
        return updated_balance, interest_earned

    def set_interest(self, interest_earned):
        self.interest = interest_earned / self.balance
        return self.interest

