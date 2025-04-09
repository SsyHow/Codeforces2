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
	var a, k int
	Fscan(in, &a)
	L := make([]int, a)
	for i := 0; i < a; i++ {
		Fscan(in, &L[i])
		k += L[i]
	}
	sort.Ints(L)
	ans := 0
	x := float32(k) / float32(a)
	if x >= 4.5 {
		Println(0)
		return
	}

	for _, v := range L {
		k += 5 - v
		ans += 1
		if float32(k)/float32(a) >= 4.5 {
			Println(ans)
			return
		}
	}
}

func main() {
	run(os.Stdin, os.Stdout)
}
