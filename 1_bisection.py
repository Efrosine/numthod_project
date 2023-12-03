import matplotlib.pyplot as plt
from prettytable import PrettyTable

def f(x):
    return 500 - x**3 + 8 * x

table = PrettyTable(['n','x1','f(x1)','x2','f(x2)','x3','f(x3)','relative_error'])

def bisection(func, x1, x2, tol=0.01, max_iter=100):
    
    if func(x1) * func(x2) >= 0:
        raise ValueError("The function must have opposite signs.")

    x3 = x1
    iter_count = 0
    relative_errors = []

    while (x2 - x1) >= tol and iter_count < max_iter:
        x3 = (x1 + x2) / 2

        relative_error = abs((x2 - x1) / x3)
        relative_errors.append(relative_error) 
        
        table.add_row([iter_count,x1,f(x1),x2,f(x2),x3,f(x3),relative_error])

        if func(x3) == 0:
            break

        if func(x3) * func(x1) < 0:
            x2 = x3
        else:
            x1 = x3

        iter_count += 1

    return x3, relative_errors



root,relative_errors  = bisection(f, 0, 10)
print(table)
print("Root found:", root)
plt.plot(range(1, len(relative_errors) + 1), relative_errors)
plt.xlabel("Iteration")
plt.ylabel("Relative Error")
plt.title("Relative Error vs. Iteration")
plt.show()

