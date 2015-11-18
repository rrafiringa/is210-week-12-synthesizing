#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03 module"""


def exception_test(arg1, arg2, arg3):
    """
    Exception test function
    Args:
        arg1 (Mixed): A list or tuple
        arg2 (Mixed): An index
        arg3 (Mixed): An index
    Return:
        Boolean: True or False
    Examples:
        >>> exception_test(('a',('trap', 'mode')), 0, 0)
        True
        >>> exception_test(('a',('trap', 'mode')), 0, 'a')
        False
    """

    caught = False
    try:
        arg1[arg2].index(arg3)
    except (TypeError, LookupError):
        caught = True

    return caught
