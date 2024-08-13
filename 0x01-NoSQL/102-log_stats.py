#!/usr/bin/env python3
"""Log stats - new version
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
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")
    
    # Print the number of GET requests to /status
    print(f"{nginx_collection.count_documents({'method': 'GET', path: status})} status check")

    # Print the top 10 most frequent IPs
    print("IPs:")
    top_ips = nginx_collection.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])
    for ip in top_ips:
        print(f"\t{ip['_id']}: {ip['count']}")
