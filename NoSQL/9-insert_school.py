#!/usr/bin/env python3
"""Insert all documents"""
import pymongo


def insert_school(mongo_collection, **kwargs):
	"""Insert doc function"""
	if len(kwargs) == 0:
		return None
	return mongo_collection.insert(kwargs)
