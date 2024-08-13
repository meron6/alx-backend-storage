#!/usr/bin/env python3
"""Log stats
"""
from pymongo import MongoClient

if __name__ == "__main__":
    # Connect to MongoDB server
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    path = "path"
    status = "/status"

    # Print the number of logs
    print(f"{nginx_collection.count_documents({})} logs")
    print("Methods:")

    # Print the number of logs for each method
    for value in methods:
        count = nginx_collection.count_documents({"method": value})
        print(f"\tmethod {value}: {count}")
    
    # Print the number of GET requests to /status
    print(f"{nginx_collection.count_documents({'method': 'GET', path: status})} status check")
