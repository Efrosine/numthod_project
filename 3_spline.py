import numpy as np

def cubic_spline_interpolation(x, y):
    n = len(x)
    
    h = np.diff(x)
    alpha = np.zeros(n)
    for i in range(1, n - 1):
        alpha[i] = 3 / h[i] * (y[i + 1] - y[i]) - 3 / h[i - 1] * (y[i] - y[i - 1])

    l = np.zeros(n)
    mu = np.zeros(n)
    z = np.zeros(n)
    l[0] = 1
    mu[0] = 0
    z[0] = 0

    for i in range(1, n - 1):
        l[i] = 2 * (x[i + 1] - x[i - 1]) - h[i - 1] * mu[i - 1]
        mu[i] = h[i] / l[i]
        z[i] = (alpha[i] - h[i - 1] * z[i - 1]) / l[i]

    l[-1] = 1
    z[-1] = 0
    c = np.zeros(n)
    b = np.zeros(n)
    d = np.zeros(n)

    for j in range(n - 2, -1, -1):
        c[j] = z[j] - mu[j] * c[j + 1]
        b[j] = (y[j + 1] - y[j]) / h[j] - h[j] * (c[j + 1] + 2 * c[j]) / 3
        d[j] = (c[j + 1] - c[j]) / (3 * h[j])

    def S(x_val):
        for j in range(n-1):
            if x[j] <= x_val <= x[j + 1]:
                return y[j] + b[j] * (x_val - x[j]) + c[j] * (x_val - x[j]) ** 2 + d[j] * (x_val - x[j]) ** 3

    return S


x = np.array([100, 200, 300, 400, 500])
y = np.array([11, 13, 21, 23, 25])


spline = cubic_spline_interpolation(x, y)


xi = 350
result = spline(xi)

print("Interpolated value at x =", xi, ":", result)
