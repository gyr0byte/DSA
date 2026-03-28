def first_position(nums, target):
    low, high = 0, len(nums) - 1 
    result = -1
    while low <= high:
        mid = ( low + high ) // 2

        if nums[mid] == target:
            result = mid
            high = mid - 1
        elif nums[mid] > target:
            high = mid - 1
        elif nums[mid] < target:
            low = mid + 1
            
    return result

def last_position(nums, target):
    low, high = 0, len(nums) - 1
    result = -1
    while low <= high:
        mid = ( low + high ) // 2
        if nums[mid] == target:
            result = mid
            low = mid + 1
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return result
nums = [1, 1, 2, 3, 4, 4, 6, 6, 6, 6, 7, 8, 8, 9]
target = 6
first_index = first_position(nums, target)
last_index = last_position(nums, target)
if first_index != -1:
    print(f"The starting index of target {target} is {first_index} and last index is {last_index}")
else:
    print(f"Target {target} not found!")