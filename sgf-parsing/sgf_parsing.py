#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 25 2019

@author: cheshirecat12

Exercism exercise: Parse a smart game format.
"""
import re
from collections import defaultdict
from string import ascii_uppercase


class SgfTree():
    def __init__(self, properties=None, children=None):
        self.properties = properties or {}
        self.children = children or []

    def __eq__(self, other):
        if not isinstance(other, SgfTree):
            return False
        for k, v in self.properties.items():
            if k not in other.properties:
                return False
            if other.properties[k] != v:
                return False
        for k in other.properties.keys():
            if k not in self.properties:
                return False
        if len(self.children) != len(other.children):
            return False
        for a, b in zip(self.children, other.children):
            if a != b:
                return False
        return True

    def __ne__(self, other):
        return not self == other


def _format_properties(properties):
    props = defaultdict(list)

    tmp_node = ""
    for (node, prop) in properties:
        if node in ascii_uppercase:
            tmp_node = node

        props[tmp_node].append(prop)

    return props


def parse(input_string: str) -> SgfTree:
    empty_patt = r'\(;.*\)'
    node_patt = r'(;|\])([A-Z])\['
    properties_patt = r'(?=([A-Z]|\])\[([a-zA-Z])\])'

    default_patt = re.search(empty_patt, input_string)

    nodes = re.findall(node_patt, input_string)
    properties = re.findall(properties_patt, input_string)

    if not default_patt or (default_patt.group(0) != '(;)' and not nodes):
        raise ValueError("Input invalid")

    f_properties = _format_properties(properties)

    if not f_properties:
        return SgfTree()

    children = []
    other_prop = []
    for (val, node) in nodes[1:]:
        if val == ";":
            children.append(SgfTree({node: f_properties[node]}))
        else:
            other_prop.append(node)

    (_, root_node), *_ = nodes
    root_prop = {node: f_properties[node]
                 for node in [root_node] + other_prop}
    root = SgfTree(properties=root_prop, children=children)

    return root
