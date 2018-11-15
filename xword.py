#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Crossword Solver Program"""

__author__ = "tgentry300"

import re


def find_matches(input_string, words):
    new_string = input_string.replace(' ', r'\w')

    new_words = []
    for word in words:
        if len(word) == len(input_string):
            new_words.append(word)

    regex = re.compile(r'{}'.format(new_string))
    match_list = filter(regex.match, new_words)
    print '\n'.join(match_list) + '\n'


def main():
    with open('dictionary.txt') as f:
        words = f.read().split()

    test_word = raw_input(
        """Please enter a word to solve.
Use spaces to signify unknown letters: """).lower()

    find_matches(test_word, words)


if __name__ == '__main__':
    main()
