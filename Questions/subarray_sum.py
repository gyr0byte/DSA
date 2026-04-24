def subarray_sum(arr, target):
    j = 0
    for i in range(len(arr)):
        s = 0
        if sum(arr[j:i]) > target:
            j += 1
        elif sum(arr[j:i]) == target:
            return j, i
    return 0


arr = [1, 7, 4, 2, 1, 3, 11, 5]
target = 10
print(subarray_sum(arr, target))
