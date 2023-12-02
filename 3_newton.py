import numpy as np

def newton_interpolation(x, y, x_interp):
    n = len(x)
    f = np.zeros((n, n))
    f[:, 0] = y

    for j in range(1, n):
        for i in range(n - j):
            f[i][j] = (f[i+1][j-1] - f[i][j-1]) / (x[i+j] - x[i])

    interp_value = f[0][0]
    for j in range(1, n):
        term = 1
        for i in range(j):
            term *= (x_interp - x[i])
        interp_value += f[0][j] * term

    return interp_value

# Example usage
x =[100, 200, 300, 400, 500]
y = [10, 12, 21, 23, 25]
x_interp = 350

interp_value = newton_interpolation(x, y, x_interp)
print(f"The interpolated value at x = {x_interp} is {interp_value}")
