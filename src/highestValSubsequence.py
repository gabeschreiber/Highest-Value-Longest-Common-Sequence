def highestVal(A, B, alphabet):
    a, b = len(A), len(B)

    # build solution 2D array M
    m = [[0] * (b + 1 ) for _ in range(a + 1)]

    for i in range(1, a + 1):
        for j in range(1, b + 1):
            if A[i-1] != B[j-1]:
                m[i][j] = max(m[i-1][j], m[i][j-1])
            elif A[i-1] == B[j-1]:
                m[i][j] = max(alphabet[A[i-1]] + m[i-1][j-1], m[i-1][j], m[i][j-1])

    return m
