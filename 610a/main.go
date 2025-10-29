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
	var a int
	Fscan(in, &a)
	if a&1 == 0 {
		if (a/2)&1 == 1 {
			Fprintln(out, a/4)
		} else {
			Fprintln(out, a/4-1)
		}
	} else {
		Fprintln(out, 0)
	}

}

func main() {
	run(os.Stdin, os.Stdout)
}
