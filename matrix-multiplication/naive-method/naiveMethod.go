package main
import (
    "fmt"
    "math/rand"
	"time"
)

func naiveMultiplication(m1 ,  m2[3][3]int) [3][3]int {
	c := [3][3]int{}
	
	for i:=0; i < len(m1); i++{
		for j:=0; j < len(m1); j++{
			c[i][j] = 0
			for k := 0; k < len(m1); k++{ 
                c[i][j] += m1[i][k] *  m1[k][j]; 
			}
		}
	}

	return c
}

func printMatrix(m [3][3]int){
	for i:=0; i < len(m); i++{
		for j:=0; j < len(m); j++{
			fmt.Printf("[ %d ]", m[i][j])
		}
		fmt.Println()
	}
}

func main(){
	fmt.Println("Program Demostration of matrix multiplication using naive method")
	rand.Seed(time.Now().UnixNano())
	m1 := [3][3]int{}
	m2 := [3][3]int{}

	// generating random numbers for matrix 1
	for i:= 0; i < 3; i++{
		for j:= 0; j < 3; j++{
			m1[i][j] = rand.Intn(10)
		}	
	}

	// generating random numbers for matrix 2
	for i:= 0; i < 3; i++{
		for j:= 0; j < 3; j++{
			m2[i][j] = rand.Intn(20)
		}	
	}

	fmt.Println("Matrix 1")
	printMatrix(m1)

	fmt.Println("Matrix 2")
	printMatrix(m2)
	
	ans := naiveMultiplication(m1, m2)
	fmt.Println("Answer For Multiplication")
	printMatrix(ans)

}