#!/usr/bin/env python3

def print_fibonacci(length):
    if length <= 0:
        print([])
        return
    fabinocci_sequence = [0,1]
    while len(fabinocci_sequence) < length:
        next_value = fabinocci_sequence[-1] + fabinocci_sequence[-2]
        fabinocci_sequence.append(next_value)
    
    fabinocci_sequence =fabinocci_sequence[:length]
    print(fabinocci_sequence)


