#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 2019

@author: cheshirecat12

Exercism exercise: Clean up user-entered phone numbers
                   so that they can be sent SMS messages.
"""
from re import sub


class Phone():

    def __init__(self, phone_number: str):
        self.number = sub(r'[a-zA-Z -\.\(\)]', '', phone_number)
        self.area_code = self.number[:3]
        self.exchange_code = self.number[3:]

    def _not_begins_by(not_accepted=["0", "1"]):
        def middle(func):
            def wrapper(self, phone_num):
                if any(phone_num.startswith(val) for val in not_accepted):
                    raise ValueError(f"Caution, the {func.__name__} begings "
                                     "with an invalid character!")
                func(self, phone_num)
            return wrapper
        return middle

    @property
    def area_code(self) -> str:
        return self.__area_code

    @area_code.setter
    @_not_begins_by(["0", "1"])
    def area_code(self, area: str):
        self.__area_code = area

    @property
    def exchange_code(self) -> str:
        return self.__exchange_code

    @exchange_code.setter
    @_not_begins_by(["0", "1"])
    def exchange_code(self, exchange: str):
        self.__exchange_code = exchange

    @property
    def number(self) -> str:
        return self.__number

    @number.setter
    def number(self, phone_number: str):
        if phone_number.startswith("1"):
            phone_number = phone_number[1:]

        if len(phone_number) != 10:
            raise ValueError("No valid phone number!")

        self.__number = phone_number

    def pretty(self) -> str:
        return (f"({self.area_code}) {self.exchange_code[:3]}-"
                f"{self.exchange_code[3:]}")
