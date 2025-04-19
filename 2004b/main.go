package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
)

func solve(in *bufio.Reader, out *bufio.Writer) {
	var x, y, m, n int
	Fscan(in, &x, &y, &m, &n)
	if m > y || x > n {
		Fprintln(out, 1)
		return
	}

	ll, rr := max(x, m), min(y, n)
	xl, xr := min(x, m), max(y, n)

	ans := rr - ll
	if xl < ll {
		ans += 1
	}
	if rr < xr {
		ans += 1
	}
	Fprintln(out, ans)
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
