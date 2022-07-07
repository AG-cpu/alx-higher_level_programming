#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    rek = list(a_dictionary.keys())[0]
    hgi = a_dictionary[rek]
    for k, v in a_dictionary.items():
        if v > hgi:
            hgi = v
            rek = k
    return (rek)
