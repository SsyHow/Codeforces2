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
	var n, a, b int
	Fscan(in, &n, &a, &b)
	for i := 0; i < n/a+1; i++ {
		if (n-i*a)%b == 0 {
			Fprintln(out, "YES")
			Fprintln(out, i, (n-i*a)/b)
			return
		}
	}
	Fprintln(out, "NO")

}

func main() {
	run(os.Stdin, os.Stdout)
}
