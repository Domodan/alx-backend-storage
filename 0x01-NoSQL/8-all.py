#!/usr/bin/env python3
"""
Module: Function that lists all documents in a collection
"""


def list_all(mongo_collection):
    """ Function that lists all documents in a collection """
    return [document for document in mongo_collection.find()]
