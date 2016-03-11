#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Imports values from task 13 to test equality.

.. hint::

    You can access task_12 data in the following example type:

.. code:: python

    print task_12.FLOATVAL
"""

import task_12
print task_12.DECVAL == task_12.FRACVAL
FRAC_DEC_EQUAL = task_12.DECVAL == task_12.FRACVAL
print task_12.DECVAL != task_12.FLOATVAL
DEC_FLOAT_INEQUAL = task_12.DECVAL != task_12.FLOATVAL
