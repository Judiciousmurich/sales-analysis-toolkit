import pandas as pd

# Define file path
raw_data_path = "data/raw/sales_data.csv"

# Load the CSV file
data = pd.read_csv(raw_data_path)
print("Data Loaded:\n", data.head())
