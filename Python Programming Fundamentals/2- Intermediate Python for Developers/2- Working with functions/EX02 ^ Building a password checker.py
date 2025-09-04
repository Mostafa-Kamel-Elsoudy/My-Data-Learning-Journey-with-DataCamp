"""
==============================================
 Name        : Building a password checker
 Author      : Mostafa Elsoudy
 Instructions :
Define a function called clean_string, which takes an argument called text.
--------------------------------
Inside the function, create a variable called no_spaces, which contains the text with spaces replaced by underscores.
--------------------------------
Inside the function, create a variable called clean_text, which converts characters in no_spaces to lowercase.
--------------------------------
Finish the function by producing clean_text as an output.
==============================================
"""

password = "not_very_secure_2023"

# Define the password_checker function
def password_checker(submission):
  
  # Check that the password variable and the submission match
  if password == submission:
    print("Successful login!")
  
  # Otherwise, print "Incorrect password"
  else:
    print("Incorrect password")

# Call the function    
password_checker("not_very_secure_2023")