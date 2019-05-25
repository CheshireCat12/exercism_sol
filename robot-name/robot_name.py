#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 25 2019

@author: cheshirecat12

Exercism exercise: Armstrong number is number where the sum
                   of its own digits each raised to the power
                   of the number of digits.
"""
from string import ascii_uppercase as letters
from random import choice, sample


class Robot():
    """A robot factory, which create robot with random name."""

    _names = []

    def __init__(self):
        self.create_rand_name()

    def _generate_new_name(self):
        first_name = ''.join(sample(letters, 2))
        second_name = str(choice(range(100, 1000)))

        return first_name + second_name

    def create_rand_name(self):
        """Create a new random name not already assigned."""
        self.name = self._generate_new_name()

        while self.name in self._names:
            self.name = self._generate_new_name()

        self._names.append(self.name)

    def reset(self):
        """Generate a new robot name."""
        self.create_rand_name()
