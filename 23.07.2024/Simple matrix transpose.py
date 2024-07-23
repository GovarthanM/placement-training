matrix = [[1, 2, 3], [4, 5, 6]]
transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]

print("Transposed matrix 1:")
for row in transposed:
    print(row)

print("\nOriginal matrix 1:")
for row in matrix:
    print(row)

matrix_2 = [[7, 8], [9, 10], [11, 12]]
transposed_2 = [[row[i] for row in matrix_2] for i in range(len(matrix_2[0]))]
print("\nTransposed matrix 2:")
for row in transposed_2:
    print(row)

print("\nOriginal matrix 2:")
for row in matrix_2:
    print(row)
