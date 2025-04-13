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
	L := make([]int, a)

	for i := 0; i < a; i++ {
		Fscan(in, &L[i])
	}
	ans := 0
	for i, v := range L {
		if v == 1 {
			ans += 1
		} else if 0 < i && i < a-1 && L[i-1] == 1 && L[i+1] == 1 {
			ans += 1
		}
	}
	Fprintln(out, ans)
}

func main() {
	run(os.Stdin, os.Stdout)
}
