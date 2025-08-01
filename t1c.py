# -*- coding: utf-8 -*-
"""T1C.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Tj8Ndfh3l4nVuJNFjcOjjRi0SxHjTjqc
"""

import pandas as pd         # For data manipulation and analysis (loading CSV, creating DataFrames)
import numpy as np          # For numerical operations, especially useful for array manipulation
import matplotlib.pyplot as plt # For creating static, interactive, and animated visualizations
import seaborn as sns       # For making attractive and informative statistical graphics (built on Matplotlib)

from sklearn.model_selection import train_test_split # To split data into training and testing sets
from sklearn.linear_model import LinearRegression    # The core linear regression model
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score # For evaluating model performance

# --- Data Loading ---
# Replace 'train.csv' with the actual path to your dataset if it's not in the same directory.
# For example: df = pd.read_csv('/path/to/your/train.csv')
try:
    df = pd.read_csv('train.csv')
    print("Dataset 'train.csv' loaded successfully!")
except FileNotFoundError:
    print("Error: 'train.csv' not found. Please ensure the file is in the correct directory.")
    print("If the file is in a different location, specify the full path, e.g., pd.read_csv('/path/to/your/train.csv')")

    df = None # Set df to None to avoid errors in subsequent steps if loading fails

df.head()
df.info()
df.describe()

# Actual vs. Predicted Prices Plot
plt.figure(figsize=(6, 4))
sns.scatterplot(x=y_test, y=y_pred, alpha=0.7)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2, label='Ideal Fit') # Diagonal line
plt.xlabel("Actual House Prices")
plt.ylabel("Predicted House Prices")
plt.title("Actual vs. Predicted House Prices (Test Set)")
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.show()

# Residual Plot
residuals = y_test - y_pred
plt.figure(figsize=(5, 3))
sns.scatterplot(x=y_pred, y=residuals, alpha=0.7)
plt.axhline(y=0, color='r', linestyle='--', lw=2, label='Zero Residuals') # Horizontal line at zero
plt.xlabel("Predicted House Prices")
plt.ylabel("Residuals (Actual - Predicted)")
plt.title("Residual Plot (Predicted vs. Residuals)")
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.show()

# Distribution of Residuals
plt.figure(figsize=(5, 3))
sns.histplot(residuals, kde=True, bins=30)
plt.title("Distribution of Residuals")
plt.xlabel("Residuals")
plt.ylabel("Frequency")
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

print("\nLinear Regression analysis complete.")

# Example for SalePrice distribution
plt.figure(figsize=(4, 3))
sns.histplot(df['SalePrice'], kde=True, bins=50)
plt.title('Distribution of Sale Prices')
plt.xlabel('Sale Price')
plt.ylabel('Frequency')
plt.show()

# Select relevant columns for correlation
cols_for_corr = ['GrLivArea', 'BedroomAbvGr', 'FullBath', 'SalePrice']
corr_matrix = df[cols_for_corr].corr()

plt.figure(figsize=(4, 2))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix of Selected Features and Sale Price')
plt.show()

# Assuming y_test and y_pred are already available from model evaluation step
plt.figure(figsize=(5, 3))
sns.scatterplot(x=y_test, y=y_pred, alpha=0.6) # alpha for seeing dense areas
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2) # Ideal line
plt.xlabel("Actual House Prices")
plt.ylabel("Predicted House Prices")
plt.title("Actual vs. Predicted House Prices")
plt.grid(True)
plt.show()

# Assuming 'df' is your loaded DataFrame
plt.figure(figsize=(7, 3))

plt.subplot(1, 3, 1)
sns.histplot(df['SalePrice'], kde=True)
plt.title('Distribution of Sale Price')
plt.xlabel('SalePrice')
plt.ylabel('Frequency')

plt.subplot(1, 3, 2)
sns.histplot(df['GrLivArea'], kde=True)
plt.title('Distribution of Living Area')
plt.xlabel('GrLivArea')
plt.ylabel('Frequency')

plt.subplot(1, 3, 3)
sns.histplot(df['BedroomAbvGr'], kde=True)
plt.title('Distribution of Bedrooms')
plt.xlabel('BedroomAbvGr')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()

# You can do the same for 'FullBath'
sns.histplot(df['FullBath'], kde=True)
plt.title('Distribution of Full Bathrooms')
plt.xlabel('FullBath')
plt.ylabel('Frequency')
plt.show()

# Data Preparation: Select features (X) and target variable (y)
# We'll start with the columns identified in the correlation matrix as examples
features = ['GrLivArea', 'BedroomAbvGr', 'FullBath']
X = df[features]
y = df['SalePrice']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Linear Regression Model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

residuals = y_test - y_pred

# Residuals vs. Predicted Values Plot
plt.figure(figsize=(5, 3))
sns.scatterplot(x=y_pred, y=residuals, alpha=0.6)
plt.axhline(y=0, color='r', linestyle='--', linewidth=2) # Zero line
plt.xlabel("Predicted Prices")
plt.ylabel("Residuals (Actual - Predicted)")
plt.title("Residuals vs. Predicted Values")
plt.grid(True)
plt.show()

# Histogram of Residuals
plt.figure(figsize=(5, 3))
sns.histplot(residuals, kde=True, bins=30)
plt.title('Distribution of Residuals')
plt.xlabel('Residuals')
plt.ylabel('Frequency')
plt.show()

# Assuming y_test and y_pred are already available from your model evaluation step
plt.figure(figsize=(4, 3))
sns.scatterplot(x=y_test, y=y_pred, alpha=0.6)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2) # Diagonal line for ideal predictions
plt.xlabel("Actual House Prices")
plt.ylabel("Predicted House Prices")
plt.title("Actual vs. Predicted House Prices")
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

residuals = y_test - y_pred

plt.figure(figsize=(4, 3))
sns.scatterplot(x=y_pred, y=residuals, alpha=0.6)
plt.axhline(y=0, color='r', linestyle='--', lw=2) # Horizontal line at zero for ideal residuals
plt.xlabel("Predicted House Prices")
plt.ylabel("Residuals (Actual - Predicted)")
plt.title("Residual Plot")
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

plt.figure(figsize=(4, 3))
sns.histplot(residuals, kde=True)
plt.title("Distribution of Residuals")
plt.xlabel("Residuals")
plt.ylabel("Frequency")
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

# Now that y_test and y_pred are defined, we can generate the scatter plot.
plt.figure(figsize=(6, 5))
sns.scatterplot(x=y_test, y=y_pred, alpha=0.6) # alpha for seeing dense areas
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2) # Ideal line
plt.xlabel("Actual House Prices")
plt.ylabel("Predicted House Prices")
plt.title("Actual vs. Predicted House Prices")
plt.grid(True)
plt.show()

