#include<stdio.h>
#include "maxHeap.h"

// program to demostrate working of max heap 


int main()
{
    printf("Program to demostrate working of max heap\n");
    int data[] = {95, 55, 42, 34, 68, 34, 2, 99, 24, 68, 68, 79, 84, 25, 2, 45, 76, 31 , 16 , 79};

    int n = sizeof(data)/(sizeof(data[0]));
    int heapSize = n;

    // build max heap 
    buildMaxHeap(data, n);

    // printing heap 
    printMaxHeap(data, heapSize);
    
    // peek maximum 
    printf("PeekMax: %d\n",peekMax(data, heapSize));

    // extract max element 
    int maxElement = extractMax(data, n, &heapSize);
    printf("MaxElement: %d\n",maxElement);

    // printing after extracting max element 
    printMaxHeap(data, heapSize);


    return 0;
}