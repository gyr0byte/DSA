#include <stdio.h>
int count_rotation(int arr[],int arrSize){
    for(int i = 0; i < arrSize; i++){
        if(i > 0 && arr[i] < arr[i-1]){
            return i;
        }
    }
    return 0;
}
int main(){
    int arr[] = {4, 5, 6, 7, 1, 2, 3};
    int arrSize = sizeof(arr) / sizeof(arr[0]);
    int result = count_rotation(arr, arrSize);
    if(result != 0){
        printf("The array has been rotated %d times.", result );
    }
    else{
        printf("The array has not been rotated!");
    }
    return 0;
}