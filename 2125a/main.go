package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
)

func solve(in *bufio.Reader, out *bufio.Writer) {
	var n, m int
	Fscan(in, &n, &m)

	L := make([]int, m)
	f := true
	x := 0
	for i := 0; i < m; i++ {
		Fscan(in, &L[i])
		if i > 0 && L[i-1] >= L[i] {
			f = false
		}
		x = max(x, L[i])

	}

	if f {
		Fprintln(out, n-x+1)
	} else {
		Fprintln(out, 1)
	}
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
