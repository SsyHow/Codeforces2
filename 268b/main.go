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
	ans := (a + 1) * a / 2
	k := 1
	for i := a - 2; i > 0; i-- {
		ans += i * k
		k++
	}
	Fprintln(out, ans)
}

func main() {
	run(os.Stdin, os.Stdout)
}
