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
	x := 0
	y := 0
	z := 0
	var b int
	for i := 0; i < a; i++ {
		Fscan(in, &b)
		x ^= b
	}
	for i := 0; i < a-1; i++ {
		Fscan(in, &b)
		y ^= b
	}
	for i := 0; i < a-2; i++ {
		Fscan(in, &b)
		z ^= b
	}
	Fprintln(out, x^y)
	Fprintln(out, y^z)
}

func main() {
	run(os.Stdin, os.Stdout)
}
