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
	ans := 0
	k := 1<<31 - 1
	for i := 1; i <= a; i++ {
		var x, y int
		fmt.Fscan(reader, &x, &y)
		k = min(k, y)
		ans += k * x
	}
	fmt.Println(ans)
}
