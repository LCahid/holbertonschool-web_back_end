#!/usr/bin/env python3
"""Documented module"""
import pymongo


def schools_by_topic(mongo_collection, topic):
	"""Documented function"""
	return [collection for collection in mongo_collection.find(
		{"topics": topic}
    )]
