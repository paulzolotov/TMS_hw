#! /usr/local/bin/python3

def swap_key_val(dict1):
    dict2 = {value: key for key, value in dict1.items()}
    return dict2

a = {'Adam': 'Pinky', 'Sveta': 'Bublik', 'Alex': 'Vivien'}
b = swap_key_val(a)
print(b)
