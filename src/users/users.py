"""
    This is the file you edit.

    You *do not need to create a new file*. Just edit this file to achieve what is needed.

    Fill in the functions provided to solve the puzzle.

    DO NOT EDIT THE EXISTING CODE UNLESS OTHERWISE SPECIFIED. You do not need to change the function definition lines. Just add your code inside the bodies.
"""

# Uncomment import line to view data in LiveCode
# Comment out to run tests
# from user_list import users as sample_data

def users_online(users: dict) -> int:
    ''' Edit here, and change the return line to
    return the expected data.
    '''
    user_values = list(users.values())
    online_count = user_values.count("online")
    return online_count


def user_status_report(users: dict) -> str:
    ''' Edit here, and change the return line to
    return the expected data.
    '''
    user_values = list(users.values())
    online_count = user_values.count("online")
    offline_count = user_values.count("offline")
    total = f'There are {online_count} of {offline_count + online_count} users online.'
    return total

# print(users_online(sample_data))
# print(user_status_report(sample_data))