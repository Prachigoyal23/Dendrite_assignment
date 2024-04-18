# Dendrite_assignment 


In the Step-1 file , The Python code implements a machine learning pipeline using scikit-learn. It parses a JSON file containing experiment details and builds a pipeline for data preprocessing, model selection, and hyperparameter tuning. The pipeline handles numerical features with scaling and missing value imputation (mean/custom value), encodes categorical features, and uses GridSearchCV with RandomForestRegressor (customizable) to find the best model configuration. An example demonstrates parsing a JSON file and building the pipeline, but the code for data loading, training, and prediction needs to be added separately.

In the step-2 file, The Python code defines a function handle_missing_values that reads a CSV file, identifies missing values, and imputes them based on a chosen strategy ("mean", "median", or "most_frequent"). It first reads the CSV data into a DataFrame and prints a summary of missing values. It then creates a SimpleImputer object for flexibility (though separate imputers for numerical/categorical data are recommended). The imputation strategy is applied, and an error message is displayed if an invalid strategy is used. The function returns the DataFrame with missing values imputed. An example demonstrates how to use the function with your CSV file path and desired strategy.

In the Step-3 file, 
