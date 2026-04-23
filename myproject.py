from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = []
@app.route("/")
def root():
    return {"message": "Time Management AI is running"}
@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()

    new_task = {
        "id": len(tasks) + 1,
        "title": data["title"],
        "deadline": data["deadline"],
        "priority": data["priority"],
        "done": False
    }

    tasks.append(new_task)
    return jsonify(new_task), 201
@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks), 200

@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    data = request.get_json()
    for task in tasks:
        if task["id"] == task_id:
            task["title"] = data.get("title", task["title"])
            task["priority"] = data.get("priority", task["priority"])
            task["done"] =data.get("done", task["done"])
            return jsonify(task), 200
    return jsonify({"error": "Task not found"}), 404
@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return jsonify({"message": "Task deleted"}), 200
        return jsonify({"error": "Task not found"}), 404
if __name__ == "__main__":
    app.run(debug = True)
