

typedef struct Node
{
    int distance;
    int prev;
    int label;
} Node;


void buildHeap(struct Node data[], int size);
void minHeapify(struct Node data[], int i, int n);
void printHeap(struct Node data[], int heapSize);
int peek(int heap[], int heapSize);
Node extractMin(struct Node heap[], int n, int* heapSize);
