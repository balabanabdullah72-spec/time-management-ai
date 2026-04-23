import urllib.request
import json

# Create a task
data = {
    "title": "Study Flask",
    "deadline": "2024-04-25",
    "priority": "high"
}

req = urllib.request.Request(
    "http://127.0.0.1:5000/tasks",
    data=json.dumps(data).encode(),
    headers={"Content-Type": "application/json"},
    method="POST"
)
response = urllib.request.urlopen(req)
created = json.loads(response.read())
print("CREATED:", created)

# Delete the task we just created
task_id = created["id"]
req2 = urllib.request.Request(
    f"http://127.0.0.1:5000/tasks/{task_id}",
    method="DELETE"
)
response2 = urllib.request.urlopen(req2)
print("DELETED:", json.loads(response2.read()))