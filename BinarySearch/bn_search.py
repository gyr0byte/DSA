def locate_num(nums, target):
    low, high = 0, len(nums) - 1 
    while low <= high:
        mid = ( low + high ) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            high = mid - 1
        elif nums[mid] < target:
            low = mid + 1
            
    return -1

nums = [1, 2, 3, 4, 7, 9, 11, 13]
target = 9
result = locate_num(nums, target)
print(f"The target {target} was found at index {result}")