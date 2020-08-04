#include <stdio.h>
#include "../heaps/maxHeap.h"

void heapSort(int data[], int n);

int main()
{
    int data[] = {9, 37, 32, 73, 59, 49, 75, 97 , 68, 74, 56, 76, 100, 6, 32, 67, 38, 58, 21, 83};
    printf("Program to demostrate Ascending Order Sort using Max Heap");
    
    int n = sizeof(data)/sizeof(data[0]);
    heapSort(data, n);

    return 0;
}


void heapSort(int data[], int n)
{
    printf("Original Data: ");
    printMaxHeap(data, n);
    buildMaxHeap(data, n);
    
    for(int i = n - 1; i>=0 ; i--){
        int temp = data[0];
        data[0] = data[i];
        data[i] = temp;
        maxHeapify(data, 0, i);
    }

    // pritintg sorted data using print max heap
    printf("Sorted Data: ");
    printMaxHeap(data, n);
}