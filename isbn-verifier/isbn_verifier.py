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
    is_valid_pattern = bool(search(r'^\d-?\d{3}-?\d{5}-?(\d|X)$', isbn))

    final_x = [10] if isbn[-1:] == 'X' else []
    format_isbn = [int(val) for val in sub(r'[A-Z-]', '', isbn)] + final_x

    is_valid_isbn = sum(i*val for i, val in enumerate(format_isbn[::-1], 1)) % 11 == 0

    return is_valid_isbn and is_valid_pattern
