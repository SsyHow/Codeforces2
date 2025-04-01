package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	var a int
	fmt.Fscan(reader, &a)
	x, y := 0, 0
	k := 0
	for i := 0; i < a; i++ {
		fmt.Fscan(reader, &x, &y)
		k = max(k, x+y)
	}
	fmt.Println(k)
}
