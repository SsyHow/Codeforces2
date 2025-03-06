package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	var a, b int
	fmt.Fscan(reader, &a, &b)

	if a > 27 {
		fmt.Println(b)
	} else {
		fmt.Println(b % (1 << a))
	}

}
