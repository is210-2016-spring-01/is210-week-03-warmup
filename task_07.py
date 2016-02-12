#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Asks the great question."""

import task_06

WORDS = task_06.WORDS

word = 'granaries'

if word in WORDS:
    GRANARIES_EXIST = "Yes!"
else:
    GRANARIES_EXIST = "No!"
