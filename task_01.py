#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Task 01 module
Create Exception classes
"""


class BaseError(Exception):
    """
    BaseError class
    Args:
        Inherited from Exception superclass
    Attributes:
        Inherited from Exception superclass
    Examples:
        >>> raise BaseError('Helloooooooo')
        Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
        BaseError: Helloooooooo
    """
    pass


class StringError(BaseError, TypeError):
    """
    StringError class
    Args:
        Inherited from superclasses
    Attributes:
        Inherited from superclasses
    Examples:
        >>> raise StringError('There\'s dust on my string!')
        Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
        StringError: There's dust on my string!
    """
    pass


class NumberError(BaseError, TypeError):
    """
    NumberError class
    Args:
        Inherited from superclasses
    Attributes:
        Inherited from superclasses
    Examples:
        >>> raise NumberError('NaN')
        Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
        NumberError: NaN
    """
    pass


class NonZeroError(NumberError):
    """
    NonZeroError class
    Args:
        Inherited from superclasses
    Attributes:
        Inherited from superclasses
    Examples:
        raise NonZeroError('Not a zero, but a hero')
        Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
        NonZeroError: Not a zero, but a hero
    """
    pass


if __name__ == '__main__':
    print issubclass(StringError, IOError)
    print issubclass(NumberError, BaseError)