import random

valid_characters = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
                    "W", "X", "Y", "Z", "_", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "@", ".", "+", "-"]


def generate_username_valid():
    # username length between [1,30] inclusive
    length = random.randint(1, 30)

    generated_username = ""

    for i in range(length):
        # 67 valid characters
        character_index = random.randint(1, len(valid_characters))-1
        generated_username += valid_characters[character_index]

    # print(generated_username)
    return generated_username
