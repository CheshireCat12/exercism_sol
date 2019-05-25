#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 25 2019

@author: cheshirecat12

Exercism exercise: Resistor color duo
"""

_band_colors = [
    'black',
    'brown',
    'red',
    'orange',
    'yellow',
    'green',
    'blue',
    'violet',
    'grey',
    'white'
]


def value(colors: list) -> int:
    return int("".join(str(_band_colors.index(color))
                       for color in colors))
