package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func solve(reader *bufio.Reader) {
	var b int
	var s string
	fmt.Fscan(reader, &b)
	fmt.Fscan(reader, &s)
	ones := 0
	for _, v := range s {
		if v == '1' {
			ones += 1
		}

	}

	if ones > 2 && ones&1 == 0 {
		fmt.Println("YES")
	} else if ones == 0 || (ones == 2 && !strings.Contains(s, "11")) {
		fmt.Println("YES")
	} else {
		fmt.Println("NO")
	}

}

func main() {
	reader := bufio.NewReader(os.Stdin)
	var a int
	fmt.Fscan(reader, &a)
	for i := 0; i < a; i++ {
		solve(reader)
	}
}
