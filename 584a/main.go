package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
	"strconv"
	"strings"
)

func run(r io.Reader, w io.Writer) {
	in := bufio.NewReader(r)
	out := bufio.NewWriter(w)
	defer out.Flush()
	var a, b int
	Fscan(in, &a, &b)

	if a == 1 && b == 10 {
		Fprintln(out, -1)
	} else if b == 10 {
		Fprintln(out, strconv.Itoa(b)+strings.Repeat("0", a-2))
	} else {
		Fprintln(out, strconv.Itoa(b)+strings.Repeat("0", a-1))
	}

}

func main() {
	run(os.Stdin, os.Stdout)
}
