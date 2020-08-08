#include <stdio.h>
#include "../heaps/maxHeap.h"
#include "../heaps/minHeap.h"

void heapSortAscending(int data[], int n);
void heapSortDescending(int data[], int n);

int main()
{
    int data[] = {9, 37, 32, 73, 59, 49, 75, 97 , 68, 74, 56, 76, 100, 6, 32, 67, 38, 58, 21, 83};
    printf("1. Sort Data Ascending Order\n");
    printf("2. Sort Data Descending Order\n");
    int choice; 
    printf("\n");
    scanf("%d",&choice);

    int n = sizeof(data)/sizeof(data[0]);
        
    switch(choice){
        case 1:
            printf("Program to demostrate Ascending Order Sort using Max Heap");    
            heapSortAscending(data, n);
            break;
        case 2: 
            printf("Program to demostrate Descending Order Sort using Max Heap");    
            heapSortDescending(data, n);
            break;
        default:
            printf("Invalid");
    }

    return 0;
}


void heapSortAscending(int data[], int n)
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

void heapSortDescending(int data[], int n)
{
    printf("Original Data: ");
    printMinHeap(data, n);
    buildMinHeap(data, n);
    
    for(int i = n - 1; i>=0 ; i--){
        int temp = data[0];
        data[0] = data[i];
        data[i] = temp;
        minHeapify(data, 0, i);
    }

    // printing sorted data using print min heap
    printf("Sorted Data: ");
    printMinHeap(data, n);   
}
