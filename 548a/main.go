package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
)

func reverse(s string) string {
	runes := []rune(s)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes)
}

func run(r io.Reader, w io.Writer) {
	in := bufio.NewReader(r)
	out := bufio.NewWriter(w)
	defer out.Flush()
	var a string
	Fscan(in, &a)
	k := len(a)
	var b int
	Fscan(in, &b)
	if k%b == 0 {

		for i := 0; i < k; i += k / b {
			x := a[i : i+k/b]
			if x != reverse(x) {
				Fprintln(out, "NO")
				return
			}
		}
		Fprintln(out, "YES")
	} else {
		Fprintln(out, "NO")
	}

}

func main() {
	run(os.Stdin, os.Stdout)
}
