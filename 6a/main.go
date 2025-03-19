package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	var a, b, c, d int
	fmt.Fscan(reader, &a, &b, &c, &d)
	nums := []int{a, b, c, d}
	sort.Ints(nums)
	a = nums[0]
	b = nums[1]
	c = nums[2]
	d = nums[3]

	if a+b > c || b+c > d {
		fmt.Println("TRIANGLE")
	} else if a+b == c || b+c == d {
		fmt.Println("SEGMENT")
	} else {
		fmt.Println("IMPOSSIBLE")
	}

}
