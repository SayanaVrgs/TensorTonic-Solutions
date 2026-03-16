import numpy as np

def _sigmoid(z):
    """Numerically stable sigmoid implementation."""
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X, y, lr=0.1, steps=1000):
    """
    Train logistic regression via gradient descent.
    Return (w, b).
    """
    # Write your code here
    n_sample , n_features = X.shape
    w = np.zeros(n_features)
    b = 0.0
    for step in range(steps): 
        y_hat = _sigmoid(X @ w +b)
        loss = y_hat - y 
        dw = (X.T @ loss) / n_sample
        db = np.mean(loss)

        w = w - lr * dw
        b = b - lr * db

    return (w,b)
        
        
    
    