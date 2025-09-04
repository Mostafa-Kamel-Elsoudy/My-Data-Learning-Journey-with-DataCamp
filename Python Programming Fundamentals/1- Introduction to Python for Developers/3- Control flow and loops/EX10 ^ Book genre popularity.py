"""
==============================================
 Name        : Book genre popularity
 Author      : Mostafa Elsoudy
 Instructions :
Filter where average_sale is equal to the largest sales revenue (5166000000) in genre_sales.
Print the genre with the largest average sales.
Next, filter where average_sale is equal to the smallest sales revenue (80000000).
Lastly, print the genre with the smallest average sales.
==============================================
"""

for genre, average_sale in genre_sales.items():
    
    # Filter for the maximum sales value
    if average_sale == 5166000000:
      
      # Print the genre
      print("Most popular genre: ", genre_sales)
      print("Average sales: ", average_sale)
    
    # Filter for the minimum sales value
    elif average_sale == 80000000:
      
      # Print the genre
      print("Least popular genre: ", genre_sales)
      print("Average sales: ", average_sale)