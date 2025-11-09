package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
)

func solve(in *bufio.Reader, out *bufio.Writer) {
	var b int
	Fscan(in, &b)
	var x, y, m, n int
	n = 1 << 60
	for i := 0; i < b; i++ {
		Fscan(in, &x, &y)
		m = max(m, x)
		n = min(n, y)

	}
	Fprintln(out, max(0, m-n))
}

func run(r io.Reader, w io.Writer) {
	in := bufio.NewReader(r)
	out := bufio.NewWriter(w)
	defer out.Flush()
	var a int
	Fscan(in, &a)
	for i := 0; i < a; i++ {
		solve(in, out)
	}

}

func main() {
	run(os.Stdin, os.Stdout)
}
