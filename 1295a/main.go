package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func solve(reader *bufio.Reader) {
	var b int
	fmt.Fscanln(reader, &b)
	if b&1 == 1 {
		fmt.Println("7" + strings.Repeat("1", (b-3)/2))
	} else {
		fmt.Println(strings.Repeat("1", b/2))
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
