import numpy as np

A = np.array([[9, 1, 1], [1, 9, 1], [1, 1, 9]])
B = np.array([11, 11, 11])

def lu_decomposition(A):
    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    for i in range(n):
   
        for k in range(i, n):
            sum = 0
            for j in range(i):
                sum += (L[i][j] * U[j][k])
            U[i][k] = A[i][k] - sum

       
        for k in range(i, n):
            if i == k:
                L[i][i] = 1
            else:
                sum = 0
                for j in range(i):
                    sum += (L[k][j] * U[j][i])
                L[k][i] = (A[k][i] - sum) / U[i][i]

    return L, U

def lu_solve(L, U, B):
    n = len(B)
    Y = np.zeros(n)
    X = np.zeros(n)

    for i in range(n):
        sum = 0
        for j in range(i):
            sum += L[i][j] * Y[j]
        Y[i] = B[i] - sum


    for i in range(n-1, -1, -1):
        sum = 0
        for j in range(i+1, n):
            sum += U[i][j] * X[j]
        X[i] = (Y[i] - sum) / U[i][i]

    return X

A = np.array([[9, 1, 1], [1, 9, 1], [1, 1, 9]])
B = np.array([11, 11, 11])


L, U = lu_decomposition(A)


solution = lu_solve(L, U, B)

print("lu_decomposition ", solution)
