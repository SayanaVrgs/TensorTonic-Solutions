def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    # Write code here
    for i in range(steps):
        f_hat = 2*a*x0 + b
        x0 = x0 - lr * f_hat

    return x0