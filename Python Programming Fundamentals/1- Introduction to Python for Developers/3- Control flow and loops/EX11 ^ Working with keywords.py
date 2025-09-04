"""
==============================================
 Name        : Working with keywords
 Author      : Mostafa Elsoudy
 Instructions :
Loop through the keys and values of the genre_sales dictionary.
Inside the loop, check if the genre is "Horror" or "Mystery".
---------------------------
Loop through the keys and values of the genre_sales dictionary.
Inside the loop, check if the genre is "Horror" or "Mystery". 
==============================================
"""

# Loop through the dictionary
for genre, sale in genre_sales.items():
  
  # Check if genre is Horror or Mystery
  if genre == "Horror" or genre == "Mystery":
    print(genre, sale)

----------------------------

# Loop through the dictionary
for genre, sale in genre_sales.items():
  
  # Check if genre is Horror or Mystery
  if genre == "Horror" or genre == "Mystery":
    print(genre, sale)
  
  # Check if genre is Thriller and sale is at least 3 million
  elif genre == "Thriller" and sale >= 3000000:
    print(genre, sale)