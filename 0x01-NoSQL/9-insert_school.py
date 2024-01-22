#!/usr/bin/env python3
"""
Module: function that inserts a new document in a collection
"""


def insert_school(mongo_collection, **kwargs):
    """ Inserts a new document in a collection based on kwargs """
    return mongo_collection.insert(kwargs)
