#!/usr/bin/env python3
"""
A Python function that inserts a new document in a collection based
on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection based on kwargs and
    returns the new document _id
    """
    new_document = mongo_collection.insert_one(kwargs)
    return new_document.inserted_id