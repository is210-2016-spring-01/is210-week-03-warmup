#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Imports values from task 13 to test equality.

.. hint::

    You can access task_12 data in the following example type:

.. code:: python

    print task_12.FLOATVAL
"""

from task_12 import FRACVAL, DECVAL
from task_12 import FLOATVAL

FRAC_DEC_EQUAL = DECVAL == FRACVAL

DEC_FLOAT_INEQUAL = DECVAL == FLOATVAL
