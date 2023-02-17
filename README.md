# work_list
A to-do list built with flask and mongodb

## Prerequisites
- Python 3.9.0

## Installation
```
pip install requirements.txt
```
### Run Server
```
flask run
```

### Build Docker Image
 ```
 docker build work_flow .
 ```
 
 ### Run Docker Container
 ```
 docker run work_flow
 ```
 
 ### API USAGE
 - To create task,
 Send POST request with body { "task_name": "write edge cases", "description": "checkout code base" } to localhost:PORT/tasks
 
 - To get all tasks,
 Send GET request to localhost:PORT/tasks
  
 - To get one task,
Send GET request to localhost:PORT/task/task_id
 
 - To delete a task,
 Send DELETE request to localhost:PORT/task/task_id
 
 - To update a task,
 Send PUT request with body { "task_name": "write edge cases", "description": "checkout code base" } to localhost:PORT/task/task_id
 
 - To mark task as complete,
 Send PATCH request with body { "status": "completed" } to localhost:PORT/task/task_id
 
  - To mark task as incomplete,
 Send PATCH request with body { "status": "uncompleted" } to localhost:PORT/task/task_id
