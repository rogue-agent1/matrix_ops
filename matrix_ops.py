#!/usr/bin/env python3
"""matrix_ops — Matrix operations (multiply, transpose, determinant, inverse). Zero deps."""

def zeros(r, c): return [[0]*c for _ in range(r)]
def identity(n): return [[1 if i==j else 0 for j in range(n)] for i in range(n)]

def transpose(A):
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]

def multiply(A, B):
    ra, ca, cb = len(A), len(A[0]), len(B[0])
    C = zeros(ra, cb)
    for i in range(ra):
        for k in range(ca):
            for j in range(cb):
                C[i][j] += A[i][k] * B[k][j]
    return C

def determinant(A):
    n = len(A)
    if n == 1: return A[0][0]
    if n == 2: return A[0][0]*A[1][1] - A[0][1]*A[1][0]
    det = 0
    for j in range(n):
        minor = [row[:j]+row[j+1:] for row in A[1:]]
        det += ((-1)**j) * A[0][j] * determinant(minor)
    return det

def inverse(A):
    n = len(A)
    aug = [row[:] + identity(n)[i] for i, row in enumerate(A)]
    for col in range(n):
        pivot = max(range(col, n), key=lambda r: abs(aug[r][col]))
        aug[col], aug[pivot] = aug[pivot], aug[col]
        if abs(aug[col][col]) < 1e-12:
            raise ValueError("Singular matrix")
        scale = aug[col][col]
        aug[col] = [x/scale for x in aug[col]]
        for row in range(n):
            if row != col:
                factor = aug[row][col]
                aug[row] = [aug[row][j] - factor*aug[col][j] for j in range(2*n)]
    return [row[n:] for row in aug]

def fmt(M):
    return "\n".join("  [" + ", ".join(f"{x:>8.3f}" for x in row) + "]" for row in M)

def main():
    A = [[1,2,3],[4,5,6],[7,8,10]]
    print(f"A:\n{fmt(A)}")
    print(f"\ndet(A) = {determinant(A):.3f}")
    inv = inverse(A)
    print(f"\nA⁻¹:\n{fmt(inv)}")
    prod = multiply(A, inv)
    print(f"\nA × A⁻¹ (should be I):\n{fmt(prod)}")

if __name__ == "__main__":
    main()
