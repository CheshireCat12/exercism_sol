#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 25 2019

@author: cheshirecat12

Exercism exercise: Resistor color
"""


def color_code(color: str) -> int:
    return colors().index(color)


def colors() -> list:
    result = [
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
    return result
