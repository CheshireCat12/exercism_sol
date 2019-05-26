#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 26 2019

@author: cheshirecat12

Exercism exercise: Translate RNA sequences into proteins.
"""
from re import findall

CONDONS_PROTEINS = [
    ("AUG", "Methionine"),
    ("UUU,UUC", "Phenylalanine"),
    ("UUA,UUG", "Leucine"),
    ("UCU,UCC,UCA,UCG", "Serine"),
    ("UAU,UAC", "Tyrosine"),
    ("UGU,UGC", "Cysteine"),
    ("UGG", "Tryptophan"),
    ("UAA,UAG,UGA", "STOP")
]
CONDONS_TO_PROTEINS = {condon: protein
                       for condons, protein in CONDONS_PROTEINS
                       for condon in condons.split(",")}


def proteins(strand: str) -> str:
    """Convert the strand rna to proteins."""
    proteins = []

    for condon in findall(r'\w{3}', strand):
        protein = CONDONS_TO_PROTEINS[condon]
        if protein == "STOP":
            return proteins

        proteins.append(protein)
    return proteins
