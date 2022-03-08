"""
    Our tree could use some presents under it, don't you think?

    Your challenge is to use the manipulation techniques you've learned in this Unit to create some presents under the tree.

    TWO THINGS: 
        1. The one thing you *cannot* use is multi-line strings! You must use other string manipulation techniques to create the final output.
        2. You *must* use more than just string concatenation or interpolation. I expect to see *at least* string replication and would ideally like to see other data types and manipulation techniques, as well.
"""


def tree(rows: int) -> str:
    '''
    DO NOT ALTER THIS FUNCTION!

    You do not need to change this function. This function is here to create the tree for you, so that you have the full image in the Livecode window.
    '''
    out = '.'
    for row in range(rows):
        if row > 0: 
            out += '\n'

        out += '.' * ((row % 7) + row)

    return out


def presents() -> str:
    """
    Add the code here to make the presents.

    You DO NOT need to change the signature, just edit below this line.
    """
    out = ''
    out += '\n'
    out += '*' * 5 + '\n'
    out +='*****       \\-\\  /-/' + '\n'
    out +='*****  ______\\_\\/_/________' + '\n'
    out +='*****  |       ||         |' + '\n'
    out +='____   |       ||         |' + '\n'
    out +='   |   |       ||         |' + '\n'
    out +='---------      ||         |' + '\n'
    out +='|  __   |-------|         |' + '\n'
    out +='| |__|  |      |-----------' + '\n'
    out +='|       |      |' + '\n'
    out +='----------------'
    return out


print(tree(28))
print(presents())



