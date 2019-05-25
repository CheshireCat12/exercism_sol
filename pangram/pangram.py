#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 25 2019

@author: cheshirecat12

Exercism exercise: Pangram, determine if the sentence use all letters at
                   least once.
"""
from re import sub

NB_ALPHABET_LETTERS = 26


def is_pangram(sentence: str) -> bool:
    """Check if the given sentence uses at least once all letters."""
    formated_sentence = sub(r'[\d_ "\.]', '', sentence).lower()
    return len(set(formated_sentence)) == NB_ALPHABET_LETTERS
