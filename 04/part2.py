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
        # add line to board
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

last_score = 0
num_boards = len(boards)
for draw in draw_numbers:
    blank_boards = 0
    for board in boards:
        if len(board) > 0:
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
                last_score = score(draw, board)
                board.clear()
        else:
            blank_boards += 1
    if blank_boards == num_boards:
        break

print(last_score)

print("--- runtime %s seconds ---" % (time.time() - start_time))
