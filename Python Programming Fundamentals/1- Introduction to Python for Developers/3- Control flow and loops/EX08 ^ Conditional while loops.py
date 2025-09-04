"""
==============================================
 Name        : Conditional while loops
 Author      : Mostafa Elsoudy
 Instructions :
Create a while loop based on current_date being less than or equal to release_date.
Increment current_date by one for each day that passes.
Check if current_date is less than 21 and, if so, print "Purchase before the 21st for early access"
Otherwise, check if current_date is less than or equal to 25, printing "Coming soon!".
==============================================
"""

release_date = 26
current_date = 19

# Create a condition where current_date is less than or equal to the release_date
while current_date <= release_date:
  
  # Increment current_date by one
  current_date += 1
  
  # Promote purchases
  if current_date < 21:
    print("Purchase before the 21st for early access")
  
  # Check if the date is less than or equal to the 25th
  elif current_date <= 25:
    print("Coming soon")
  else:
    print("Available now!")