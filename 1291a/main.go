package main

import (
	"bufio"
	"fmt"
	"os"
)

func calc(s string) int {
	sum := 0
	for _, v := range s {
		sum += int(v)
	}
	return sum
}

func solve(reader *bufio.Reader) {
	var b int
	var s string
	fmt.Fscan(reader, &b, &s)
	k := b - 1
	for len(s) > 0 && (int(s[k])&1 == 0 || calc(s)&1 == 1) {
		s = s[:k]
		k -= 1
	}
	if len(s) == 0 {
		fmt.Println(-1)
	} else {
		fmt.Println(s)
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
