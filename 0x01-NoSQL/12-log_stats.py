#!/usr/bin/env python3
"""
Provide some stats about Nginx logs stored in MongoDB.
Database: logs, Collection: nginx, Display same as example
First line: x logs, x number of documents in this collection
Second line: Methods
5 lines with method = ["GET", "POST", "PUT", "PATCH", "DELETE"]
One line with method=GET, path=/status
"""
from pymongo import MongoClient

METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]

def log_stats(mongo_collection, option=None):
    """
    Provide some stats about Nginx logs stored in MongoDB.
    """
    if option:
        # Count documents matching the specific method
        value = mongo_collection.count_documents({"method": option})
        print(f"\tmethod {option}: {value}")
        return

    # Count total documents in the collection
    total_logs = mongo_collection.count_documents({})
    print(f"{total_logs} logs")

    # Print stats for each method
    print("Methods:")
    for method in METHODS:
        log_stats(mongo_collection, method)

    # Count documents with method=GET and path=/status
    status_check = mongo_collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check} status check")

if __name__ == "__main__":
    # Connect to MongoDB and access the collection
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    log_stats(nginx_collection)
