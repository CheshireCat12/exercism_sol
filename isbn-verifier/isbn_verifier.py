#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 27 2019

@author: cheshirecat12

Exercism exercise: An ISBN-10 verificator
"""
from re import sub, search


def verify(isbn: str) -> bool:
    """Check if the given isbn code is valid."""
    final_x = [10] if isbn[-1:] == 'X' else []
    format_isbn = [int(val) for val in sub(r'[A-Z-]', '', isbn)] + final_x

    valid_isbn = sum(i*val
                     for i, val in enumerate(format_isbn[::-1], 1)) % 11 == 0

    # Not to do the test at the return or if I should write a test
    # at the beginning of the function to return directly if the pattern
    # doesn't match.
    valid_pattern = bool(search(r'^\d-?\d{3}-?\d{5}-?(\d|X)$', isbn))

    return valid_isbn and valid_pattern
