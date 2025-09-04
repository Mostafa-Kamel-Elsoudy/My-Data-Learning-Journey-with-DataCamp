"""
==============================================
 Name        : Working with dictionaries
 Author      : Mostafa Elsoudy
 Instructions :
Print the name of the song in the playlist that is by the artist "Coldplay".
Add a new key-value pair to the playlist, where the key is "Usher" and the value is "Yeah!".
Print only the songs in the playlist.
==============================================
"""
# Print the song by Coldplay
print(playlist["Coldplay"]) 

# Add a new song by Usher
playlist["Usher"] = "Yeah!"

# Print only the songs (values) in the playlist
print(list(playlist.values()))
