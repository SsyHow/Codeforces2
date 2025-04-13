package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
	"slices"
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
	var x int
	for i := 0; i < b; i++ {
		Fscan(in, &x)
		L[x-1]++
	}
	Fprintln(out, slices.Min(L))

}

func main() {
	run(os.Stdin, os.Stdout)
}
