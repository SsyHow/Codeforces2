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
}

func run(r io.Reader, w io.Writer) {
	in := bufio.NewReader(r)
	out := bufio.NewWriter(w)
	defer out.Flush()
	var a, b int
	Fscan(in, &a, &b)
	L := make([]int, a)
	for i := 0; i < a; i++ {
		Fscan(in, &L[i])
	}
	sort.Ints(L)
	b *= 2
	ans := 0
	for i := 1; i < a; i++ {
		if L[i]-L[i-1] > b {
			ans += 2
		} else if L[i]-L[i-1] == b {
			ans += 1
		}
	}
	Fprintln(out, ans+2)
}

func main() {
	run(os.Stdin, os.Stdout)
}
