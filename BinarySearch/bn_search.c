#include <stdio.h>

int locate_num(int nums[], int arraySize, int target){
    int low = 0, high = arraySize - 1;
    while (low <= high){
        int mid = (low + high) / 2;

        if (nums[mid] == target){
            return mid;
        }
        else if (nums[mid] > target){
            high = mid - 1;
        }
        else{
            low = mid + 1;
        }
    }
    return -1;
}

int main(){
    int nums[] = {1, 2, 3, 4, 7, 9, 11, 13};
    int target = 9;
    int arraySize = sizeof(nums) / sizeof(nums[0]);
    int result = locate_num(nums, arraySize, target);
    printf("The target %d was found at index: %d", target, result);
    return 0;
}