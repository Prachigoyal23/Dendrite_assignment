import pandas as pd 
from sklearn.impute import SimpleImputer 
def data_preprocessing_pipeline(data_path, imputation_strategy="mean"): 
""" Performs data loading, feature engineering (if needed), and missing value imputation. 
Args: data_path: Path to the CSV file. imputation_strategy: 
Strategy for imputing missing values (default: "mean"). - "mean": 
Impute with the mean value of the feature (numerical only). - "median": 
Impute with the median value of the feature (numerical only). - "most_frequent": 
Impute with the most frequent value (categorical only). 
Returns: A pandas DataFrame with preprocessed data. """ 
# 1. Load data 
df = pd.read_csv(data_path) 
# 2. Feature engineering (replace with your specific feature engineering logic)
# ... (your feature engineering code here) 
# ... (example: create a new feature 'petal_area' by multiplying petal length and width) 
 df['petal_area'] = df['petal_length'] * df['petal_width'] 
# 3. Handle missing values
# Identify problematic column (assuming error message reveals it) 
problematic_column = None 
# Replace with the actual column name if applicable 
# Handle non-numeric data (assuming it represents categories) 
if problematic_column is not None and df[problematic_column].dtype != "category": 
df[problematic_column] = df[problematic_column].astype("category") 
# Impute missing values in numerical columns (excluding the problematic one) 
numerical_columns = [col for col in df.columns if col != problematic_column and df[col].dtype not in ["object", "category"]] 
if imputation_strategy in ["mean", "median"]: 
df[numerical_columns] = df[numerical_columns].fillna(df[numerical_columns].mean()) 
# For numerical features elif imputation_strategy == "most_frequent":
# Handle missing values in categorical features separately (e.g., using mode) 
if problematic_column is not None: 
df[problematic_column] = df[problematic_column].fillna(df[problematic_column].mode().iloc[0]) 
# Impute with most frequent value for this column else: 
# Handle missing values in other categorical columns (if any) 
categorical_columns = [col for col in df.columns 
if df[col].dtype == "category"] 
for col in categorical_columns: 
df[col] = df[col].fillna(df[col].mode().iloc[0]) 
# Impute with most frequent value for other categorical columns 
else: 
print(f"Invalid imputation strategy: 
{imputation_strategy}. Using 'mean' instead.") 
df = df.fillna(df.mean()) return df 
# Example usage data_path = "your_data.csv" 
imputation_strategy = "mean" 
# Choose based on your data 
df_preprocessed = data_preprocessing_pipeline(data_path, imputation_strategy) 
# Now you can proceed with further data analysis using 'df_preprocessed' 
print(df_preprocessed.head()) 
# View the first few rows
