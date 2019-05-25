#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 25 2019

@author: cheshirecat12

Exercism exercise: D&D Character
"""
from random import sample


class Character:

    _abilities = [
        "strength",
        "dexterity",
        "constitution",
        "intelligence",
        "wisdom",
        "charisma",
    ]

    def __init__(self):
        self._set_abilities()

    def ability(self) -> int:
        """Throw 4 dice and remove the smallest value."""
        return sum(sample(range(1, 7), 3))

# Is it equal if we throw 3 dice instead of 4 and remove the smallest value ?
#    def ability(self):
#        pts = sample(range(1, 7), 4)
#        pts.remove(min(pts))
#
#        return sum(pts)

    def _set_abilities(self):
        for ability_ in self._abilities:
            setattr(self, ability_, self.ability())

        self.hitpoints = 10 + modifier(self.constitution)


def modifier(constitution: int) -> int:
    """Modify the character's constitution."""
    return (constitution - 10) // 2
