def count_rotation_linear(nums):
    for i in range(len(nums)):
        if i > 0 and nums[i] < nums[i - 1]:
            return i
        
    return 0 

nums = [4, 5, 6, 7, 1, 2, 3]
result = count_rotation_linear(nums)
if result > 0:
    print(f"The list has been rotated {result} times!")
else:
    print(f"The list has not been rotated!")