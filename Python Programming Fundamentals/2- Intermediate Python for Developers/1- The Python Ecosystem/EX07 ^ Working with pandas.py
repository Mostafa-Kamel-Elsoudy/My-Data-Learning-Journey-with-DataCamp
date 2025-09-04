"""
==============================================
 Name        : Working with pandas
 Author      : Mostafa Elsoudy
 Instructions :
Import the pandas module using an alias of pd.
Create sales_df by using a pandas function to convert sales into a DataFrame.
Preview the first five rows of sales_df.
==============================================
"""
# Import pandas as pd
import pandas as pd

# Convert sales to a pandas DataFrame
sales_df = pd.DataFrame(sales)

# Preview the first five rows
print(sales_df.head())