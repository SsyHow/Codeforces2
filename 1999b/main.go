package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
)

func solve(in *bufio.Reader, out *bufio.Writer) {
	var a1, a2, b1, b2 int
	Fscan(in, &a1, &a2, &b1, &b2)
	ans := 0
	if ((a1 > b1) && (a2 >= b2)) || ((a1 >= b1) && (a2 > b2)) {
		ans++
	}
	if ((a1 > b2) && (a2 >= b1)) || ((a1 >= b2) && (a2 > b1)) {
		ans++
	}
	if ((a2 > b1) && (a1 >= b2)) || ((a2 >= b1) && (a1 > b2)) {
		ans++
	}
	if ((a2 > b2) && (a1 >= b1)) || ((a2 >= b2) && (a1 > b1)) {
		ans++
	}
	Fprintln(out, ans)
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
