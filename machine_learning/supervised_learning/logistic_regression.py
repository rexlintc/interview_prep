import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification

# Generate synthetic data
X, y = make_classification(n_samples=1000, n_features=20, n_classes=2, random_state=42)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Generate synthetic data
X, y = make_classification(n_samples=1000, n_features=20, n_classes=2, random_state=42)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def logistic_regression(X, weights, bias):
    # Compute logits
    z = np.dot(X, weights) + bias
    # Apply sigmoid function
    predictions = sigmoid(z)
    return predictions

def log_loss(y_true, y_pred):
    epsilon = 1e-15  # Small number to avoid division by zero
    return -np.mean(y_true * np.log(y_pred + epsilon) + (1 - y_true) * np.log(1 - y_pred + epsilon))

def gradient_descent(X, y, predictions, weights, bias, learning_rate):
    m = len(y)
    
    # Compute gradients for weights
    weight_gradient = (1 / m) * np.dot(X.T, (predictions - y))
    
    # Compute gradient for bias
    bias_gradient = (1 / m) * np.sum(predictions - y)
    
    # Update weights and bias
    weights -= learning_rate * weight_gradient
    bias -= learning_rate * bias_gradient
    
    return weights, bias

def train_logistic_regression(X_train, y_train, n_iterations=1000, learning_rate=0.01):
    # Initialize weights and bias
    weights = np.random.randn(n_features)
    bias = 0
    
    for iteration in range(n_iterations):
        # Compute predictions
        predictions = logistic_regression(X_train, weights, bias)
        
        # Calculate cost
        cost = log_loss(y_train, predictions)
        
        # Update weights and bias using gradient descent
        weights, bias = gradient_descent(X_train, y_train, predictions, weights, bias, learning_rate)
        
        if iteration % 100 == 0:
            print(f'Iteration {iteration}: Cost = {cost:.4f}')
    
    return weights, bias

# Train the model
weights, bias = train_logistic_regression(X_train, y_train)

# Make predictions on the test set
predictions = logistic_regression(X_test, weights, bias)
predicted_classes = (predictions >= 0.5).astype(int)

# Calculate accuracy
accuracy = np.mean(predicted_classes == y_test)
print(f'Accuracy: {accuracy:.4f}')

