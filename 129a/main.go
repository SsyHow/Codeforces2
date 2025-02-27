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
	var ans, odd, even int
	var b int

	for i := 1; i <= a; i++ {
		fmt.Fscan(reader, &b)
		ans += b
		if b&1 == 0 {
			even++
		} else {
			odd++
		}
	}

	if ans&1 == 0 {
		fmt.Println(even)
	} else {
		fmt.Println(odd)
	}

}
