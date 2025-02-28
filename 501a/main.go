package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	var a, b, c, d int
	fmt.Fscan(reader, &a, &b, &c, &d)

	n := max(3*a/10, a-a/250*c)
	m := max(3*b/10, b-b/250*d)

	if m == n {
		fmt.Println("Tie")
	} else if m > n {
		fmt.Println("Vasya")
	} else {
		fmt.Println("Misha")
	}
}
