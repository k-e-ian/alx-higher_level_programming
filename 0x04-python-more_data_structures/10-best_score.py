#!/usr/bin/python3
def best_score(a_dictionary):
    score = ""
    big = 0
    if a_dictionary:
        for x, y in a_dictionary.items():
            if x > big:
                big = y
                score = x
        return score
    else:
        return None
