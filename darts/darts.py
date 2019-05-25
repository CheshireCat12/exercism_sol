#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 25 2019

@author: cheshirecat12

Exercism exercise: Write a function that returns the earned points
                   in a single toss of a Darts game.
"""
_TARGET = [
    (1, 10),
    (25, 5),
    (100, 1),
]


def score(x: float, y: float) -> int:
    """Compute the earned points of a single toss of a dart game.

    Args:
        x (float): x coordinate of the dart
        y (float): y coordinate of the dart

    Returns:
        int: the score of the toss
    """
    land = x**2 + y**2

    for (rad, pts) in _TARGET:
        if land <= rad:
            return pts

    return 0
