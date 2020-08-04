#include<stdio.h>
#include "minHeap.h"

void createGraph(int graph[3][3],int i, int j, int weight);
void printMatrix(int graph[3][3]);
void getNeighbors(Node neighbors[], int numberOfNeighbors, int graph[3][3], int v);


int main()
{
    int graph[3][3];
    for(int i = 0; i < 3; i++){
        for(int j=0; j < 3; j++){
            graph[i][j] = 0;
        }
    }
    
    createGraph(graph, 0, 1, 50);
    createGraph(graph, 0, 2, 30);
    createGraph(graph, 1, 2, 70);

    printMatrix(graph);

    struct Node node[3];
    for (int i =0;i < 3;i++){
        node[i].distance = __INT32_MAX__;
        node[i].prev = 0;
        node[i].label = i;
    }

    node[0].distance = 0;
    node[0].prev = 0;

    struct Node queue[] = {node[0]};
    int n = sizeof(queue)/sizeof(queue[0]); 
    int heapSize = n;
    
    Node minNode; 
    Node neighbors[3];

    int numberOfNeighbors = 0;
    
    for(int i=0;i<3;i++){
        neighbors[i].label = 0;
    }
    
    
    while(queue){
        minNode = extractMin(queue, n, &heapSize);
        printf("MinNode: %d\n",minNode.label);
        n = sizeof(queue)/sizeof(queue[0]);
        
        
        for(int i=0;i<n;i++){
            //printf("Queue: %d\n",queue[i].label);
        }

        for (int i=0;i<3;i++){
            if (graph[minNode.label][i] > 0){
                numberOfNeighbors++;
            }
        }    

        getNeighbors(neighbors, numberOfNeighbors ,graph, minNode.label);
        for(int  i = numberOfNeighbors - 1; i <= numberOfNeighbors ; i++){
            if (neighbors[i].distance > neighbors[minNode.label].distance + graph[minNode.label][i]){
                neighbors[i].distance = neighbors[minNode.label].distance + graph[minNode.label][i];
                neighbors[i].prev = minNode.label;
                queue[i] = neighbors[i];
            }
        }
    }

    return 0;
}


void createGraph(int graph[3][3],int i, int j, int weight)
{
    graph[i-1][j-1] = weight;
    graph[j-1][i-1] = weight;
}

void printMatrix(int graph[3][3])
{
    for(int i = 0; i < 3; i++){
        for(int j=0; j < 3; j++){
            printf("%d ",graph[i][j]);
        }
        printf("\n");
    }

    printf("\n");
}

void getNeighbors(Node neighbors[], int numberOfNeighbors, int graph[3][3], int v)
{
    for(int i = numberOfNeighbors - 1 ; i <= numberOfNeighbors; i++){
        if(graph[v][i] > 0){
            neighbors[i].label = i;
            //printf("%d\n",i);
        }
    }
}


