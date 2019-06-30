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
        #    canvas = canvas + "."
            j += 1
        #canvas = canvas + "\n"
        j = 0
        i += 1

    #get rid of last new line and print out canvas
    canvasPrint = ""
    print(canvas)
    for x in range(rows):
        for y in range(cols):
            canvasPrint = canvasPrint + canvas[x][y]
        canvasPrint = canvasPrint + "\n"

    canvasPrint = canvasPrint[:-1]
    print(canvasPrint)
