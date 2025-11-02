package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
	"sort"
)

func solve(in *bufio.Reader, out *bufio.Writer) {
	var b int
	Fscan(in, &b)
	L := make([]int, b)
	for i := 0; i < b; i++ {
		Fscan(in, &L[i])
	}
	sort.Ints(L)
	q := 1
	if L[0] != 1 {
		Fprintln(out, "NO")
		return
	}

	for i := 1; i < b; i++ {
		if L[i] > q {
			Fprintln(out, "NO")
			return
		}
		q += L[i]
	}
	Fprintln(out, "YES")
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
