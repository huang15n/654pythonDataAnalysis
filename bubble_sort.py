"""
This is pure python implementation of bubble sort algorithm

For doctests run following command:
python -m doctest -v bubble_sort.py
or
python3 -m doctest -v bubble_sort.py

For manual testing run:
python bubble_sort.py
"""

from __future__ import print_function


def bubble_sort(collection):
    """Pure implementation of bubble sort algorithm in Python

    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending

    Examples:
    >>> bubble_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]

    >>> bubble_sort([])
    []

    >>> bubble_sort([-2, -5, -45])
    [-45, -5, -2]
    """
    length = len(collection)
    for i in range(length):
        for j in range(length-1):
            if collection[j] > collection[j+1]:
                collection[j], collection[j+1] = collection[j+1], collection[j]

    return collection



