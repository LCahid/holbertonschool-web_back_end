#!/usr/bin/env python3
"""List all documents"""
import pymongo


def list_all(collection):
	"""List doc function"""
	if not collection:
		return []
	return list(collection.find())
