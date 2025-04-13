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
	var s string
	Fscan(in, &s)
	ans := 0
	for _, v := range s {
		if v == '0' {
			Fprintln(out, ans+1)
			return
		}
		ans += 1
	}
	Fprintln(out, ans)
	return

}

func main() {
	run(os.Stdin, os.Stdout)
}
