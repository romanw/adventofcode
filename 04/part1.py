#!/usr/bin/env python

import time
start_time = time.time()

file = open("input.txt", "r")

line = file.readline()
draw_numbers = line.split(",")
line = file.readline()

boards = []
board = ""
while (len(line) > 0):
    line = file.readline()
    if (len(line) > 1):
        # process board
        board += line + " "
    else:
        # end of board data
        board = board.split()
        boards.append(board)
        board = ""
    
file.close()

def score(draw, board):
    count = 0
    for number in board:
        if int(number) > 0:
            count += int(number)
    return count * int(draw)

def check_rows(board):
    # check the rows
    for row in range(5):
        count = 0
        for col in range(5):
            i = row * 5 + col
            count += int(board[i])
        if count == -5:
            # we have a winner
            return True
    return False

def check_cols(board):
    # check the columns
    for col in range(5):
        count = 0
        for row in range(5):
            i = row*5 + col
            count += int(board[i])
        if count == -5:
            # we have a winner
            return True
    return False

for draw in draw_numbers:
    for board in boards:
        # check the board for the drawn number and mark it if found
        for index, number in enumerate(board):
            if number == draw:
                board[index] = -1
        # check the board has won
        # check the rows
        iwon = check_rows(board)
        if not iwon:
            # check the columns
            iwon = check_cols(board)
        if iwon:
            print(score(draw, board))
            break
        else:
            continue
        break
    else:
        continue
    break
            

print("--- runtime %s seconds ---" % (time.time() - start_time))
