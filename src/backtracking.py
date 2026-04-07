def backtrack(A, B, alphabet, m):
    i, j = len(A), len(B)
    result = []

    while i > 0 and j > 0:
        if A[i-1] == B[j-1] and m[i][j] == m[i][j-1] + alphabet[A[i-1]]:
            result.append(A[i-1])
            i -= 1
            j -= 1
        elif m[i-1][j] >= m[i][j-1]:
            i -= 1
        else:
            j -= 1

    return ''.join(reversed(result))