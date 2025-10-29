package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
)

func run(r io.Reader, w io.Writer) {
	in := bufio.NewReader(r)
	out := bufio.NewWriter(w)
	defer out.Flush()
	var a, b int
	Fscan(in, &a, &b)
	x := 0
	for {
		if a == b {
			break
		}
		if a > b {
			b += 1
		} else {
			if b&1 == 0 {
				b /= 2
			} else {
				b += 1
			}
		}

		x += 1
	}
	Println(x)
}

func main() {
	run(os.Stdin, os.Stdout)
}
