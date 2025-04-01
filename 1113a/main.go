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

	ans := min(a-1, b)
	k := 2
	for a-b-1 > 0 {
		ans += k
		k += 1
		a -= 1
	}

	fmt.Println(ans)
}
