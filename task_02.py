#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Task_02 module
"""


class CustomError(Exception):
    """
    CustomError exception
    """
    def __init__(self, msg, cause):
        """
        Constructor
        Args:
            msg (String): Exception message
            cause (String): Exception cause
        Attributes:
            message (String): Inherited from superclass
            cause (String): Local instance attribute
        Examples:
        """
        self.message = msg
        self.cause = cause
        Exception.__init__(self)


if __name__ == '__main__':

    MYERR = CustomError('Gouge eyeballs', 'Just because')
    print MYERR.message
    print MYERR.cause
