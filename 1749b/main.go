package main

import (
	"bufio"
	"fmt"
	"os"
)

func solve(reader *bufio.Reader) {
	var b int
	fmt.Fscan(reader, &b)
	var x int
	Lsum := 0
	Msum := 0
	Mmax := 0
	for i := 0; i < b; i++ {
		fmt.Fscan(reader, &x)
		Lsum += x
	}
	for i := 0; i < b; i++ {
		fmt.Fscan(reader, &x)
		Msum += x
		Mmax = max(Mmax, x)
	}
	fmt.Println(Lsum + Msum - Mmax)

}

func main() {
	reader := bufio.NewReader(os.Stdin)
	var a int
	fmt.Fscan(reader, &a)
	for i := 0; i < a; i++ {
		solve(reader)
	}
}
