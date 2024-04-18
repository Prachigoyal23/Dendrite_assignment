import pandas as pd 
from sklearn.impute import SimpleImputer 
def handle_missing_values(data_path, imputation_strategy="mean"): 
""" Reads a CSV file, identifies missing values, and imputes them using the specified strategy. 
Args: data_path: Path to the CSV file. imputation_strategy: Strategy for imputing missing values (default: "mean"). - "mean": 
Impute with the mean value of the feature (numerical only). - "median": 
Impute with the median value of the feature (numerical only). - "most_frequent": 
Impute with the most frequent value (categorical only). Returns: A pandas DataFrame with missing values imputed. """ 
# Read the CSV data into a DataFrame 
df = pd.read_csv(data_path) 
# Check for missing values 
print(f"Missing values summary:\n {df.isnull().sum()}") 
# Print number of missing values per column 
# Impute missing values based on strategy
if imputation_strategy == "mean": 
# Impute numerical features with mean (replace NaN with mean) 
df = df.fillna(df.mean()) 
# Works for numerical features only elif imputation_strategy == "median":
# Impute numerical features with median 
df = df.fillna(df.median()) 
# Works for numerical features only elif imputation_strategy == "most_frequent": 
# Impute categorical features with most frequent value 
df = df.fillna(df.mode().iloc[0]) 
# Works for categorical features only 
else: print(f"Invalid imputation strategy: {imputation_strategy}. Using 'mean' instead.") 
df = df.fillna(df.mean()) 
# Print post-imputation summary (optional) 
# print(f"Missing values summary after imputation:\n {df.isnull().sum()}") 
return df 
# Example usage data_path = "your_data.csv" 
# Replace with your CSV file path imputation_strategy = "mean" 
# Choose "mean", "median", or "most_frequent" 
df = handle_missing_values(data_path, imputation_strategy) 
# Now you can proceed with your data analysis using the DataFrame 'df' 
print(df.head()) 
# View the first few rows of the DataFrame
