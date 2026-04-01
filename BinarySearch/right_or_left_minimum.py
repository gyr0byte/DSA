def locate_num(nums):
    low, high = 0, len(nums) - 1 
    while low <= high:
        mid = ( low + high ) // 2

        if nums[mid] > nums[len(nums) - 1]:
            return 1
        elif nums[mid] < nums[len(nums) - 1]:
            return 2
            
    return -1

nums = [4, 7, 9, 11, 13, 1, 2, 3]
result = locate_num(nums)
if result == 1:
    print("The minimum value is located at Right of the list!")
elif result == 2:
    print("The minimum value is located at left of the list!")