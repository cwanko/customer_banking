from Account import Account 

class SavingsAccount(Account):
    """Creates a savings account, calculates interest earned, and updates the account balance.
    
    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
    
    Methods:
        calculate_interest(months): Calculates the interest earned and updates the balance.
    """
    
    def __init__(self, balance, interest_rate):
        super().__init__(balance, interest_rate / 100)  # Convert percentage to a decimal
    
    def calculate_interest(self, months):
        interest_earned = self.balance * self.interest * (months / 12)
        self.balance += interest_earned
        return self.balance, interest_earned
                                                      # remove L21-L23 later
def create_savings_account(balance, interest_rate, months):
    return SavingsAccount(balance, interest_rate, months)


# Input from the user
balance = float(input("Enter the initial balance of the account: "))
interest_rate = float(input("Enter the interest rate for the account (in percentage): "))

# Create an instance of SavingsAccount
account_instance = SavingsAccount(balance, interest_rate)

# Calculate interest earned and update balance
months = int(input("Enter the number of months: "))
updated_balance, interest_earned = account_instance.calculate_interest(months)

# Print account details
print("Account details:")
print("Initial Balance:", balance)
print("Interest Rate:", interest_rate, "%")
print("Updated Balance:", updated_balance)
print("Interest Earned:", interest_earned) 