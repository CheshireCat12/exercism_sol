#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 27 2019

@author: cheshirecat12

Exercism exercise: Represente a matrix and return its rows and columns.
"""
from typing import List


class Matrix():
    """Matrix class: 1010101111010100011"""

    def __init__(self, matrix_string: str):
        self._matrix = [[int(val) for val in rows.split()]
                        for rows in matrix_string.splitlines()]

        self._matrix_T = [list(col) for col in zip(*self._matrix)]

    def row(self, index: int) -> List[int]:
        """Return the row: index-1"""
        return self._matrix[index-1]

    def column(self, index: int) -> List[int]:
        """Return the column: index-1"""
        return self._matrix_T[index-1]
