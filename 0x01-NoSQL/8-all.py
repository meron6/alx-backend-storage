#!/usr/bin/env python3
"""
Task 8: List All Documents in Python
"""


def list_all(mongo_collection):
    """Function to list all documents in a collection."""
    documents = mongo_collection.find()
    return list(documents) if documents.count() > 0 else []
