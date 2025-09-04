"""
==============================================
 Name        : Adding arbitrary arguments
 Author      : Mostafa Elsoudy
 Instructions :
Define a function called concat() that accepts arbitrary arguments called args.
--------------------------------
Create a variable called result and assign an empty string to it.
--------------------------------
Use a for loop to iterate over each arg in args.
--------------------------------
Call the function to test that it works correctly.
==============================================
"""

# Define a function called concat
def concat(*args):
  
  # Create an empty string
  result = ""
  
  # Iterate over the Python args tuple
  for arg in args:
    result += " " + arg
  return result

# Call the function
print(concat("Python", "is", "great!"))