"""
==============================================
 Name        : Checking inflation
 Author      : Mostafa Elsoudy
 Instructions :
Check if inflation_september is less than inflation_august, 
printing "Inflation decreased" if this is the case.
--
Else, check if inflation_september is more than inflation_august, 
printing "Inflation increased" if true.
--
Otherwise, print "Inflation remained stable".

==============================================
"""

# Example inflation data for September and August
inflation_september = 5.4  # Replace with actual data
inflation_august = 5.6     # Replace with actual data

# Check if September inflation is less than August inflation
if inflation_september < inflation_august:
    print("Inflation decreased")
--
# Example inflation data for September and August
inflation_september = 5.4  # Replace with actual data
inflation_august = 5.6     # Replace with actual data

# Check if September inflation is less than August inflation
if inflation_september < inflation_august:
    print("Inflation decreased")
# Check if September inflation is more than August inflation
elif inflation_september > inflation_august:
    print("Inflation increased")
--
# Check if September inflation is less than August inflation
if inflation_september < inflation_august:
  print("Inflation decreased")

# Check if September inflation is more than August inflation
elif inflation_september > inflation_august:
  print("Inflation increased")
  
# Confirm that they are equal
else:
  print("Inflation remained stable")