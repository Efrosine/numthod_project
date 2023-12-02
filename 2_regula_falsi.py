import matplotlib.pyplot as plt
def v(t):
    return 50 + 8 * t - 5 * t**2

def false_position(func,x1, x2, tol=0.001, max_iter=100):
    relative_errors = []
    if func(x1) * func(x2) >= 0:
        raise ValueError("The function values must have opposite signs.")
    
    for i in range(max_iter):
        x3 = (x1 * func(x2) - x2 * func(x1)) / (func(x2) - func(x1))
        
        relative_error = abs((x3 - x1) / x3)
        relative_errors.append(relative_error)
        
        if abs(func(x3)) < tol:
            return x3,relative_errors
        
        if func(x1) * func(x3) < 0:
            x2 = x3
        else:
            x1 = x3
    
    raise ValueError("The method did not converge within the maximum number of iterations.")


root,relative_errors = false_position(v,0,10)
print("Root found:", root)
plt.plot(range(1, len(relative_errors) + 1), relative_errors)
plt.xlabel("Iteration")
plt.ylabel("Relative Error")
plt.title("Relative Error vs. Iteration")
plt.show()

