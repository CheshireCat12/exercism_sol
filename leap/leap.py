#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 27 2019

@author: cheshirecat12

Exercism exercise: Check if the given year is a leap year
"""


def is_leap_year(year: int) -> bool:
    """Check if the given year is a leap year."""
    return year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)
