package main

import "fmt"

func selectionSort(array []int) []int{

	for i:=0; i < len(array); i++{
		minElement := i

		for j:=0; j < len(array); j++{
			if array[j] > array[minElement]{
				minElement = j
			}
		}

		if minElement != i{
			array[i], array[minElement] = array[minElement], array[i]
		}
	}
	return array
}

func main(){
	fmt.Println("Program demostration for working of selection sort")
	array := []int {64, 11, 22, 25, 64, 12}
	fmt.Println("Original Array: ")
	fmt.Println(array)
	sortedArray := selectionSort(array)
	
	fmt.Println("Sorted Array: ")
	fmt.Println(sortedArray)
}