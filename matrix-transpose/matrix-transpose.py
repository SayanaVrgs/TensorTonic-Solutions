import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    x = np.asarray(A)
    #print(f"{x} is A")
    r, c = x.shape
    new_x = np.zeros((c, r))
    for row in range(r):
        for col in range(c):
            new_x[col][row] = x[row][col]

    #print(f"{new_x} is new_x")
    return new_x
    
