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
	var x, sum int
	k := 1 << 31
	for i := 0; i < a; i++ {
		fmt.Fscan(reader, &x)
		if x < k && x&1 == 1 {
			k = x
		}
		sum += x
	}
	if sum&1 == 0 {
		fmt.Println(sum)
	} else {
		fmt.Println(sum - k)
	}
}
