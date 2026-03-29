#include <stdio.h>

int first_position(int nums[], int size, int target) {
    int low = 0, high = size - 1, result = -1;
    while (low <= high) {
        int mid = (low + high) / 2;
        if (nums[mid] == target) {
            result = mid;
            high = mid - 1;
        } else if (nums[mid] > target) {
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }
    return result;
}

int last_position(int nums[], int size, int target) {
    int low = 0, high = size - 1, result = -1;
    while (low <= high) {
        int mid = (low + high) / 2;
        if (nums[mid] == target) {
            result = mid;
            low = mid + 1;
        } else if (nums[mid] < target) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    return result;
}

int main() {
    int nums[] = {1, 1, 2, 3, 4, 4, 6, 6, 6, 6, 7, 8, 8, 9};
    int size = sizeof(nums) / sizeof(nums[0]);
    int target = 6;

    int first_index = first_position(nums, size, target);
    int last_index  = last_position(nums, size, target);

    if (first_index != -1) {
        printf("The starting index of target %d is %d and last index is %d\n", target, first_index, last_index);
    } else {
        printf("Target %d not found!\n", target);
    }

    return 0;
}