import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Load the dataset
file_path = '/storage/emulated/0/optifyx/advertising.csv'
data = pd.read_csv(file_path)

# Drop the unnecessary column
data = data.drop(columns=['Unnamed: 0'])

# Define features (X) and target (y)
X = data[['TV', 'Radio', 'Newspaper']]
y = data['Sales']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Save evaluation metrics to a text file
results_path = '/storage/emulated/0/optifyx/analysis_results.txt'
with open(results_path, 'w') as file:
    file.write(f"Mean Squared Error (MSE): {mse}\n")
    file.write(f"R-squared (R²): {r2}\n")

# Save the scatter plot to a file
plot_path = '/storage/emulated/0/optifyx/scatter_plot.png'
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Sales")
plt.ylabel("Predicted Sales")
plt.title("Actual vs Predicted Sales")
plt.savefig(plot_path)
plt.close()

print(f"Analysis results saved to: {results_path}")
print(f"Scatter plot saved to: {plot_path}")
