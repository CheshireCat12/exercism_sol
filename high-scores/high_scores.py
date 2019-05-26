#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 25 2019

@author: cheshirecat12

Exercism exercise: Manage a game player's High Score list.
"""
from typing import List


def latest(scores: List[int]) -> int:
    """Return the last value of the list."""
    return scores[-1]


def personal_best(scores: List[int]) -> int:
    """Return the max value of the scores' list."""
    return max(scores)


def personal_top_three(scores: List[int]) -> List[int]:
    """Return the top three scores of the scores' list"""
    return sorted(scores, reverse=True)[:3]
