#include<stdio.h>
#include "minHeap.h"
#include "maxHeap.h"


void maxHeap(int data[]);
void minHeap(int data[]);
void copy(int a[], int b[], int n);

int main()
{
    printf("Program to demostrate working of Binary Heap\n"); 
    int data[] = {95, 55, 42, 34, 68, 34, 2, 99, 24, 68, 68, 79, 84, 25, 2, 45, 76, 31 , 16 , 79};
    
    printf("\n");
    maxHeap(data);
    minHeap(data);
    
    return 0;
}


void maxHeap(int data[])
{
    printf("Implementation of Max Heap\n");
    int arr[20];

    int n = sizeof(arr)/(sizeof(arr[0]));
    int heapSize = n;

    // copy data into array 
    copy(data, arr, n);

    printf("Original Array:");
    printMaxHeap(arr, heapSize);

    // build max heap using buildMaxHeap function
    buildMaxHeap(arr, n);
    printf("Max Heap:");
    
    printMaxHeap(arr, heapSize);
    printf("PeekMax: %d\n",peekMax(arr, heapSize));
    
    printf("Extract Max: %d\n",extractMax(arr, n, &heapSize));
    printf("Array After Extracting Maximum:\n");
    
    printf("HeapSize: %d", heapSize);
    printMaxHeap(arr, heapSize);
    printf("\n");
}

void minHeap(int data[])
{
    printf("Implementation of Min Heap\n");
    int arr[20];

    int n = sizeof(arr)/(sizeof(arr[0]));
    int heapSize = n;

    // copy data into array 
    copy(data, arr, n);

    printf("Original Array:");
    printMinHeap(arr, heapSize);

    // build max heap using buildMinHeap function
    buildMinHeap(arr, n);
    printf("Min Heap:");
    
    printMinHeap(arr, heapSize);
    printf("PeekMin: %d\n",peekMin(arr, heapSize));
    
    printf("Extract Min: %d\n",extractMin(arr, n, &heapSize));
    printf("Array After Extracting Minimum:\n");
    
    printf("HeapSize: %d", heapSize);
    printMinHeap(arr, heapSize);
    printf("\n");
}


void copy(int a[], int b[], int n)
{
    // number of elements must be same for both arrays 
    for (int i=0;i< n;i++){
        b[i] = a[i];
    }
}