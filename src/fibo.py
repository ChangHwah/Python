"""
    This is the file you edit.

    You *do not need to create a new file*. Just edit this file to achieve what is needed.

    Fill in the functions provided to solve the puzzle.

    DO NOT EDIT THE FUNCTION DEFINITION LINES. Just update the body of the function.
"""

def fibo_sequence(end: int) -> list:
    first, second = 0, 1
    sequence = []
    while True:
        third = first + second
        sequence.append(first)
        if first >= end:
            return sequence
        first = second
        second = third
# print(fibo_sequence(4))
