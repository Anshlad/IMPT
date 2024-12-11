def matrix_chain_order(p):
    n = len(p) - 1  # Number of matrices
    # m[i][j] will hold the minimum number of multiplications needed to multiply matrices Ai...Aj
    m = [[0] * n for _ in range(n)]
    
    # l is the chain length
    for l in range(2, n + 1):  # l = 2 to n
        for i in range(n - l + 1):
            j = i + l - 1
            m[i][j] = float('inf')  # Set to infinity initially
            for k in range(i, j):
                # Cost of multiplying A[i..k] and A[k+1..j]
                q = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                if q < m[i][j]:
                    m[i][j] = q

    return m[0][n - 1]  # Minimum cost for multiplying A1...An

# Example usage
if __name__ == "__main__":
    # Dimensions of matrices A1, A2, A3, ..., An
    # For example, if A1 is 10x20, A2 is 20x30, A3 is 30x40, then p = [10, 20, 30, 40]
    dimensions = [10, 20, 25, 20]  # This represents 3 matrices: A1(10x20), A2(20x30), A3(30x40)
    
    result = matrix_chain_order(dimensions)
    print(f"Minimum number of multiplications required: {result}")