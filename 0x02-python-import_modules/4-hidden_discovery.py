#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    names = dir(hidden_4)
    for index in range(len(names)):
        if (names[index][0] != "_"):
            print("{:s}".format(names[index]))
