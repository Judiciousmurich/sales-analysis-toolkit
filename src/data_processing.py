#  Loading the Data
import pandas as pd

# Load the CSV file
data = pd.read_csv("../data/sales_data.csv")
print("Data Loaded:\n", data.head())

# Cleaning the Data
# 1. Handling Missing Values:
print("Missing Values:\n", data.isnull().sum())

# Fill missing Quantity with 0 and drop rows with missing Product
data['Quantity'].fillna(0, inplace=True)
data.dropna(subset=['Product'], inplace=True)
print("Data after Handling Missing Values:\n", data)

import pandas as pd

# Assuming you have already loaded your data into the 'data' DataFrame
# If you haven't loaded the data yet, use the following code to load the CSV file:
# data = pd.read_csv('sales_data.csv')

# Step 1: Check column names for any leading or trailing spaces
data.columns = data.columns.str.strip()  # Remove leading/trailing spaces from column names

# Step 2: Verify the columns in your dataframe
print("Columns in Dataframe:\n", data.columns)

# Step 3: Check for the presence of the 'Date' column
if 'Date' in data.columns:
    # Step 4: Convert 'Date' to datetime format, handle errors by coercing invalid values to NaT
    data['Date'] = pd.to_datetime(data['Date'], errors='coerce')

    # Step 5: Check the data types after conversion
    print("Data Types After Conversion:\n", data.dtypes)

    # Step 6: Check for any missing or invalid dates (NaT)
    print("\nMissing or Invalid Dates:\n", data[data['Date'].isnull()])
else:
    print("The 'Date' column is missing from the dataset.")
    
    # Remove duplicates
data.drop_duplicates(inplace=True)
print("Data after Removing Duplicates:\n", data)

# Calculate total sales
data['TotalSales'] = data['Quantity'] * data['Price']
print("Data with Total Sales:\n", data)

# Filter sales for Widget A
widget_a_sales = data[data['Product'] == 'Widget A']
print("Sales for Widget A:\n", widget_a_sales)

# Group by Product and sum TotalSales
summary = data.groupby('Product')['TotalSales'].sum().reset_index()
print("Sales Summary by Product:\n", summary)