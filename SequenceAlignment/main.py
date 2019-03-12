# Sarah Jorissen
# CSCI 4270
# Assignment 4

import numpy as np

matrix = []

seq1 = list(input("Enter the first sequence: "))
seq2 = list(input("Enter the second sequence: "))

m = len(seq2)
n = len(seq1)

# Builds the "optimal alignment" matrix in reverse-row order
for i in range(m+1):
    matrix.append(list(range((n + i)*2, -1 + 2*i, -2)))

# Corrects the row order :)
matrix = np.matrix(matrix[::-1])

for j in range(n-1, -1, -1):
    for i in range(m-1, -1, -1):
        # 	If the character at first at position i is equal to second at position j,
        # 	copy the value at i+1,j+1 into the matrix at position i,j.
        if seq1[j] == seq2[i]:
            matrix[i, j] = matrix[i+1, j+1]
        else:
            # Fetch the element below this position and add 2 to it.
            below = matrix[i-1, j] + 2
            # Fetch the element to the right of this position and add 2 to it.
            right = matrix[i, j+1] + 2
            # Fetch the element below AND to the right of this position and add 1 to it.
            diag = matrix[i-1, j+1] + 1
            # Find the smallest of the three fetched values. Write that value to the matrix at
            # position i,j.
            matrix[i, j] = min(below, right, diag)

print(f"Optimal alignment distance: {matrix[0, 0]}")