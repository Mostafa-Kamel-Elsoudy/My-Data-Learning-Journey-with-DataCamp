"""
==============================================
 Name        : Single-line docstrings
 Author      : Mostafa Elsoudy
 Instructions :
 Add a docstring stating '''Swap spaces to underscores and convert text to lowercase.'''--------------------------------
Add a condition to check if data_type is "tuple".
--------------------------------
Access the function's docstring using the appropriate attribute.
==============================================
"""

def clean_string(text):
  
  # Add a single-line docstring
  """Swap spaces to underscores and convert text to lowercase."""  
  
  no_spaces = text.replace(" ", "_")
  clean_text = no_spaces.lower()
  return clean_text

# Access the docstring
print(clean_string.__doc__)