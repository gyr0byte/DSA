def bubble_sort(nums):
    for i in range(len(range)-1):
        if nums[i] > nums[i+1]:
            nums[i], nums[i+1] = nums[i+1], nums[i]
            
    return nums