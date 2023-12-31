# stg2-user-manage-app

## USER MANAGE APP
Welcome to the USER MANAGE CRUD(Create, Read, update and Delete) App! This api allows you to create, retrieve, update, and delete user information.

### Getting Started
Local machine setup, follow this steps to run on your local machine

#### Prerequisites
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


## API Endpoints
The User Manager CRUD App provides the following API endpoints
You can use tools like curl, Postman, or Swagger UI(/docs) to interact with these endpoints. Example request bodies can be found below

### 1. Create User: POST /api
This endpoint allows you to create a new user by sending a POST request with user data in the request body, entries are assigned user id for further/future manipulation.

### 2. Retrieve User by ID: GET /api/{user_id}
This endpoint retrieves user data by specifying the user_id in the URL.

### 3.  Retrieve All Users: GET /api
This endpoint retrieves a list of all users in the database.

### 4. Update User by ID: PUT /api/{user_id}
This endpoint allows you to update user data by specifying the user_id in the URL and providing the updated user data in the request body.

### 5. Delete User by ID: DELETE /api/{user_id}
This endpoint allows you to delete a user by specifying the user_id in the URL.


For more detailed requests and response format, see the DOCUMENTATION.md





