#Caameron Nakasone
#HW 1 Mini Projext Open Source Summer 2019 Bart Massey

import sys


#Read in file from the command line if no file display error
if len(sys.argv) == 1:
    print("No file provided, please run program with file")
else:
    #Read in content of file and store in variable
    fileContent = None
    f = open(sys.argv[1], "r")
    if f.mode == 'r':
        fileContent = f.readlines()

    #Get dimensions of canvas
    dimensions = fileContent[0].split(' ')
    #If canvas size input is wrong display error and quit program
    if len(dimensions) != 2:
        print("Invalid number of argument on first line of file for canvas size. Must be two numbers seperated by space")
        sys.exit()
    rows = dimensions[0]
    rows = int(rows, 10)
    cols = dimensions[1]
    cols = cols[:-1]
    cols = int(cols, 10)
    #Print out canvas
    canvas = [[0 for x in range(cols)] for y in range(rows)]
    i = 0
    j = 0

    while i < rows:
        while j < cols:
            canvas[i][j] = "."
            j += 1
        j = 0
        i += 1

    #Take in command of each line and add it to the canvas
    line = 1
    while line < len(fileContent):
        command = fileContent[line].split(' ')

        #throw error and exit if command is invalid
        if len(command) != 5:
            print("Invalid number of arguments for one of the commands. Must be 5 arguments seperated by space")
            sys.exit()

        #get all arguments for the command
        character = command[0]
        rowP = int(command[1], 10)
        colP = int(command[2], 10)
        direction = command[3]
        length = command[4]
        #get rid of ending new line and convert to int
        length = length[:-1]
        length = int(length, 10)

        #set the correct positions to the character in command
        for x in range(length):
            #Check for in bounds of canvas for vertical
            if direction == 'v':
                if rowP < 0 or rowP > (rows - 1):
                    rowP += 1
                    continue
                if colP < 0 or colP > (cols - 1):
                    continue
                canvas[rowP][colP] = character
                rowP += 1
            #Check for in bounds of canvas for horizontal
            if direction == 'h':
                if rowP < 0 or rowP > (rows - 1):
                    continue
                if colP < 0 or colP > (cols - 1):
                    colP += 1
                    continue
                canvas[rowP][colP] = character
                colP += 1

        line += 1

    #get rid of last new line and print out canvas
    canvasPrint = ""
    for x in range(rows):
        for y in range(cols):
            canvasPrint = canvasPrint + canvas[x][y]
        canvasPrint = canvasPrint + "\n"

    canvasPrint = canvasPrint[:-1]
    print(canvasPrint)
