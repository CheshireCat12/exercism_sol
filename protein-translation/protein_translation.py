#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 26 2019

@author: cheshirecat12

Exercism exercise: Translate RNA sequences into proteins.
"""
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
LENGTH_CONDON = 3
CONDONS_TO_PROTEINS = {condon: protein
                       for condons, protein in CONDONS_PROTEINS
                       for condon in condons.split(",")}


def proteins(strand: str) -> str:
    """Convert the strand rna to proteins."""
    proteins = []

    for idx in range(0, len(strand)-LENGTH_CONDON+1, LENGTH_CONDON):
        condon = strand[idx:idx+LENGTH_CONDON]
        protein = CONDONS_TO_PROTEINS[condon]
        if protein == "STOP":
            return proteins

        proteins.append(protein)
    return proteins
