import numpy as np

def positional_encoding(seq_len, d_model, base=10000.0):
    """
    Return PE of shape (seq_len, d_model) using sin/cos formulation.
    Odd d_model -> last column is sin.
    """
    # Write code here()
    pe = np.zeros((seq_len, d_model))
    col_vec = np.arange(seq_len).reshape(-1, 1)
    row_vec = np.arange(np.ceil(d_model/2)).reshape(1, -1)

    angles = col_vec / np.power(base, (2*row_vec)/d_model)
    print(angles)

    pe[:,0::2] = np.sin(angles)
    pe[:, 1::2] = np.cos(angles[:, :pe[:,1::2].shape[1]])
    

    return pe
