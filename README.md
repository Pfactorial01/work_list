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
 - To create task
 Send POST request with body { "task_name
