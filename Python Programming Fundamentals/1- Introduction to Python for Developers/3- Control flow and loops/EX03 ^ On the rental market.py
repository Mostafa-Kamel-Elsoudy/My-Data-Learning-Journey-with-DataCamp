"""
==============================================
 Name        : On the rental market
 Author      : Mostafa Elsoudy
 Instructions :
Check if num_beds is less than min_num_beds, printing "Insufficient bedrooms" if this is the case.
Else, check if sq_foot is less than or equal to min_sq_foot, printing "Too small" if this is the case.
Else, check if rent is more than max_rent, printing "Too expensive" if this is the case.
Otherwise, print "This looks promising!".
==============================================
"""

# Check the number of beds
if num_beds < min_num_beds:
  print("Insufficient bedrooms")

# Check square feet
elif sq_foot <= min_sq_foot:
  print("Too small")
  
# Check the rent
elif rent > max_rent:
  print("Too expensive")

# If all conditions met
else:
  print("This looks promising!")
