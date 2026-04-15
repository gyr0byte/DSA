def bubble_sort(nums):
    for j in range(len(nums) - 1):
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]

    return nums

nums = [5, 7, 2, 1, 6, 8, 3, 4]
print(bubble_sort(nums))