#!/usr/bin/env python3
"""
Task 11. Returns the list of school having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """Function that returns the list of school having a
       specific topic"""
    find_topic = mongo_collection.find({"topics": topic})
    return find_topic
