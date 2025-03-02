package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	var a int
	fmt.Fscan(reader, &a)
	L := make([]int, a)
	x := 0
	cnt := 0
	mx := -1
	o := 0
	for i := 0; i < a; i++ {
		fmt.Fscan(reader, &x)
		L[i] = x
		if x == 0 {
			cnt += 1
			mx = max(mx, cnt)
		} else {
			if cnt > 0 {
				cnt -= 1
			}
			o += 1

		}

	}
	if a == 1 {
		if L[0] == 0 {
			fmt.Println(1)
		} else {
			fmt.Println(0)
		}

	} else if o == a {
		fmt.Println(a - 1)
	} else {
		fmt.Println(o + mx)
	}
}
