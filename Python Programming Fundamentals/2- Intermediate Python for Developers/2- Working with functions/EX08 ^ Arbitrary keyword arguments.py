"""
==============================================
 Name        : Arbitrary keyword arguments
 Author      : Mostafa Elsoudy
 Instructions :
Define concat() as a function that accepts arbitrary keyword arguments called kwargs.
--------------------------------
Inside the function, create an empty string.
--------------------------------
Inside the function, loop over the keyword argument's values, using kwarg as the iterator.
--------------------------------
Call concat() with keyword arguments of start equal to "Python", middle equal to "is", and end equal to "great!".
==============================================
"""

# Define a function called concat
def concat(**kwargs):
  
  # Create an empty string
  result = ""
  
  # Iterate over the Python kwargs
  for kwarg in kwargs.values():
    result += " " + kwarg
  return result

# Call the function
print(concat(start="Python", middle="is", end="great!"))