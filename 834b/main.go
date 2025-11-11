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
	var s string
	Fscan(in, &s)
	L := []rune(s)
	last := make(map[rune]int)
	act := make(map[rune]bool)

	for i := 0; i < a; i++ {
		last[L[i]] = i
	}

	for i := 0; i < a; i++ {
		act[L[i]] = true
		if len(act) > b {
			Fprintln(out, "YES")
			return
		}
		if last[L[i]] == i {
			delete(act, L[i])
		}
	}
	Fprintln(out, "NO")
}

func main() {
	run(os.Stdin, os.Stdout)
}
