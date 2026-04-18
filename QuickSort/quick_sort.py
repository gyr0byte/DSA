def partition(nums, start = 0, end = None):
    if end is None:
        end = len(nums) - 1
    l, r = start, end - 1
    while l <= r:
        if nums[l] <= nums[end]:
            l += 1
        elif nums[r] > nums[end]:
            r -= 1
        else:
            nums[l], nums[r] = nums[r], nums[l]

    nums[l], nums[end] = nums[end], nums[l]
    return l 

def quick_sort(nums, start = 0, end = None):
    if end is None:
        end = len(nums) - 1
    if start < end:
        pivot = partition(nums, start, end)
        quick_sort(nums, start, pivot-1)
        quick_sort(nums, pivot+1, end)

    return nums

nums = [3, 2, 4, 5, 2, 4, 5, 8, 5, 3, 1, 0, 3, 7, 9, 2, 5, 4, 12, 4, 3, 1, 0, 3, 4, 15, 12, 6]
print(quick_sort(nums))