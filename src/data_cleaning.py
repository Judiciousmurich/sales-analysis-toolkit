#  Loading the Data
import pandas as pd

# Load the CSV file
data = pd.read_csv("../data/sales_data.csv")
print("Data Loaded:\n", data.head())

# Cleaning the Data
# 1. Handling Missing Values:
print("Missing Values:\n", data.isnull().sum())