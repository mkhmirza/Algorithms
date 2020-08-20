package main

import "fmt"

func bucketSort(array [5]float64) []float64 {
	
	bucketSize := 5
	var max, min float64
	for _, n := range array {
		if n < min {
			min = n
		}

		if n > max {
			max = n
		}
	}

	nBuckets := int(max-min)/bucketSize + 1
	buckets := make([][]float64, nBuckets)
	
	// create new buckets inside the main bucket 
	for i := 0; i < nBuckets; i++ {
		buckets[i] = make([]float64, 0)
	}

	// append the elements from array into buckets
	for _, n := range array {
		idx := int(n-min) / bucketSize
		buckets[idx] = append(buckets[idx], n)
	}

	sorted := make([]float64, 0)

	// sort each bucket using insertion sort 
	for _, bucket := range buckets {
		if len(bucket) > 0 {
			insertionSort(bucket)
			sorted = append(sorted, bucket...)
		}
	}
	
	return sorted
}

// sorts data array using insertion sort n ascending order 
func insertionSort(array []float64) []float64 {
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

func main(){

	a := [5]float64{0.897, 0.565, 0.656, 0.1234, 0.665}
	
	sorted := bucketSort(a)
	
	fmt.Println("Original Array: ")
	fmt.Println(a)
	
	fmt.Println("Sorted Array Acending Order: ")
	fmt.Println(sorted)
	
	
}
