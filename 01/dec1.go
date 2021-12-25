package main

import (
	"bufio"
	"log"
	"os"
	"strconv"
)

var report []int

func part1() {
	count := 0
	for i := 0; i < (len(report) - 1); i++ {
		if report[i+1] > report[i] {
			count++
		}
	}
	log.Println("part1:", count)
}

func part2() {
	count := 0
	for i := 0; i < (len(report) - 3); i++ {
		w1 := report[i] + report[i+1] + report[i+2]
		w2 := report[i+1] + report[i+2] + report[i+3]
		if w2 > w1 {
			count++
		}
	}
	log.Println("part2:", count)
}

func main() {
	log.Println("Day 1")
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}

	sc := bufio.NewScanner(file)
	//report := []int{}
	//count := 0
	for sc.Scan() {
		n, err := strconv.Atoi(sc.Text())
		if err != nil {
			log.Fatal(err)
		}
		report = append(report, n)
		//log.Println(sc.Text())
		//count++
	}

	part1()
	part2()
}
