# User Manager CRUD App Documentation

Welcome to the documentation for the User Manager CRUD (Create, Read, Update, Delete) App. This API allows you to manage user information by performing various operations.

## Table of Contents
- [Request and Response Formats](#request-and-response-formats)
- [Sample API Usage](#sample-api-usage)
- [Known Limitations](#known-limitations)
- [Local Setup and Deployment](#local-setup-and-deployment)
- [UML Diagram](#UML-diagram)

## Request and Response Formats

### Create User: POST /api

**Request Format:**

Request:
 ```
POST /api
Content-Type: application/json
{
    "name": "John Doe"
} 
  ```
Response:
```
{
  "200": "User added successfully.",
  "data": {
    "user_id": "1",
    "name": "John Doe"
  }
}
```
### 2. Retrieve User by ID: GET /api/{user_id}
**Request Format:**

Request:
 ```
GET /api/1
  ```
Response:
```
{
  "200": "User data retrieved successfully.",
  "data": {
    "user_id": "1",
    "name": "John Doe"
  }
}
```
### 3.  Retrieve All Users: GET /api
**Request Format:**

Request:
 ```
GET /api/
  ```
Response:
```
{
  "200": "User data retrieved successfully.",
  "data": {
    "user_id": "1",
    "name": "John Doe"
  },
    {
      "user_id": "2",
      "name": "Jane Doe"
    }

}
```
### 4. Update User by ID: PUT /api/{user_id}
**Request Format:**

Request:
 ```
PUT /api/1
Content-Type: application/json

{
    "name": "Updated Name"
}

  ```
Response:
```
{
  "200": "User data deleted successfully.",
  "data": {
    "user_id": "1",
    "name": "John Doe"
  }
}
```
### 5. Delete User by ID: DELETE /api/{user_id}
**Request Format:**

Request:
 ```
DELETE /api/1

  ```
Response:
```
{
  "200": "User data deleted successfully.",
  "data": {
    "user_id": "1",
    "name": "John Doe"
  }
}
```
### Known Limitations
- There is no authentication or authorization implemented for API endpoints, making them publicly accessible.
- There are only two field in the data, would be more when implemented.

## Local Setup and Deployment

### Prerequisites
Before you begin, ensure you have the following prerequisites installed on your local machine:
- Python 3.7 or higher
- MongoDB ;
[Installing MongoDB](https://www.mongodb.com/docs/manual/administration/install-community/)

### Installation
1. Clone the repository to your local machine:

`git clone https://github.com/your-username/user-manager-crud-app.git`

2. Navigate to the project directory:

`cd user-manager-crud-app`

3. Install the required Python packages using pip:

```pip install -r requirements.txt```

### Configuration
1. Ensure you have MongoDB running locally. You can modify the MongoDB connection details in the *db.py* file if necessary:

``MONGO_DETAILS = "mongodb://localhost:27017"``

2. To start the User Manage Api, run the following command:
   
`python3 app/main.py`

The api will be accessible at http://localhost:8000.

## UML Diagram
![UML Diagram](./path/to/your/uml-diagram.png)





