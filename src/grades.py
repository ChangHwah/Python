"""
    This is the file you edit.

    You *do not need to create a new file*. Just edit this file to achieve what is needed.

    Fill in the functions provided to solve the puzzle.

    DO NOT EDIT THE EXISTING CODE UNLESS OTHERWISE SPECIFIED. You do not need to change the function definition lines. Just add your code inside the bodies.
"""

def grade(percent: float) -> str:
    '''
    Replace entire body with your code
    '''
    if(percent > 100):
        return 'A+'
    elif(percent >= 93):
        return 'A'
    elif(percent >= 90):
        return 'A-'
    elif(percent >= 87):
        return 'B+'
    elif(percent >= 83):
        return 'B'
    elif(percent >= 80):
        return 'B-'
    elif(percent >= 77):
        return 'C+'
    elif(percent >= 73):
        return 'C'
    elif(percent >= 70):
        return 'C-'
    elif(percent >= 68):
        return 'D+'
    elif(percent >= 66):
        return 'D'
    elif(percent >= 65):
        return 'D-'
    else:
        return 'F'
    # pass # Remove me

