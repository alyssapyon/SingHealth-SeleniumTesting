import random
import json

from CONSTANTS import *

# file to store registered accounts
# filename = "registeredAccounts.json"
filename = registeredAccounts_filepath


valid_characters = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
                    "W", "X", "Y", "Z", "_", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "@", ".", "+", "-"]

INvalid_characters = ["!", "#", "$", "%", "&",
                      "(", ")", "{", "}", "[", "]", "|", "*", ",", "<", ">", "=", "/", "\\", ":", ";", "~", "`", "'", '"', "^"]
# invalid characters -> not only alphanumeric


def generate_username_INvalid_chars():
    invalid_length = random.randint(1, len(INvalid_characters))
    valid_length = random.randint(0, 30-invalid_length)
    character = []
    for i in range(invalid_length):
        index = random.randint(1, len(INvalid_characters))-1
        character.append(INvalid_characters[index])

    for j in range(valid_length):
        index = random.randint(1, len(valid_characters))-1
        character.append(valid_characters[index])

    g_username = ""
    while len(character) != 0:
        index = random.randint(1, len(character)) - 1
        g_username += character[index]
        del character[index]

    return g_username


def generate_username_INvalid_taken():

    # looking thru json file to find already registered usernames
    f = open(filename)
    data = json.load(f)

    try:
        arrayOfUsernames = []
        usernamesTaken = True
        for i in data['accounts']:
            username = i['username']
            arrayOfUsernames.append(username)
        usernameCount = len(arrayOfUsernames)

    except:
        usernamesTaken = False

    if len(arrayOfUsernames) == 0:
        usernamesTaken = False

    f.close()

    if usernamesTaken:
        index = random.randint(1, usernameCount)-1
        g_username = arrayOfUsernames[index]
        return g_username
    else:
        return generate_username_INvalid_chars()


# test below ############################################################
# print(generate_username_INvalid_chars())


# for i in range(10):
#     user = generate_username_INvalid_length()
#     print(str(len(user)) + " :  " + user)


# generate_username_INvalid_taken()

# print(generate_username_INvalid_taken())
