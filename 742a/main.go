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
	var a int
	Fscan(in, &a)
	L := [4]int{8, 4, 2, 6}
	if a == 0 {
		Fprintln(out, 1)
	} else {
		k := a%4 - 1
		if k < 0 {
			k += 4
		}
		Fprintln(out, L[k])
	}
}

func main() {
	run(os.Stdin, os.Stdout)
}
