#include<stdio.h>
#include "maxHeap.h"


// data is the array being heapify, 
// i is the current index
// n is the size of the data
void maxHeapify(int data[], int i, int n) 
{ 
    // current index largest 
	int largest = i;
	int left = (2 * i); 
	int right = 2 * i + 1; 

    // left child is largest 
	if (left < n && data[left] > data[largest]) 
		largest = left; 

    // right child is largest
	if (right < n && data[right] > data[largest]) 
		largest = right; 

    // largest isnt root 
	if (largest != i) { 
        // swap
		int temp = data[largest];
        data[largest] = data[i];
        data[i] = temp;
        // call min heapify again on the largest index 
		maxHeapify(data, largest, n); 
	} 
} 


// data is the data from which we are going to build heap
// n is the size of data 
void buildMaxHeap(int data[], int n) 
{ 

	for (int i = n / 2 - 1; i >= 0; i--){ 
		// calls min heapify on the parent nodes 
        //first half elements are parent nodes, 
        // second half elements are child nodes 
        maxHeapify(data, i, n);  
    }
} 


// data is the current heap/arry
// heapSize is the current number of elements in the heap
void printMaxHeap(int data[], int heapSize)
{
    printf("\n");
    for(int i = 0; i < heapSize; i++){
        printf("%d, ",data[i]);
    }
    printf("\n");
}


// heap is the current heap 
// heapSize is the current number of elements in the heap
int extractMax(int heap[], int n, int* heapSize)
{
    if(n < 0){
        // nothing in the heap
        return -1;
    }

    // first element will be the maximum
    int maxElement = heap[0];
    // replace first element with last element
    heap[0] = heap[*heapSize - 1];
    
    // decreasing heap size as element is extracted 
    *heapSize = *heapSize - 1;

    maxHeapify(heap ,0, n);    
    return maxElement;
}


// returns the first element as maximum element 
int peekMax(int heap[], int heapSize)
{
    if (heapSize < 0){

        return -1;
    }

    return heap[0];
}


// returns parent of the current index i 
int getParentMax(int i)
{
    return (i / 2) - 1;
}

// increases value of index of heap with a new value 
int increaseKey(int heap[], int index, int newValue)
{
    // new value must be greater than he current value
    if (newValue < heap[index]){
        // invalid value
        return -1;
    }
    
    heap[index] = newValue;
    // rearrainging the elements to hold max heap property 
    // sort data using insertion sort 
    while ((index  > 1) && (heap[getParentMax(index)] < heap[index])){
        int temp = heap[index];
        heap[index] = heap[getParentMax(index)];
        heap[getParentMax(index)] = temp;
        index = getParentMax(index);
    } 

    // increase value was success 
    return 1;
}

