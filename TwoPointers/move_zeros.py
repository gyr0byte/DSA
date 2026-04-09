def move_zero(nums):
    left = 0
    for right in range(len(nums)):
        if (nums[right] != 0):
            temp = nums[left]
            nums[left] = nums[right]
            nums[right] = temp
            left += 1
    print(nums)

nums = [12, 0, 4, 5, 0, 8]
move_zero(nums)