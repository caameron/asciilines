# HW 1 Mini Project

Copyright (c) 2019 Caameron Nakasone

## Description of Program

This program is a command-line program that takes in a .tvg file and outputs ASCII
lines on standard output according to the .tvg file. The .tvg files should have commands
which will determine what characters are output and where they belong.
The program starts out by reading in the file and making a canvas with a 2d array of chars
according to the dimensions specified. It will then loop through each command given
in the .tvg file. The commands will be parsed and used to change the chars in the
2d array. Finally the 2d array is printout using standard output.

## Build and Run

To build and run this program run `python asciilines.py <tvg file>` on the command line
The output of the program will be output immediately after.
For example,

    python asciilines.py tests/test6.tvg
    C.......
    .A......
    ..A.....
    ...M....
    ....E...
    .....R..
    ......O.
    .......N

## Bugs/Defects/Failing Tests/Issues

Currently there are no bugs, defects, or failing tests that we are aware of.
There are four tests that test various input and outputs for the program and there
are 2 tests for invalid input errors which all pass.
The only issue with the program is that there is minimum error handling. The
program fails on invalid input however there is no error handling for edge cases
or rare events that might occur.

## License

This program is llicensed under the "MIT LIcense". Please
see the file `LICENSE` in the source distribution of this
software for licesnse terms.

