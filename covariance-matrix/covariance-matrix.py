import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    # Write code here
    X = np.asarray(X)
    if X.ndim < 2:
        return None
    n_sample, n_feature = X.shape
    #print(f"{X.ndim} is the dimensions of X array")
    if n_sample< 2: 
        return None
    #print(f"{X.shape} is the sahpe of X array")
    mu = np.mean(X, axis = 0)
    #print(f"{mu} is the mean of x")
    x_cen = X - mu
    #print(f"{x_cen} is the centered x")
    cov = (x_cen.T @ x_cen) /(n_sample - 1)
    
    #print(f"{cov} is the covariance")
    return cov