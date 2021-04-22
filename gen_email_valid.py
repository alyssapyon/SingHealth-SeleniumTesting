import random

# user @ mailserver . domain
# g_user + "@" + g_mailserver + "." + g_domain

validchar_user = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
                  "W", "X", "Y", "Z", "_", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "+", "-", "~"]

validchar_mailserver = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
                        "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

validchar_domain = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
                    "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def generate_email_valid():
    # max email length is 254 chars

    # DOMAIN
    # length can be 2 to 61
    domain_length = random.randint(2, 61)
    g_domain = ""
    for i in range(domain_length):
        index_char = random.randint(1, len(validchar_domain)) - 1
        g_domain += validchar_domain[index_char]

    # MAILSERVER
    # max length for "mailserver.domain" is 63
    mailserver_maxlength = 62-len(g_domain)
    mailserver_length = random.randint(1, mailserver_maxlength)

    g_mailserver = ""

    for i in range(mailserver_length):
        index_char = random.randint(1, len(validchar_mailserver)) - 1
        newchar = validchar_mailserver[index_char]
        if (len(g_mailserver) > 0) and (g_mailserver[-1] in ["-", "."]) and (newchar in ["-", "."]):
            continue
        g_mailserver += newchar

    while g_mailserver[0] in [".", "_", "-"]:
        g_mailserver = g_mailserver[1:]

    while g_mailserver[-1] in [".", "_", "-"]:
        g_mailserver = g_mailserver[:-1]

    # USER
    user_maxlength = 254 - len(g_domain) - len(g_mailserver) - 1
    user_length = random.randint(1, user_maxlength)

    g_user = ""

    for i in range(user_length):
        index_char = random.randint(1, len(validchar_user)) - 1
        newchar = validchar_user[index_char]
        if (len(g_user) > 0) and (g_user[-1] in ["-", "."]) and (newchar in ["-", "."]):
            continue
        g_user += newchar

    while g_user[0] in [".", "_"]:
        g_user = g_user[1:]

    while g_user[-1] in [".", "_"]:
        g_user = g_user[:-1]

    # ASSEMBLE EMAIL
    g_email = g_user + "@" + g_mailserver + "." + g_domain

    # print(g_email)
    # print()
    return g_email
