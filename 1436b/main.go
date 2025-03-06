package main

import (
	"bufio"
	"fmt"
	"os"
)

func solve(reader *bufio.Reader) {
	var b int
	fmt.Fscan(reader, &b)
	matrix := make([][]int, b)
	for i := range matrix {
		matrix[i] = make([]int, b)
	}
	for i := 0; i < b; i++ {
		matrix[i][i] = 1
		matrix[i][b-i-1] = 1
	}
	if b&1 == 1 {
		matrix[b/2-1][b/2] = 1
		matrix[b/2][b/2+1] = 1
	}
	for _, row := range matrix {
		for _, i := range row {
			fmt.Print(i, " ")
		}
		fmt.Println()
	}
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	var a int
	fmt.Fscan(reader, &a)
	for i := 0; i < a; i++ {
		solve(reader)
	}
}
