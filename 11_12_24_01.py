def matrix_chain_order(p):
    n = len(p) - 1  
   
    m = [[0] * n for _ in range(n)]
    
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                if q < m[i][j]:
                    m[i][j] = q

    return m[0][n - 1]

if __name__ == "__main__":
    dimensions = [10, 20, 25, 20]
    
    result = matrix_chain_order(dimensions)
    print(f"Minimum number of multiplications required: {result}")