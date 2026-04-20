def max_profit_recursive(weights, profits, capacity, idx=0):
    if idx == len(weights):
        return 0
    elif weights[idx] > capacity:
        return max_profit_recursive(weights, profits, capacity, idx+1)
    else:
        option1 = max_profit_recursive(weights, profits, capacity, idx+1)
        option2 = profits[idx] + max_profit_recursive(weights, profits, capacity - weights[idx], idx + 1)
        return max(option1, option2)

print(max_profit_recursive([1, 2, 3], [10, 15, 40], 6))
print(max_profit_recursive([1, 2, 3], [10, 15, 40], 5))
print(max_profit_recursive([1, 2, 3], [10, 15, 40], 3))