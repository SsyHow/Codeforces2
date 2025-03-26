package main

import (
	"bufio"
	"fmt"
	"os"
)

func solve(reader *bufio.Reader) {
	var n, m int
	fmt.Fscan(reader, &n, &m)

	L := make([][]int, n)
	for i := 0; i < n; i++ {
		row := make([]int, 0, m)
		if i%4 == 0 || i%4 == 3 {
			for j := 0; j < m/4; j++ {
				row = append(row, 1, 0, 0, 1)

			}
			if m%4 == 2 {
				row = append(row, 1, 0)
			}
		} else {
			for j := 0; j < m/4; j++ {
				row = append(row, 0, 1, 1, 0)
			}
			if m%4 == 2 {
				row = append(row, 0, 1)
			}
		}
		L[i] = row
	}

	for _, row := range L {
		for j, val := range row {
			if j > 0 {
				fmt.Print(" ")
			}
			fmt.Print(val)
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
