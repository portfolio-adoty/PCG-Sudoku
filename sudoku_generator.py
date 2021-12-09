"""
Sudoku Generator
Andi Doty
December 8, 2021
"""

import turtle
import random
import subprocess
import os

board = []
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

count = 1

myPen = turtle.Turtle()
# myPen.tracer(0)
myPen.speed(0)
myPen.color("#000000")
myPen.hideturtle()
topLeft_x = -240
topLeft_y = 240

def text(message, x, y, size):

    FONT = ('Arial', size, 'normal')
    myPen.penup()
    myPen.goto(x, y)    		
    myPen.write(message, align = "center",font = FONT)

#A procedure to draw the grid on screen using Python Turtle
def draw_board(grid):

    turtle.hideturtle()
    intDim = 50

    text("Sudoku by Andi Doty", topLeft_x + 228, topLeft_y + 10, 18)


    for row in range(0, 10):

        if (row % 3) == 0:

            myPen.pensize(3)

        else:

            myPen.pensize(1)

        myPen.penup()
        myPen.goto(topLeft_x, topLeft_y-row * intDim)
        myPen.pendown()
        myPen.goto(topLeft_x + 9 * intDim, topLeft_y-row * intDim)

    for col in range(0,10):

        if (col % 3) == 0:

            myPen.pensize(3)

        else:

            myPen.pensize(1)

        myPen.penup()
        myPen.goto(topLeft_x + col * intDim, topLeft_y)
        myPen.pendown()
        myPen.goto(topLeft_x + col * intDim, topLeft_y - 9 * intDim)

    for row in range (0,9):

        for col in range (0,9):

            if grid[row][col]!= 0:

                text(grid[row][col], topLeft_x + col * intDim + 25,topLeft_y - row * intDim - intDim + 8, 28)

def print_board(grid):

    for row in grid:

        row_str = ""

        for item in row:

            if item == 0:

                row_str += "   "
                continue

            row_str += str(item) + "  "

        print(row_str)

def shuffle(li):

    for i in range(len(li)):

        r = i + (random.randint(1, 9) % (len(li) -i))
        tmp = li[i]

        li[i] = li[r]
        li[r] = tmp

    return li

def check_board(grid):

    for row in range(9):

      for col in range(9):

        if grid[row][col] == 0:

          return False

    return True

def fill(grid, num):

    for i in range(81):

        row = i // 9
        col = i % 9

        nums = shuffle(num)

        if grid[row][col] == 0:

            for val in nums: # Values 1 - 9

                if not val in grid[row]:

                    if not val in (grid[0][col], grid[1][col], grid[2][col], grid[3][col], grid[4][col], grid[5][col], grid[6][col], grid[7][col], grid[8][col]):

                        square_vals = []

                        square_col = col // 3
                        square_row = row // 3

                        for r in range(square_row * 3, square_row * 3 + 3):

                            for j in range(square_col * 3, square_col * 3 + 3):

                                square_vals.append(grid[r][j])

                        if not val in square_vals:

                            grid[row][col] = val

                            if check_board(grid):

                                return True

                            else:

                                if fill(grid, nums):

                                    return True

            break

    grid[row][col] = 0

def solve(grid):

    #global count

    for i in range(81):

        row = i // 9
        col = i % 9

        if grid[row][col] == 0:

            for val in range(1, 10): # Values 1 - 9

                if not val in grid[row]:

                    if not val in (grid[0][col], grid[1][col], grid[2][col], grid[3][col], grid[4][col], grid[5][col], grid[6][col], grid[7][col], grid[8][col]):

                        square_vals = []

                        square_col = col // 3
                        square_row = row // 3

                        for r in range(square_row * 3, square_row * 3 + 3):

                            for j in range(square_col * 3, square_col * 3 + 3):

                                square_vals.append(grid[r][j])

                        if not val in square_vals:

                            grid[row][col] = val

                            if check_board(grid):

                                global count
                                count += 1
                                break

                            else:

                                if solve(grid):

                                    return True

            break

    grid[row][col] = 0


def make_puzzle(grid):

    global count
    global board

    attempts = 7
    count = 0

    while attempts > 0:

        row = random.randint(0, 8)
        col = random.randint(0, 8)

        while board[row][col] == 0:

            row = random.randint(0, 8)
            col = random.randint(0, 8)

        temp = board[row][col]

        board[row][col] = 0

        #Take a full copy of the grid
        copy_grid = []

        for r in range(0, 9):

            rl = []

            for c in range(0, 9):

                rl.append(board[r][c])

            copy_grid.append(rl)

        count = 0
        solve(copy_grid)

        if count != 1:

            board[row][col] = temp
            attempts -= 1

# Generates an empty board.
def clear(grid):

    grid = []

    for r in range(9):

        row = []

        for c in range(9):

            row.append(0)

        grid.append(row)

    return grid

def new_game():

    global board

    board = clear(board)
    fill(board, nums)
    make_puzzle(board)
    draw_board(board)

new_game()

ts = turtle.getscreen()
ts.getcanvas().postscript(file="tmp.ps")
process = subprocess.Popen(["ps2pdf", "tmp.ps", "sudoku.pdf"], shell=True)
process.wait()
os.remove("tmp.ps")
turtle.done()