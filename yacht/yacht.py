#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 25 2019

@author: cheshirecat12

Exercism exercise: Score a single throw of dice in Yacht
"""
from typing import List, Callable


def _yacht(dice: List[int]) -> int:
    return [0, 50][len(set(dice)) == 1]


def _main_category(num: int) -> Callable[[List[int]], int]:
    def wrapper(dice: List[int]) -> int:
        return num * len([val for val in dice if val == num])

    return wrapper


def _full_house(dice: List[int]) -> int:
    return [0, sum(dice)][any(dice.count(val) == 3 for val in set(dice))]


def _four_of_a_kind(dice: List[int]) -> int:
    four_time = [val for val in set(dice) if dice.count(val) >= 4]

    return [0, 4*sum(four_time)][bool(four_time)]


_STRAIGHTS = {"small": set(range(1, 6)),
              "big": set(range(2, 7))}


def _straight(straight_type: str) -> Callable[[List[int]], int]:
    def wrapper(dice: List[int]) -> int:
        return [0, 30][set(dice) == _STRAIGHTS[straight_type]]

    return wrapper


def _choice(dice: List[int]) -> int:
    return sum(dice)


YACHT = _yacht
ONES = _main_category(1)
TWOS = _main_category(2)
THREES = _main_category(3)
FOURS = _main_category(4)
FIVES = _main_category(5)
SIXES = _main_category(6)
FULL_HOUSE = _full_house
FOUR_OF_A_KIND = _four_of_a_kind
LITTLE_STRAIGHT = _straight("small")
BIG_STRAIGHT = _straight("big")
CHOICE = _choice


def score(dice: List[int], category: Callable) -> int:
    """Compute the score of a dice throw."""
    return category(dice)
