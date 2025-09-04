"""
==============================================
 Name        : Appending to a list
 Author      : Mostafa Elsoudy
 Instructions :
Create an empty list called authors_below_twenty_five.
Loop through key and value in the authors dictionary.
Inside the for loop, check if the number of books is less than 25.
If so, append the author's name to the authors_below_twenty_five list.
==============================================
"""

# Create an empty list
authors_below_twenty_five = []

# Loop through the authors dictionary
for key, value in authors.items():
  
  # Check for values less than 25
  if value < 25:
    
    # Append the author to the list
    authors_below_twenty_five.append(key)
    
print(authors_below_twenty_five)