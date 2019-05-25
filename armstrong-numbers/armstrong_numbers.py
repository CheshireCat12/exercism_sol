#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 25 2019

@author: cheshirecat12

Exercism exercise: Armstrong number is number where the sum
                   of its own digits each raised to the power
                   of the number of digits.
"""


def is_armstrong_number(number: int) -> bool:
    """Check if the given number is an armstrong number.

    Args:
        number (int): number to check

    Returns:
        bool: The return value. True for success, False otherwise.
    """
    power = len(str(number))
    return number == sum(int(val)**power for val in str(number))
