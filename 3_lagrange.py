def lagrange_interpolation(x, y, xi):

    n = len(x)
    yi = 0

    for i in range(n):
        L = 1
        for j in range(n):
            if i != j:
                L *= (xi - x[j]) / (x[i] - x[j])
        yi += y[i] * L

    return yi

x =[100, 200, 300, 400, 500]
y = [10, 12, 21, 23, 25]
x_interp = 350
interp_value =lagrange_interpolation(x, y, x_interp)
print(f"The interpolated value at x = {x_interp} is {interp_value}")