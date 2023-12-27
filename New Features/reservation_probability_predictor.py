import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Load your dataset (replace 'your_dataset.csv' with your actual file)
data = pd.read_csv('your_dataset.csv')

# Assume you have features 'num_previous_reservations', 'booking_channel', etc.
features = ['num_previous_reservations', 'booking_channel', ...]

# Select features and target variable
X = data[features]
y = data['reservation_confirmed']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a logistic regression model
model = LogisticRegression()

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test set
predictions = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, predictions)
print(f'Accuracy: {accuracy:.2f}')

# Print classification report for more detailed metrics
print(classification_report(y_test, predictions))

# Now, you can use the trained model to predict reservation probability for new data
# Example prediction for a new reservation
new_data = pd.DataFrame([[3, 'Online']], columns=['num_previous_reservations', 'booking_channel'])
new_prediction = model.predict_proba(new_data)
print(f'Probability of reservation confirmation: {new_prediction[0][1]:.2%}')
