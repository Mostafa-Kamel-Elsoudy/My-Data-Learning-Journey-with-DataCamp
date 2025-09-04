"""
==============================================
 Name        : Adding a keyword argument
 Author      : Mostafa Elsoudy
 Instructions :
Define clean_text, which has two arguments: text, and lower, with the latter having a default value of True.
--------------------------------
Re-define clean_text with arguments of text followed by remove, with the latter having a default value of None.
==============================================
"""
# Define clean_text
def clean_text(text, lower=True):
    # Replace spaces with underscores
    clean_text = text.replace(" ", "_")
    
    # If lower is True, convert the text to lowercase
    if lower:
        clean_text = clean_text.lower()
        
    return clean_text


print("=" * 50)

# Define clean_text
def clean_text(text, remove = None):
  if remove != None:
    clean_text = text.replace(remove, "")
    clean_text = clean_text.lower()
    return clean_text
  else:
    clean_text = text.lower()
    return clean_text
  


