#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Using simple numeric types."""


from fractions import Fraction
import decimal

INTVAL = 1
FLOATVAL = 0.1
DECVAL = decimal.Decimal('1.0')/decimal.Decimal('10.0')
FRACVAL = Fraction(1, 10)
print INTVAL
print FLOATVAL
print DECVAL
print FRACVAL
