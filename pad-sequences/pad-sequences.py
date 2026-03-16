import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    # Your code here
    if not max_len:
        max_len = max(len(s) for s in seqs)
    seqs = [s[:max_len] for s in seqs]

    result = np.full((len(seqs), max_len), fill_value = pad_value)

    for i, s in enumerate(seqs):
        result[i, :len(s)] = s

    return result