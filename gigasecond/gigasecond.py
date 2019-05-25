#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 25 2019

@author: cheshirecat12

Exercism exercise: Calculate the moment when someone has lived
                   for 10^9 seconds.
"""
from datetime import datetime, timedelta


def add_gigasecond(moment: datetime) -> datetime:
    """Calculate the moment when someone has lived for 10^9 seconds.

    Args:
        moment (datetime): birth date

    Returns:
        datetime: moment + 1'000'000'000 seconds
    """
    return moment + timedelta(seconds=10**9)
