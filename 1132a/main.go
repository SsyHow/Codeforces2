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
	var a, b, c, d int
	Fscan(in, &a, &b, &c, &d)
	if (a == d) && ((c > 0 && a > 0) || c == 0) {
		Fprintln(out, 1)
	} else {
		Fprintln(out, 0)
	}
}

func main() {
	run(os.Stdin, os.Stdout)
}
