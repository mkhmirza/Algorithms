#!/usr/python env

# program to demostrate bubble sort algorithm

def bubbleSortAscending(data: list):
    "Bubble Sort Algorithm to sort data into Ascending Order"
    for i in range(0, len(data)):
        for j in range(0, len(data)):
            if data[i] < data[j]:
                data[i], data[j] = data[j], data[i]
    
def bubbleSortDescending(data: list):
    "Bubble Sort Algorithm to sort data into Descending Order"
    for i in range(0, len(data)):
        for j in range(0, len(data)):
            if data[i] > data[j]:
                data[i], data[j] = data[j], data[i]    

def printSortedData(data: list):
    for i in range(0, len(data)):
        print(f"{data[i]}, ",end=' ')
    print()

# unsorted data
a = [1 , 2, 4, 5, 6, 0, 2]

print("1. Sort Data into Ascending Order")
print("2. Sort Data into Descending Order")
choice = int(input("Enter Your Choice: "))

if choice == 1:
    print("Sorting Data into Ascending Order.")
    bubbleSortAscending(a)
elif choice == 2:
    print("Sorting Data into Descending Order.")
    bubbleSortDescending(a)
else:
    print("Invalid Choice!")
    
printSortedData(a)
