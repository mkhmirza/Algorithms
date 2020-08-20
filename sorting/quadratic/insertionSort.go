package main

import "fmt"

// sorts data array using insertion sort n ascending order 
func insertionSortAcending(array [10]int) [10]int {
	var i int = 0 // counter 
	for i < len(array){
		j := i
		for j > 0 {
			if array[j] < array[j - 1]{
				// swap values 
				array[j], array[j-1] = array[j-1], array[j]
			}
			j--
		}
		i++
	}

	return array
}

func insertionSortDescending(array [10]int) []int {
	var i int = 0 // counter 
	for i < len(array){
		j := i
		for j > 0 {
			if array[j] > array[j - 1]{
				// swap values 
				array[j], array[j-1] = array[j-1], array[j]
			}
			j--
		}
		i++
	}

	return array[:10]
}

func main(){

	fmt.Println("Program to demostrate working of insertion sort")
	array := [10]int{1, 4, 5, 0, 99, 67, 1, 100, 2, 8}
	sortedArrayAscending := insertionSortAcending(array)
	
	fmt.Println("Original Array: ")
	fmt.Println(array)
	fmt.Println("Sorted Array Acending Order: ")
	fmt.Println(sortedArrayAscending)
	
	fmt.Println()

	sortedArrayDescending := insertionSortDescending(array)
	fmt.Println("Original Array: ")
	fmt.Println(array)
	fmt.Println("Sorted Array Descending Order: ")
	fmt.Println(sortedArrayDescending)
}