package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
	"sort"
)

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
	sort.Slice(L, func(i, j int) bool {
		return L[i] > L[j]
	})

	for i := 0; i < a-2; i++ {
		if L[i] < L[i+1]+L[i+2] {
			Fprintln(out, "YES")
			return
		}
	}
	Fprintln(out, "NO")
	return
}

func main() {
	run(os.Stdin, os.Stdout)
}
