import json 
from sklearn.pipeline import Pipeline 
from sklearn.preprocessing import StandardScaler, OneHotEncoder, SimpleImputer 
from sklearn.compose import ColumnTransformer 
from sklearn.ensemble import RandomForestRegressor 
from sklearn.model_selection import GridSearchCV 
def parse_json(json_file_path): 
  """ Parses the JSON file containing experiment details, handling potential errors. 
  Args: 
  json_file_path: Path to the JSON file. 
  Returns: 
  A dictionary containing the parsed data if successful, or None otherwise. """ 
  try: 
  with open(json_file_path, 'r') as f: 
    data = json.load(f) 
    return data 
except (FileNotFoundError, JSONDecodeError) as e: 
print(f"Error parsing JSON file: {e}") 
return None 
def build_pipeline(data): 
  """ Builds a scikit-learn pipeline based on the parsed JSON data. 
  Args: 
  data: 
  A dictionary containing the parsed JSON data (or None if parsing failed). 
  Returns: 
  A scikit-learn pipeline object, or None if data is invalid. """ 
  if data is None: 
    print("Error: Invalid JSON data. Pipeline cannot be built.") 
    return None 
# Feature Preprocessing Steps 
    preprocessing_steps = [] 
    try: 
    for feature_name, feature_details in data["feature_handling"].items(): 
    if feature_details["feature_variable_type"] == "numerical": 
      # Numerical features: Apply standard scaling 
      preprocessing_steps.append((f"{feature_name}_scaler", StandardScaler())) 
# Handle missing values based on user selection 
      if feature_details["missing_values"] == "Impute": 
      if feature_details["impute_with"] == "Average of values": 
        preprocessing_steps.append((f"{feature_name}_imputer", Imputer(strategy="mean"))) 
      elif feature_details["impute_with"] == "custom": 
        imputation_value = feature_details["impute_value"] 
        preprocessing_steps.append((f"{feature_name}_imputer", Imputer(strategy="constant", fill_value=imputation_value))) 
      else: 
        # Categorical features: Apply one-hot encoding 
        preprocessing_steps.append((f"{feature_name}_encoder", OneHotEncoder(handle_unknown="ignore"))) 
except KeyError: 
print("Error: JSON data missing 'feature_handling' key. Pipeline cannot be built.") 
return None 
# Feature Transformer (if multiple preprocessing steps) 
if len(preprocessing_steps) > 1: 
  preprocessor = ColumnTransformer(transformers=preprocessing_steps) 
else: 
  preprocessor = preprocessing_steps[0][1] 
  if preprocessing_steps 
  else None 
# Model Selection and Hyperparameter Tuning try: 
  model = RandomForestRegressor() 
# Select model based on "prediction_type" (regression in this case) 
  hyperparameters = data["hyperparameters"] 
  param_grid = { # Define hyperparameter grid search space based on data["hyperparameters"] "max_depth": [int(x) for x in data["hyperparameters"]["max_depth"].split(",")], "min_samples_split": [int(x) for x in data["hyperparameters"]["min_samples_split"].split(",")], "n_estimators": [int(x) for x in data["hyperparameters"]["n_estimators"].split(",")], } 
    grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=5, scoring="neg_mean_squared_error") 
except KeyError: 
print("Error: JSON data missing 'hyperparameters' key. Pipeline cannot be built.") 
return None 
# Build the pipeline 
pipeline = Pipeline(steps=[ ("preprocessor", preprocessor), ("model", grid_search) ]) 
return pipeline 
# Example usage 
data = parse_json("algoparams_from_ui.json") 
# Replace with your JSON file path 
if data is not None: 
  pipeline = build_pipeline(data) 
# Use the pipeline for training, fitting, and prediction
  # ... (add your code for data loading, training, and prediction)
