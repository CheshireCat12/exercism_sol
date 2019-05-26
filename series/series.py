#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 25 2019

@author: cheshirecat12

Exercism exercise: Manage a game player's High Score list.
"""
from typing import List


def slices(series: str, length: int) -> List[str]:
    """Slice the series given in parameters in slice of the given length."""
    if not 0 < length <= len(series):
        raise ValueError(f"Caution: the slicing length {length} "
                         "is not correct!")

    return [series[idx:idx+length]
            for idx in range(len(series)-length+1)]
