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

	L := make([]int, 26)
	f := true
	for _, v := range s {
		L[v-'a'] += 1
		if L[v-'a'] > b {
			f = false
		}
	}
	if f {
		Println("YES")
	} else {
		Println("NO")
	}

}

func main() {
	run(os.Stdin, os.Stdout)
}
