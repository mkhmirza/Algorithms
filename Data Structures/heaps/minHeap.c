#include<stdio.h>
#include "minHeap.h"

// data is the array being heapify, 
// i is the current index
// n is the size of the data
void minHeapify(int data[], int i, int n) 
{ 
    // current index smallest 
	int smallest = i;
	int left = (2 * i); 
	int right = 2 * i + 1; 

    // left child is smallest 
	if (left < n && data[left] < data[smallest]) 
		smallest = left; 

    // right child is smallest
	if (right < n && data[right] < data[smallest]) 
		smallest = right; 

    // smallest isnt root 
	if (smallest != i) { 
        // swap
		int temp = data[smallest];
        data[smallest] = data[i];
        data[i] = temp;
        // call min heapify again on the smallest index 
		minHeapify(data, smallest, n); 
	} 
} 


// data is the data from which we are going to build heap
// n is the size of data 
void buildHeap(int data[], int n) 
{ 

	for (int i = n / 2 - 1; i >= 0; i--){ 
		// calls min heapify on the parent nodes 
        //first half elements are parent nodes, 
        // second half elements are child nodes 
        minHeapify(data, i, n);  
    }
} 


// data is the current heap/arry
// heapSize is the current number of elements in the heap
void printHeap(int data[], int heapSize)
{
    printf("\n");
    for(int i = 0; i < heapSize; i++){
        printf("%d, ",data[i]);
    }
    printf("\n");
}


// heap is the current heap 
// heapSize is the current number of elements in the heap
int extractMin(int heap[], int n, int* heapSize)
{
    if(n < 0){
        // nothing in the heap
        return -1;
    }

    // first element will be the minimum
    int minElement = heap[0];
    // replace first element with last element
    heap[0] = heap[n - 1];
    
    // decreasing heap size as element is extracted 
    *heapSize = *heapSize - 1;

    minHeapify(heap ,0, n);    
    return minElement;
}

// returns the first element as minimum element 
int peek(int heap[], int heapSize)
{
    if (heapSize < 0){
        return -1;
    }

    return heap[0];
}



