#!/usr/bin/python

def get_even_numbers():
    return [num for num in range(2, 21) if num % 2 == 0]

print(get_even_numbers())
