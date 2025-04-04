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
}

func run(r io.Reader, w io.Writer) {
	in := bufio.NewReader(r)
	out := bufio.NewWriter(w)
	defer out.Flush()
	var a int
	Fscan(in, &a)
	L := make([]int, 3)
	var x int
	for i := 0; i < a; i++ {
		Fscan(in, &x)
		L[x-1]++
	}
	Fprintln(out, a-max(L[0], L[1], L[2]))

}

func main() {
	run(os.Stdin, os.Stdout)
}
