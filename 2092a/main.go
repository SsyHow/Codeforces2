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
	mh, ml := -1<<31, (1<<31)-1
	var k int
	for i := 0; i < b; i++ {
		Fscan(in, &k)
		mh = max(mh, k)
		ml = min(ml, k)
	}
	Fprintln(out, mh-ml)
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
