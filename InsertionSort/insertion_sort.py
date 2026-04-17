def insertion_sort(nums):
    for i in range(len(nums)):
        cur = nums.pop(i)
        j = i - 1
        while j >= 0 and nums[j] > cur:
            j -= 1
        nums.insert(j + 1, cur)
    return nums

nums = [5, 7, 2, 1, 6, 8, 3, 4]
print(insertion_sort(nums))
