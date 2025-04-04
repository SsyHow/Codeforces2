package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
)

func run(z io.Reader, w io.Writer) {
	in := bufio.NewReader(z)
	out := bufio.NewWriter(w)
	defer out.Flush()
	var a, b, c int
	Fscan(in, &a, &b, &c)
	var k, r int
	k = (c - a) / b
	r = (c - a) % b

	if (r == 0 && k >= 0) || (r == 1 && k > 0) {
		Println("YES")
	} else {
		Println("NO")
	}

}

func main() {
	run(os.Stdin, os.Stdout)
}
