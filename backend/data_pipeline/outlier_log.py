"""
outlier_log.py - Exclusion tracking
============================================


Accumulates every row removed by the cleaning rules so the pipeline can
publish a transparency report at the end.

Motivation:
    The assignment brief requires that we keep a log of excluded or
    suspicious records. Reviewers should be able to understand exactly
    which rows were dropped and why without reading the cleaning code.
"""
