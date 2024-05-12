#!/usr/bin/env python3
"""Documented module"""
import pymongo


def update_topics(mongo_collection, name, topics):
	"""Documented function"""
	mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
