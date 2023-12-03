import numpy as np

def gauss_jordan(A, B):
    augmented_matrix = np.column_stack((A, B))

    n = len(A)
    for i in range(n):
        pivot_row = i
        for j in range(i+1, n):
            if abs(augmented_matrix[j, i]) > abs(augmented_matrix[pivot_row, i]):
                pivot_row = j

        augmented_matrix[[i, pivot_row]] = augmented_matrix[[pivot_row, i]]
        pivot = augmented_matrix[i, i]
        augmented_matrix[i] = augmented_matrix[i] / pivot

        for j in range(n):
            if j != i:
                factor = augmented_matrix[j, i]
                augmented_matrix[j] -= factor * augmented_matrix[i]

    solution = augmented_matrix[:, -1]

    return solution


A = np.array([[9,1, 1], [1,9,1],[1,1,9]])
B = np.array([11,11,11])
solution = gauss_jordan(A, B)
print('gaus_jordan ',solution)
