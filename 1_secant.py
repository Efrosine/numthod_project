import matplotlib.pyplot as plt

def f(x):
    return 500 - x**3 + 8 * x

def secant_method(func, x1, x2, tol=0.001, max_iter=100):
    x_prev = x1
    x_curr = x2
    iteration = 0
    relative_errors = []

    while abs(func(x_curr)) > tol and iteration < max_iter:        
        x_next = x_curr - (func(x_curr) * (x_curr - x_prev)) / (func(x_curr) - func(x_prev))
        
        relative_error = abs((x_next - x_curr) / x_next)
        relative_errors.append(relative_error)

        x_prev = x_curr
        x_curr = x_next
        iteration += 1

    return x_curr, relative_errors

root,relative_errors  = secant_method(f, 1, 2)
print("Root found:", root)
plt.plot(range(1, len(relative_errors) + 1), relative_errors)
plt.xlabel("Iteration")
plt.ylabel("Relative Error")
plt.title("Relative Error vs. Iteration")
plt.show()

