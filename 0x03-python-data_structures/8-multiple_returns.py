#!/usr/bin/python3
def multiple_returns(sentence):
        length = len(sentence)
        tuple = ()
        if length == 0:
                tuple = 0, None
        else:
                tuple = length, sentence[0]
        return tuple 