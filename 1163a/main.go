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
	if b == 0 {
		Println(1)
	} else {
		Println(min(a-b, b))
	}

}

func main() {
	run(os.Stdin, os.Stdout)
}
