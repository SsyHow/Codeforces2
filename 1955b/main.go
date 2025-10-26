package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
)

func solve(in *bufio.Reader, out *bufio.Writer) {
	var n, c, d int
	Fscan(in, &n, &c, &d)

	dic := make(map[int]int)
	M := make([]int, n)
	x := 10_000_000_000
	var tmp int
	for i := 0; i < n*n; i++ {
		Fscan(in, &tmp)
		x = min(x, tmp)
		dic[tmp] += 1
	}

	for i := 0; i < n; i++ {
		M[i] = i*c + x
	}

	for _, a := range M {
		for j := 0; j < n; j++ {
			dic[d*j+a] -= 1
			if dic[d*j+a] < 0 {
				Fprintln(out, "NO")
				return
			}
		}
	}

	for _, v := range dic {
		if v != 0 {
			Fprintln(out, "NO")
			return
		}
	}
	Fprintln(out, "YES")
	return
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
