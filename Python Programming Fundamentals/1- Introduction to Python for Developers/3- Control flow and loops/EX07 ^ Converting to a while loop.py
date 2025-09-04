"""
==============================================
 Name        : Converting to a while loop
 Author      : Mostafa Elsoudy
 Instructions :
Create a while loop to run while tickets_sold is less than max_capacity.
Inside the loop, increment tickets_sold by 1, representing an increase for each ticket sold.
Outside of the loop, print tickets_sold.
==============================================
"""

tickets_sold = 0
max_capacity = 50

# Create a while loop
while tickets_sold < max_capacity:
  
  # Add one to tickets_sold in each iteration
  tickets_sold += 1

# Print the number of tickets sold
print("Sold out:", tickets_sold, "tickets sold!")