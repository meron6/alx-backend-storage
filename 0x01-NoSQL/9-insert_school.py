#!/usr/bin/env python3
"""
Task 9. Inserts a new document in a collection based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """Function that inserts a new document in a collection"""
    insert_doc = mongo_collection.insert(kwargs)
    return insert_doc
