#!/usr/bin/env python3
"""
Task 10. Changes all topics of a school document based on the name
"""


def update_topics(mongo_collection, name, topics):
    """Function that changes all topics of a school document
       based on the name"""
    update_top = mongo_collection.update_many({"name": name},
                                              {"$set": {"topics": topics}})
    return update_top
