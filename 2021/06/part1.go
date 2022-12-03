package main

import (
	"fmt"
	"sort"
)

var fishes = []int{3, 4, 3, 1, 2}
//var fishes = []int{1, 4, 2, 4, 5, 3, 5, 2, 2, 5, 2, 1, 2, 4, 5, 2, 3, 5, 4, 3, 3, 1, 2, 3, 2, 1, 4, 4, 2, 1, 1, 4, 1, 4, 4, 4, 1, 4, 2, 4, 3, 3, 3, 3, 1, 1, 5, 4, 2, 5, 2, 4, 2, 2, 3, 1, 2, 5, 2, 4, 1, 5, 3, 5, 1, 4, 5, 3, 1, 4, 5, 2, 4, 5, 3, 1, 2, 5, 1, 2, 2, 1, 5, 5, 1, 1, 1, 4, 2, 5, 4, 3, 3, 1, 3, 4, 1, 1, 2, 2, 2, 5, 4, 4, 3, 2, 1, 1, 1, 1, 2, 5, 1, 3, 2, 1, 4, 4, 2, 1, 4, 5, 2, 5, 5, 3, 3, 1, 3, 2, 2, 3, 4, 1, 3, 1, 5, 4, 2, 5, 2, 4, 1, 5, 1, 4, 5, 1, 2, 4, 4, 1, 4, 1, 4, 4, 2, 2, 5, 4, 1, 3, 1, 3, 3, 1, 5, 1, 5, 5, 5, 1, 3, 1, 2, 1, 4, 5, 4, 4, 1, 3, 3, 1, 4, 1, 2, 1, 3, 2, 1, 5, 5, 3, 3, 1, 3, 5, 1, 5, 3, 5, 3, 1, 1, 1, 1, 4, 4, 3, 5, 5, 1, 1, 2, 2, 5, 5, 3, 2, 5, 2, 3, 4, 4, 1, 1, 2, 2, 4, 3, 5, 5, 1, 1, 5, 4, 3, 1, 3, 1, 2, 4, 4, 4, 4, 1, 4, 3, 4, 1, 3, 5, 5, 5, 1, 3, 5, 4, 3, 1, 3, 5, 4, 4, 3, 4, 2, 1, 1, 3, 1, 1, 2, 4, 1, 4, 1, 1, 1, 5, 5, 1, 3, 4, 1, 1, 5, 4, 4, 2, 2, 1, 3, 4, 4, 2, 2, 2, 3}
var days = []int{0, 0, 0, 0, 0, 0, 0}

func main() {
	sort.Ints(fishes)
	count := len(fishes)
	for day := 0; day < 18; day++ {
		end := len(fishes)
		for fish := 0; fish < end; fish++ {
			fishes[fish]--
			if fishes[fish] < 0 {
				fishes[fish] = 6
				fishes = append(fishes, 8)
				count++
			}
		}
		fmt.Println(day+1, fishes)
	}
	fmt.Println(count)
}