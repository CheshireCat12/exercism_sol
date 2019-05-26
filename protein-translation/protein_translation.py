#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 26 2019

@author: cheshirecat12

Exercism exercise: Translate RNA sequences into proteins.
"""
from re import findall
from itertools import takewhile

CODONS_PROTEINS = [
    ("AUG", "Methionine"),
    ("UUU,UUC", "Phenylalanine"),
    ("UUA,UUG", "Leucine"),
    ("UCU,UCC,UCA,UCG", "Serine"),
    ("UAU,UAC", "Tyrosine"),
    ("UGU,UGC", "Cysteine"),
    ("UGG", "Tryptophan"),
    ("UAA,UAG,UGA", "STOP")
]
CODONS_TO_PROTEINS = {codon: protein
                      for codons, protein in CODONS_PROTEINS
                      for codon in codons.split(",")}


def _stop_condition(codon):
    return CODONS_TO_PROTEINS[codon] != "STOP"


def proteins(strand: str) -> str:
    """Convert the strand rna to proteins."""
    result = [CODONS_TO_PROTEINS[codon]
              for codon in takewhile(_stop_condition,
                                     findall(r'\w{3}', strand))]

    return result
