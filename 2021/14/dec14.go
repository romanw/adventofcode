package main

import (
	"bufio"
	"log"
	"os"
	"sort"
	"strings"
)

var rules map[string]string

func p1(tmpl string, rules map[string]string, steps int) {
	elements := make(map[string]int)
	pairs := make(map[string]int)
	for _, c := range tmpl {
		elements[string(c)]++
	}

	for i := 0; i < len(tmpl)-1; i++ {
		pairs[tmpl[i:i+2]]++
	}

	for i := 0; i < steps; i++ {
		newPairs := make(map[string]int)
		for pair, v := range pairs {
			e := rules[pair]
			elements[e] += v
			p1 := string(pair[0]) + string(e)
			p2 := string(e) + string(pair[1])
			newPairs[p1] += v
			newPairs[p2] += v
		}
		pairs = newPairs
	}

	var arr []int
	for _, e := range elements {
		arr = append(arr, e)
	}

	sort.Ints(arr)
	log.Println(arr[len(arr)-1] - arr[0])
}

func main() {
	log.Println("Day 14")
	//file, err := os.Open("test.txt")
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}

	var template string
	rules = make(map[string]string)
	nl := false
	sc := bufio.NewScanner(file)
	for sc.Scan() {
		if len(sc.Text()) == 0 {
			nl = true
			continue
		}
		if nl {
			s := strings.Split(sc.Text(), " -> ")
			rules[s[0]] = s[1]
		} else {
			template = sc.Text()
		}
	}
	//log.Println(template)
	//log.Println(rules)
	p1(template, rules, 40)
}
