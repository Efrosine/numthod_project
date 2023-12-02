import matplotlib.pyplot as plt

def f(x):
    return 500 - x**3 + 8 * x

def f_prime(x):
    return -3 * x**2 + 8

def newton_raphson(func,func_p,guess, tol=0.001, max_iter=100):
    x = guess
    relative_errors = []  
    for _ in range(max_iter):
        fx = func(x)
        if abs(fx) < tol:
            return x, relative_errors
        fpx = func_p(x)
        if fpx == 0:
            break
        x = x - fx / fpx
        relative_error = abs((x - guess) / guess)  
        relative_errors.append(relative_error)
    return None, relative_errors


root, relative_errors = newton_raphson(f,f_prime,1)
if root is not None:
    print("Root found:", root)
    plt.plot(range(1, len(relative_errors) + 1), relative_errors)
    plt.xlabel("Iteration")
    plt.ylabel("Relative Error")
    plt.title("Relative Error vs. Iteration")
    plt.show()
else:
    print("Root not found within the maximum number of iterations.")
