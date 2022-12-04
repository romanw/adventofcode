// run this file using the following command...
// deno run --allow-read main.ts

import { readLines } from "https://deno.land/std@0.167.0/io/mod.ts";

const filename = "input"
let fileReader = await Deno.open(filename)

let total1 = 0
let total2 = 0

for await (let line of readLines(fileReader)) {
  let elf = line.trim().split(",")
  let sec1 = elf[0].split("-")
  let sec2 = elf[1].split("-")
  let sec10 = parseInt(sec1[0])
  let sec11 = parseInt(sec1[1])
  let sec20 = parseInt(sec2[0])
  let sec21 = parseInt(sec2[1])
  // part 1 - one rang within another
  if ((sec20 >= sec10) && (sec21 <= sec11)) total1 += 1
  else if ((sec10 >= sec20) && (sec11 <= sec21)) total1 += 1
  // part 2 - one range overlaps or is within another
  if (sec20 > sec11) {}
  else if (sec21 < sec10) {}
  else total2 += 1
}

console.log("part1: " + total1)
console.log("part2: " + total2)
