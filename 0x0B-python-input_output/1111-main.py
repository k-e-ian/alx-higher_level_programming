#!/usr/bin/python3
write_file = __import__('1-write_file').write_file

nb_characters = write_file("my_fisr
number_of_lines = __import__('1-number_of_lines').number_of_lines

filename = "my_file_0.txt"
nb_lines = number_of_lines(filename)
print("{} has {:d} lines".format(filename, nb_lines))
