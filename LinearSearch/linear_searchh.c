#include <stdio.h> 
int locate_num(int arr[],int arraySize, int target){
    for(int i = 0; i < arraySize; i++){
        if (arr[i] == target){
            return i;
        }
    }
    return -1;
}
int main(){
    int arr[] = {13, 11, 12, 7, 4, 3, 1, 2};
    int target = 7;
    int arraySize = sizeof(arr) / sizeof(arr[0]);
    int result = locate_num(arr, arraySize, target);
    printf("The target was found at %d index", result);
    return 0;
}