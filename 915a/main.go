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
	var a, b int
	Fscan(in, &a, &b)
	L := make([]int, a)
	for i := 0; i < a; i++ {
		Fscan(in, &L[i])
	}
	sort.Ints(L)
	for i := a - 1; i >= 0; i-- {
		if b%L[i] == 0 {
			Println(b / L[i])
			return
		}
	}

}

func main() {
	run(os.Stdin, os.Stdout)
}
