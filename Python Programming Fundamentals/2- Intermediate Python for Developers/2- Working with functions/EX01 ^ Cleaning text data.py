"""
==============================================
 Name        : Cleaning text data
 Author      : Mostafa Elsoudy
 Instructions :
Define the password_checker function, which should accept one argument called submission.
--------------------------------
Check if password is equal to submission.
--------------------------------
Add a keyword enabling the conditional printing of "Incorrect password" if password and submission are different.
--------------------------------
Call the function, passing "NOT_VERY_SECURE_2023".
==============================================
"""

# Create the clean_string function
def clean_string(text):
  
  # Replace spaces with underscores
  no_space = text.replace(" ", "_")
  
  # Convert to lowercase
  clean_string = no_space.lower()
  
  # Return the final text as an output
  return clean_string

converted_text = clean_string("I LoVe dATaCamP!")
print(converted_text)