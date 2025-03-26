package main

import (
	"bufio"
	"fmt"
	"os"
)

func solve(reader *bufio.Reader, out *bufio.Writer) {
	var b, c, d int
	fmt.Fscan(reader, &b, &c, &d)
	if c > d {
		c, d = d, c
	}

	if c != 0 || d == 0 {
		fmt.Fprintln(out, -1)
	} else if (b-1)%d == 0 {
		k := d + 2
		L := make([]int, 0, d)
		for i := 0; i < d; i++ {
			L = append(L, 1)
		}

		for i := d; i < b-1; i++ {
			if k+d-1 > i+1 {
				L = append(L, k)
			} else {
				k += d
				L = append(L, k)
			}
		}
		for i, v := range L {
			if i > 0 {
				fmt.Fprint(out, " ")
			}
			fmt.Fprint(out, v)
		}
		fmt.Fprintln(out)

	} else {
		fmt.Fprintln(out, -1)
	}
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	var a int
	fmt.Fscan(in, &a)
	for i := 0; i < a; i++ {
		solve(in, out)
	}
}
