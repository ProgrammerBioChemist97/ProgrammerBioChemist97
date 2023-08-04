import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Load the data
data = pd.read_csv("churn_data.csv")

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(data, data["Churn"], test_size=0.2)

# Create a logistic regression model
model = LogisticRegression()

# Train the model on the training data
model.fit(X_train, y_train)

# Make predictions on the test data
predictions = model.predict(X_test)

# Calculate the accuracy of the model
accuracy = model.score(X_test, y_test)

print("Accuracy:", accuracy)
