package main

import (
	"bufio"
	"log"
	"os"
)

func main() {
	log.Println("Day 3")
	file, err := os.Open("test.txt")
	//file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}

	sc := bufio.NewScanner(file)
	for sc.Scan() {
	}
}
