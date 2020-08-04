#include<stdio.h>
#include "minHeap.h"


int main()
{
    //int data[] = {2,7,26,25,19,17,1,90,3,36};
    int data[] = {3,5,8,0};

    int n = sizeof(data)/sizeof(data[0]);    
    int heapSize = n;
    
    buildHeap(data, n);
    printHeap(data, n);

    int minElement = extractMin(data, n, &heapSize);
    printf("MinElement: %d\n",minElement);
    printf("Current HeapSize: %d\n",heapSize);

    printHeap(data, heapSize);

    printf("Peek: %d\n",peek(data, heapSize));

    return 0;
}