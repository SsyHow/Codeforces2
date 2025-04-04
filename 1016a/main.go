package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
)

func run(r io.Reader, w io.Writer) {
	in := bufio.NewReader(r)
	out := bufio.NewWriter(w)
	defer out.Flush()
	var a, b int
	Fscan(in, &a, &b)
	left := 0
	var x int
	for i := 0; i < a; i++ {
		Fscan(in, &x)
		k := (left + x) / b
		Fprint(out, k, " ")
		left = (left + x) % b
	}
	Fprintln(out)

}

func main() {
	run(os.Stdin, os.Stdout)
}
