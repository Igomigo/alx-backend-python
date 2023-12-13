#!/usr/bin/env python3
""" Script that runs the to_kv function """
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, Union[int, float]]:
    """ returns a tuple with str as the first element and float
    or int as second element of the tuple"""
    return (k, v)
