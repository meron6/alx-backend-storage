#!/usr/bin/env python3
from pymongo import MongoClient

# Connect to the MongoDB server
client = MongoClient()
db = client.logs
collection = db.nginx

# Count the total number of logs
total_logs = collection.count_documents({})

# Count the number of logs for each HTTP method
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
method_counts = {method: collection.count_documents({"method": method}) for method in methods}

# Count the number of GET requests to /status
status_check_count = collection.count_documents({"method": "GET", "path": "/status"})

# Print the results
print(f"{total_logs} logs")
print("Methods:")
for method in methods:
    print(f"\tmethod {method}: {method_counts[method]}")
print(f"{status_check_count} status check")
