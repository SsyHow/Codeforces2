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
	if b%3 == 0 {
		Fprintln(out, "YES")
	} else if b%7 == 0 {
		Fprintln(out, "YES")
	} else {
		k := 1
		f := false
		for k*3 < b {
			if (b-k*3)%7 == 0 {
				f = true
				break
			}
			k++
		}
		if f {
			Fprintln(out, "YES")
		} else {
			Fprintln(out, "NO")
		}
	}
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
