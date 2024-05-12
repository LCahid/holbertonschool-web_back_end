#!/usr/bin/env python3
"""Documented module"""
import pymongo


if __name__ == "__main__":
    """Log stats"""
    client = pymongo.MongoClient("mongodb://127.0.0.1:27017")
    collection = client.logs.nginx

    doc_count = collection.estimated_document_count()
    print("{} logs".format(doc_count))

    print("Methods:")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        method_count = collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, method_count))

    status_count = collection.count_documents(
        {
            "method": "GET",
            "path": "/status",
        }
    )

    print("{} status check".format(status_count))
