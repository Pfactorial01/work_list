from flask import Flask, jsonify, request, make_response
from bson.objectid import ObjectId
from flask_restful import Api, Resource
import pymongo

""" Database connection """
connection_url = "mongodb+srv://pfactorial:new_pass*123@cluster0.leidy8g.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(connection_url)
database = client.get_database("work_list")
tasks = database.tasks


""" flask app initialization """
app = Flask(__name__)
api = Api(app)
app.config["SECRET_KEY"] = "thisisthesecretkey"


class Task(Resource):
    def get(self):
        """get all tasks resource"""
        task_list = tasks.find({})
        output = []

        for task in task_list:
            data = {}
            data["id"] = str(task["_id"])
            data["task_name"] = task["task_name"]
            data["description"] = task["description"]
            data["status"] = task["status"]
            output.append(data)
        if not output:
            return make_response({"message": "No tasks to display"}, 404)
        return output

    def post(self):
        """create task resource"""
        data = request.get_json(silent=True)
        if not data:
            return make_response(
                {"message": "Task details required, JSON content not detected"}, 400
            )
        try:
            new_task = {
                "task_name": data["task_name"],
                "description": data["description"],
                "status": "uncompleted",
            }
        except:
            return jsonify({"message": "task_name or description missing"})
        tasks.insert_one(new_task)
        return jsonify({"message": "Task added succesfully"})


api.add_resource(Task, "/tasks")


class Single_Task(Resource):
    def get(self, task_id):
        """get one task resource"""
        try:
            task = tasks.find_one({"_id": ObjectId(task_id)})
        except:
            return jsonify({"message": "invalid task_id"})
        if not task:
            return make_response({"message": "task not found"}, 404)

        output = {}
        output["id"] = str(task["_id"])
        output["task_name"] = task["task_name"]
        output["description"] = task["description"]
        output["status"] = task["status"]

        return jsonify({"Task": output})

    def put(self, task_id):
        """update one task resource"""
        try:
            task = tasks.find_one({"_id": ObjectId(task_id)})
        except:
            return jsonify({"message": "invalid task_id"})
        data = request.get_json(silent=True)
        if not data:
            return make_response(
                "Task details required, JSON content not detected", 400
            )

        if data.get("task_name"):
            tasks.find_one_and_update(
                {"_id": ObjectId(task_id)},
                {"$set": {"task_name": data["task_name"]}},
            )
        if data.get("description"):
            tasks.find_one_and_update(
                {"_id": ObjectId(task_id)},
                {"$set": {"description": data["description"]}},
            )
        return jsonify({"message": "task updated succesfully"})

    def delete(self, task_id):
        """delete one task resource"""
        try:
            task = tasks.find_one({"_id": ObjectId(task_id)})
        except:
            return jsonify({"message": "invalid task_id"})
        if not task:
            return make_response({"message": "Task not found"}, 404)

        tasks.delete_one({"_id": ObjectId(task_id)})
        return jsonify({"message": "task deleted succesfully"})

    def patch(self, task_id):
        """mark task as completed or uncompleted resource"""
        data = request.get_json(silent=True)
        if not data:
            return make_response(
                {"message": "Task details required, JSON content not detected"}, 400
            )
        try:
            task = tasks.find_one({"_id": ObjectId(task_id)})
        except:
            return jsonify({"message": "invalid task_id"})
        if not task:
            return make_response({"message": "Task not found"}, 404)
        if data.get("status") == "completed":
            tasks.find_one_and_update(
                {"_id": ObjectId(task_id)},
                {"$set": {"status": "completed"}},
            )
            return jsonify({"message": "task marked as completed"})
        if data.get("status") == "uncompleted":
            tasks.find_one_and_update(
                {"_id": ObjectId(task_id)},
                {"$set": {"status": "uncompleted"}},
            )
            return jsonify({"message": "task marked as uncompleted"})


api.add_resource(Single_Task, "/task/<string:task_id>")


if __name__ == "__main__":
    app.run(debug=True)
