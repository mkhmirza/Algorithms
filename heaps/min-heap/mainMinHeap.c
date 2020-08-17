#include<stdio.h>
#include "../header/minHeap.h"

// program to demostrate working of Min heap 


int main()
{
    printf("Program to demostrate working of Min heap\n");
    int data[] = {95, 55, 42, 34, 68, 34, 2, 99, 24, 68, 68, 79, 84, 25, 2, 45, 76, 31 , 16 , 79};

    int n = sizeof(data)/(sizeof(data[0]));
    int heapSize = n;

    // build min heap 
    buildMinHeap(data, n);

    // printing heap 
    printMinHeap(data, heapSize);
    
    // peek Minimum 
    printf("PeekMin: %d\n",peekMin(data, heapSize));

    // extract min element 
    int minElement = extractMin(data, n, &heapSize);
    printf("MinElement: %d\n",minElement);

    // printing after extracting Min element 
    printMinHeap(data, heapSize);


    return 0;
}