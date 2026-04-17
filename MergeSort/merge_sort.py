def merge(nums1, nums2):
    merged = []

    i,j = 0,0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1
            

    return merged + nums[i:] + nums[j:]
    
def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    
    mid = len(nums) // 2
    
    left = nums[:mid]
    right = nums[mid:]

    left_sorted, right_sorted = merge_sort(left), merge_sort(right)

    sorted_nums = merge(left_sorted, right_sorted)

    return sorted_nums

nums = [7, 3, 2, 4, 1, 4, 7, 8, 2, 4, 3, 9, 6]
print(merge_sort(nums))