package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
	"sort"
)

func solve(in *bufio.Reader, out *bufio.Writer) {
	var b, c int
	Fscan(in, &b, &c)
	L := make([]int, b)
	for i := 0; i < b; i++ {
		Fscan(in, &L[i])
	}
	sort.Ints(L)
	ans := 0
	x := 1
	idx := b - 1
	for idx >= 0 {
		//Fprintln(out, L[idx], ans)
		if L[idx]*x > c {
			ans++
		} else {
			x *= 2
		}
		idx -= 1
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
