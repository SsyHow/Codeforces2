package main

import (
	"bufio"
	"fmt"
	"os"
)

func solve(reader *bufio.Reader) (int, int, int) {
	var b int
	fmt.Fscan(reader, &b)
	for i := 0; i < b/7+1; i++ {
		for j := 0; j < b/5+1; j++ {
			for k := 0; k < b/3+1; k++ {
				if k*3+j*5+i*7 == b {
					//fmt.Println(k, j, i)
					return k, j, i
				}
			}
		}
	}
	return -1, -1, -1

}

func main() {
	reader := bufio.NewReader(os.Stdin)
	var a int
	fmt.Fscan(reader, &a)
	for i := 0; i < a; i++ {
		x, y, z := solve(reader)
		if x != -1 {
			fmt.Println(x, y, z)

		} else {
			fmt.Println(-1)
		}
	}

}
