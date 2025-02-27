package main

import (
	"bufio"
	"fmt"
	"os"
)

func solve(reader *bufio.Reader) {
	var a int
	fmt.Fscan(reader, &a)

	s1, m1 := 0, (1<<31)-1

	for i := 0; i < a; i++ {
		var s int
		fmt.Fscan(reader, &s)
		s1 += s
		m1 = min(m1, s)
	}
	s2, m2 := 0, (1<<31)-1
	for i := 0; i < a; i++ {
		var s int
		fmt.Fscan(reader, &s)
		s2 += s
		m2 = min(m2, s)
	}
	//fmt.Println(s1, s2, m1, m2)
	fmt.Println(min((m1*a)+s2, min((m2*a)+s1)))
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	var a int
	fmt.Fscan(reader, &a)
	for i := 1; i <= a; i++ {
		solve(reader)
	}
}
