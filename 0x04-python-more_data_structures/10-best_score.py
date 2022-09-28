#!/usr/bin/python3
def best_score(a_dictionary):
    score = list(a_dictionary.keys())[0]
    big = a_dictionary[score]
    if a_dictionary:
        for x, y in a_dictionary.items():
            if x > big:
                big = y
                score = x
        return score
    else:
        return None
