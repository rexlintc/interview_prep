import numpy as np

# Function to calculate the mean squared error
def mse(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)

# Function to perform linear regression using gradient descent
def simple_linear_regression(X, y, learning_rate=0.01, n_iterations=1000):
    # Initialize parameters
    m = b = 0
    n = len(y)
    
    for _ in range(n_iterations):
        # Calculate predictions
        y_pred = m * X + b
        
        # Compute gradients
        dm = (-2/n) * np.sum(X * (y - y_pred))
        db = (-2/n) * np.sum(y - y_pred)
        
        # Update parameters
        m -= learning_rate * dm
        b -= learning_rate * db
    
    return m, b

# Example usage
if __name__ == "__main__":
    # Sample data
    X = np.array([1, 2, 3, 4, 5])
    y = np.array([2, 4, 6, 8, 10])
    
    # Train the model
    m, b = simple_linear_regression(X, y)
    print(f"Optimal parameters: m = {m}, b = {b}")
    
    # Predict new values
    X_new = np.array([6, 7, 8, 9])
    y_pred = m * X_new + b
    print("Predictions:", y_pred)
    
    # Calculate MSE
    mse_value = mse(y, y_pred)
    print(f"MSE: {mse_value}")
