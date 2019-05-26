#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 25 2019

@author: cheshirecat12

Exercism exercise: Given a DNA strand return its RNA transcription.
"""

_dna_nucleotides = "GCTA"
_rna_nucleotides = "CGAU"

_dna_to_rna = {dna: rna for dna, rna
               in zip(_dna_nucleotides, _rna_nucleotides)}


def to_rna(dna_strand: str) -> str:
    """Transcript the given dna strand into a rna strand."""
    return "".join(_dna_to_rna[nucleotide] for nucleotide in dna_strand)
