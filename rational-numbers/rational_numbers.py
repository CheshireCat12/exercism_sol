#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 26 2019

@author: cheshirecat12

Exercism exercise: Write a class for rational number.
"""
from math import gcd
import operator


class Rational():
    def __init__(self, numer, denom):
        gcd_numer_denom = gcd(numer, denom)

        if denom < 0:
            numer *= -1
            denom *= -1

        self.numer = numer // gcd_numer_denom
        self.denom = denom // gcd_numer_denom

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return f'{self.numer}/{self.denom}'

    def _add_sub_op(self, other, op):
        new_numer = op(self.numer * other.denom, self.denom * other.numer)
        new_denom = self.denom * other.denom
        return Rational(new_numer, new_denom)

    def __add__(self, other):
        return self._add_sub_op(other, operator.add)

    def __sub__(self, other):
        return self._add_sub_op(other, operator.sub)

    def __mul__(self, other):
        return Rational(self.numer * other.numer, self.denom * other.denom)

    def __truediv__(self, other):
        return Rational(self.numer * other.denom, self.denom * other.numer)

    def __abs__(self):
        return Rational(abs(self.numer), abs(self.denom))

    def __pow__(self, power):
        power = abs(power)
        return Rational(self.numer**power, self.denom**power)

    def __rpow__(self, base):
        return (base**self.numer)**(1/self.denom)
