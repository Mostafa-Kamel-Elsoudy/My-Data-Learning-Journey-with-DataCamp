"""
==============================================
 Name        : Updating a variable with for loops
 Author      : Mostafa Elsoudy
 Instructions :
Create a variable called tickets_sold with a value of 0.
Create a variable called max_capacity with a value of 30.
Loop through a range starting at 1 and finishing at max_capacity plus one.
Inside the for loop, add 1 to the value of tickets_sold.
==============================================
"""

# Create the tickets_sold variable
tickets_sold = 0

# Create the max_capacity variable
max_capacity = 30

# Loop through a range up to and including max_capacity's value
for tickets in range(1, 31):
  
  # Add one to tickets_sold in each iteration
  tickets_sold += 1
  
print("Sold out:", tickets_sold, "tickets sold!")