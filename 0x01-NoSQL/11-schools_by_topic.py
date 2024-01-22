#!/usr/bin/env python3
"""
Module: Function that returns the list of school having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of schools having a specific topic
    """
    results = mongo_collection.find({ "topics": topic })
    return list(results)
