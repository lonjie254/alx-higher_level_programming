#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """
    Prevent the user from creating new instance attributes
    except if the new attribute is called 'first_name'.
    """

    __slots__ = ["first_name"]
