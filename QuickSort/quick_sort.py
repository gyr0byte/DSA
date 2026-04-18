def quick_sort(nums, start = 0, end = None):
    if end is None:
        end = len(nums) - 1
    if start < end:
        pivot = partition(nums, start, end)
        quick_sort(nums, start, pivot-1)
        quick_sort(nums, pivot+1, end)

    return nums