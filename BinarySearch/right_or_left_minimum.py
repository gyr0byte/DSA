def locate_num(nums):
    low, high = 0, len(nums) - 1 
    while low < high:
        mid = ( low + high ) // 2

        if nums[mid] > nums[high]:
            low = mid + 1
        else:
            high = mid

    return low

nums = [4, 7, 9, 11, 13, 1, 2, 3]
result = locate_num(nums)
print(f"The minimum value {nums[result]} is at index {result}")