void buildMinHeap(int data[], int size);
void minHeapify(int data[], int i, int n);
void printMinHeap(int data[], int heapSize);
int peekMin(int heap[], int heapSize);
int extractMin(int heap[], int n, int* heapSize);
int getParentMin(int i);
int decreaseKey(int heap[], int index, int newValue);
