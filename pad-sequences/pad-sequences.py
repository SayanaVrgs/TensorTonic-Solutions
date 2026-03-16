import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    # Your code here 
    if not seqs:
        return np.full(shape=(0, 0), fill_value=pad_value)
    cols = [len(seq) for seq in seqs]
    if not max_len:
        max_len = max(cols)
    #print(max_len)
    rows = len(seqs)
    result = np.full(shape = (rows, max_len), fill_value = pad_value)
    for r in range(rows):
        for mx in range(max_len):
            if mx <  cols[r]:
                result[r][mx] = seqs[r][mx]

    return result
    