"""
==============================================
 Name        : Adding tax
 Author      : Mostafa Elsoudy
 Instructions:
 Define the add_tax lambda function, which multiplies the argument provided to it, x, by 1.2.
 Call add_tax() on the sale_price variable and print the result.
==============================================
"""

# Given sale price
sale_price = 29.99

# Define a lambda function called add_tax that applies a 20% tax
add_tax = lambda x: x * 1.2

# Call the lambda function and print the taxed sale price
print(add_tax(sale_price))
