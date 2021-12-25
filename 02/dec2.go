package main

import (
	"bufio"
	"log"
	"os"
	"strconv"
	"strings"
)

type p1struct struct {
	horiz int
	depth int
}

type p2struct struct {
	horiz int
	depth int
	aim   int
}

var p1 p1struct
var p2 p2struct

func part1proc(dir string, amnt int) {
	switch dir {
	case "forward":
		p1.horiz += amnt
	case "up":
		p1.depth -= amnt
	case "down":
		p1.depth += amnt
	default:
		log.Println("unknown:", dir)
	}
}

func part1() {
	//log.Println("Part One:", "horiz:", p1.horiz, "depth:", p1.depth)
	log.Println("Part One:", "product:", p1.horiz*p1.depth)
}

func part2proc(dir string, amnt int) {
	switch dir {
	case "forward":
		p2.horiz += amnt
		p2.depth += p2.aim * amnt
	case "up":
		p2.aim -= amnt
	case "down":
		p2.aim += amnt
	default:
		log.Println("unknown:", dir)
	}
}

func part2() {
	//log.Println("Part Two:", "horiz:", p2.horiz, "depth:", p2.depth)
	log.Println("Part Two:", "product:", p2.horiz*p2.depth)
}

func main() {
	log.Println("Day 2")
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}

	sc := bufio.NewScanner(file)
	for sc.Scan() {
		dir := strings.Split(sc.Text(), " ")
		amnt, err := strconv.Atoi(dir[1])
		if err != nil {
			log.Fatalln(err)
		}
		part1proc(dir[0], amnt)
		part2proc(dir[0], amnt)
	}

	part1()
	part2()
}
