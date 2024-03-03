#!/usr/bin/env python3

def double_print(string: str):
    if string:
        print(string)
        print(string)
    else:
        raise ValueError("empty string is not allowed")
