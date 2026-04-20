def max_profit_dp(weights, profit, capacity):
    n = len(weights)
    table = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    for i in range(n):
        for c in range(1, capacity + 1):
            if weights[i] > c:
                table[i+1][c] = table[i][c]
            else:
                table[i+1][c] = max(table[i][c], profit[i] + table[i][c-weights[i]])
    return table[-1][-1]