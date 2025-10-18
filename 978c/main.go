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
	L := make([][]int, a)
	start := 1
	end := 0
	for i := 0; i < a; i++ {
		Fscan(in, &end)
		L[i] = []int{start, start + end - 1}
		start += end
	}
	x := 0
	idx := 0

	for i := 0; i < b; i++ {
		Fscan(in, &x)

		for idx < a {
			if x > L[idx][1] {
				idx += 1
			} else {
				Fprintln(out, idx+1, x-L[idx][0]+1)
				break
			}
		}
	}
}

func main() {
	run(os.Stdin, os.Stdout)
}
