def lcs(X, Y):
    m = len(X)
    n = len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    lcs_length = dp[m][n]
    lcs_string = []
    i, j = m, n

    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs_string.append(X[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    lcs_string.reverse()
    return ''.join(lcs_string), lcs_length

maryam = input()
n = int(input())
best_lcs = ""
best_length = 0

for _ in range(n):
    candidate = input()
    lcs_string, lcs_length = lcs(maryam, candidate)
    if lcs_length > best_length:
        best_lcs = lcs_string
        best_length = lcs_length

print(best_lcs)
print(best_length)
