"""
==============================================
 Name        : Importing from a module
 Author      : Mostafa Elsoudy
 Instructions :
Import the date function from the datetime module.
Create a variable called deadline, assigning a call of date(), passing in the numbers 2024, 1, and 19, in that order, separated by commas.
Check the data type of deadline.
Print the deadline variable.
==============================================
"""
# Import date from the datetime module
from datetime import date

# Create a variable called deadline
deadline = date(2024, 1, 19)

# Check the data type
print(type(deadline))

# Print the deadline
print(deadline)