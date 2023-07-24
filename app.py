from flask import Flask, request, jsonify
from pymongo import MongoClient

from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_bcrypt import Bcrypt
from flask_bcrypt import generate_password_hash
from bson import json_util
from flask_cors import CORS
from flask_mail import Mail, Message


app = Flask(__name__)
CORS(app)
client = MongoClient('mongodb://localhost:27017/')
db = client['portfolio_manager_app']

app.config['JWT_SECRET_KEY'] = 'myjwtauthorisationsceretkeyformanangers1#'  # Change this to a strong secret key
jwt = JWTManager(app)

bcrypt = Bcrypt(app)


# Define the collection names
portfolio_managers_col = db['portfolio_managers']
projects_col = db['projects']
tasks_col = db['tasks']
resources_col = db['resources']  # New collection for resources
task_resources_col = db['task_resources']  # New collection for task-resource associations

# Configure Flask-Mail settings for Mailtrap
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = '782f269672b478'
app.config['MAIL_PASSWORD'] = 'a2f42265481cd5'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)


@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

  # Retrieve the user data from the database based on the provided username
    user = portfolio_managers_col.find_one({'username': username})

    if user and bcrypt.check_password_hash(user['password'], password):
        # If the user exists and the password matches, generate a JWT token
        manager_id = user['manager_id']
        access_token = create_access_token(identity=manager_id)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401

def get_next_manager_id():
    highest_manager = portfolio_managers_col.find_one({}, sort=[('manager_id', -1)])

    if highest_manager:
        last_id = int(highest_manager['manager_id'][1:])  # Extract the numeric part of the last manager ID
        next_id = f"M{str(last_id + 1).zfill(3)}"  # Increment and format the new manager ID
    else:
        next_id = "M001"  # If no managers exist, start with M001

    return next_id


def send_email(username, password):
    try:
        msg = Message('Subject: Hello from Flask-Mail',
                      sender='chauhansurya302@gmail.com.com',
                      recipients=[username])
        msg.body = 'This is a test email sent from Flask using Flask-Mail and Mailtrap .'+password
        mail.send(msg)
        return 'Email sent successfully!'
    except Exception as e:
        return f'Error sending email: {str(e)}'

# API endpoint to create a new Portfolio Manager
@app.route('/portfolio_managers', methods=['POST'])
def create_portfolio_manager():
    data = request.json
     
    existing_manager = portfolio_managers_col.find_one({'username': data['username']})
    if existing_manager:
        return jsonify({"message": "Username is already taken"}), 400

    send_email(data['username'], data['password'])
    # Hash the password before storing it in the database
    hashed_password = generate_password_hash(data['password']).decode('utf-8')
    data['password'] = hashed_password

    # Generate the next auto-incrementing manager ID
    data['manager_id'] = get_next_manager_id()

    # Insert the new manager into the database
    inserted_id = portfolio_managers_col.insert_one(data).inserted_id

    # Return the manager_id along with the MongoDB-generated _id
    
    return jsonify({'message': 'Portfolio Manager created successfully!', '_id': str(inserted_id), 'manager_id': data['manager_id']}), 201

# API endpoint to retrieve all Portfolio Managers
@app.route('/portfolio_managers', methods=['GET'])
def get_all_portfolio_managers():
    # Project only the desired fields (excluding '_id' and 'password')
    managers = list(portfolio_managers_col.find({}, {'_id': 0, 'password': 0}))
    # Serialize the result to JSON using json_util.dumps
    managers_json = json_util.dumps(managers)
    return managers_json, 200

# API endpoint to retrieve a specific Portfolio Manager by ID
@app.route('/portfolio_managers/<string:manager_id>', methods=['GET'])
def get_portfolio_manager(manager_id):
    print(manager_id)
    portfolio_manager = portfolio_managers_col.find_one({'manager_id':manager_id},{'_id': 0, 'password': 0})
    if portfolio_manager:
        return json_util.dumps(portfolio_manager), 200
    return jsonify({'message': 'Portfolio Manager not found!'}), 404

# API endpoint to update a Portfolio Manager

@app.route('/portfolio_managers/<string:manager_id>', methods=['PUT'])
def update_portfolio_manager(manager_id):
    data = request.json
    existing_manager = portfolio_managers_col.find_one({'manager_id': manager_id})

    if existing_manager:
        # If the 'password' field is present in the data, it means a new password is provided
        if 'password' in data:
            # Hash the new password before storing it in the database
            hashed_password = generate_password_hash(data['password']).decode('utf-8')
            data['password'] = hashed_password
        else:
            # If 'password' is not provided, retain the existing hashed password in the data
            data['password'] = existing_manager['password']

        updated_manager = portfolio_managers_col.find_one_and_update(
            {'manager_id': manager_id}, {'$set': data}, return_document=True
        )

        return jsonify({'message': 'Portfolio Manager updated successfully!'}), 200

    return jsonify({'message': 'Portfolio Manager not found!'}), 404

# API endpoint to delete a Portfolio Manager
@app.route('/portfolio_managers/<string:manager_id>', methods=['DELETE'])
def delete_portfolio_manager(manager_id):
    result = portfolio_managers_col.delete_one({'manager_id': manager_id})
    if result.deleted_count > 0:
        return jsonify({'message': 'Portfolio Manager deleted successfully!'}), 200
    return jsonify({'message': 'Portfolio Manager not found!'}), 404
# Example: Retrieving the authenticated username in a protected endpoint
@app.route('/protected_endpoint', methods=['GET'])
@jwt_required()
def protected_endpoint():
    current_user = get_jwt_identity()
    return jsonify({"message": f"Hello, {current_user}!"}), 200

@app.route('/managers/active', methods=['GET'])
def get_active_managers():
    try:
        # Find all managers with the status "active"
        active_managers = list(portfolio_managers_col.find({'status': "Active"}, {'_id': 0}))
        
        if not active_managers:
            return jsonify({'message': 'No active managers found'}), 404
        
        return jsonify(active_managers), 200

    except Exception as e:
        return jsonify({'message': 'Error fetching active managers', 'error': str(e)}), 500


# Projects APIS

def get_next_project_id():
    highest_project = projects_col.find_one({}, sort=[('project_id', -1)])

    if highest_project:
        last_id = int(highest_project['project_id'][1:])  # Extract the numeric part of the last project ID
        next_id = f"P{str(last_id + 1).zfill(3)}"  # Increment and format the new project ID
    else:
        next_id = "P001"  # If no projects exist, start with P001

    return next_id



# API endpoint to create a new Project
@app.route('/projects', methods=['POST'])
def create_project():
    data = request.json

    # Generate the next auto-incrementing project ID
    data['project_id'] = get_next_project_id()

    # Insert the new project into the database
    inserted_id = projects_col.insert_one(data).inserted_id

    # Return the project ID along with the MongoDB-generated _id
    return jsonify({'message': 'Project created successfully!', '_id': str(inserted_id), 'project_id': data['project_id']}), 201

# API endpoint to retrieve all projects
@app.route("/projects", methods=["GET"])
def get_all_projects():
    projects = list(projects_col.find({}, {"_id": 0}))
    return jsonify(projects), 200

# API endpoint to retrieve a specific project by ID
@app.route("/projects/<string:project_id>", methods=["GET"])
def get_project(project_id):
    project = projects_col.find_one({"project_id": project_id}, {"_id": 0})
    if project:
        return jsonify(project), 200
    return jsonify({"message": "Project not found!"}), 404

# API endpoint to update a project
@app.route("/projects/<string:project_id>", methods=["PUT"])
def update_project(project_id):
    data = request.json
    updated_project = projects_col.find_one_and_update(
        {"project_id": project_id}, {"$set": data}, return_document=True
    )
    if updated_project:
        return jsonify({"message": "Project updated successfully!"}), 200
    return jsonify({"message": "Project not found!"}), 404


# API endpoint to delete a project
@app.route("/projects/<string:project_id>", methods=["DELETE"])
def delete_project(project_id):
    result = projects_col.delete_one({"project_id": project_id})
    if result.deleted_count > 0:
        return jsonify({"message": "Project deleted successfully!"}), 200
    return jsonify({"message": "Project not found!"}), 404

# API endpoint to get all projects associated with a specific Portfolio Manager
@app.route('/manager/projects/<string:manager_id>', methods=['GET'])

def get_projects_by_manager(manager_id):
    
   

    # Check if the manager ID is provided in the query parameters
    if not manager_id:
        return jsonify({'message': 'Manager ID not provided in query parameters'}), 400

    # Find all projects with the specified manager ID
    projects = list(projects_col.find({'manager_id': manager_id}, {'_id': 0}))

    # Check if any projects were found
    if not projects:
        return jsonify({'message': 'No projects found for the specified Manager ID'}), 404

    return jsonify(projects), 200

# API endpoint to get all projects with status "completed"
@app.route('/projects/completed', methods=['GET'])
def get_completed_projects():
    # Find all projects with the status "completed"
    projects = list(projects_col.find({'status': 'completed'}, {'_id': 0}))

    # Check if any completed projects were found
    if not projects:
        return jsonify({'message': 'No completed projects found'}), 404

    return jsonify(projects), 200

@app.route('/projects/available', methods=['GET'])
def get_projects_with_no_manager():
    # Find all projects with no manager assigned (managerId is null)
    projects = list(projects_col.find({'manager_id': None}, {'_id': 0}))

    # Check if any projects with no manager assigned were found
    if not projects:
        return jsonify({'message': 'No projects with no manager assigned found'}), 404

    return jsonify(projects), 200

@app.route('/projects/<project_id>/assign-manager', methods=['PUT'])
def assign_manager_to_project(project_id):
    data = request.get_json()

    # Validate the managerId in the request data
    manager_id = data.get('managerId')
    print(manager_id)
    if not manager_id:
        return jsonify({'message': 'Manager ID not provided'}), 400

    # Check if the project exists and has no manager assigned
    project = projects_col.find_one({'project_id':project_id, 'manager_id': None})
    if not project:
        return jsonify({'message': 'Project not found or already has a manager assigned'}), 404

    # Check if the manager exists and is active
    manager = portfolio_managers_col.find_one({'manager_id': manager_id, 'status': 'Active'})
    if not manager:
        return jsonify({'message': 'Invalid or inactive manager ID'}), 400

    # Update the project with the manager's ID
    projects_col.update_one({'project_id': project_id}, {'$set': {'manager_id': manager_id}})

    # Return the updated project data
    project = projects_col.find_one({'project_id': project_id}, {'_id': 0})
    return jsonify({'message': 'Manager assigned successfully', 'project': project}), 200


# Task Apis

def get_next_task_id():
    highest_task = tasks_col.find_one({}, sort=[('task_id', -1)])

    if highest_task:
        last_id = int(highest_task['task_id'][1:])  # Extract the numeric part of the last task ID
        next_id = f"T{str(last_id + 1).zfill(3)}"  # Increment and format the new task ID
    else:
        next_id = "T001"  # If no tasks exist, start with T001

    return next_id

# API endpoint to create a new Task
@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.json
    # Generate the next auto-incrementing task ID
    data['task_id'] = get_next_task_id()

    # Insert the new task into the database
    inserted_id = tasks_col.insert_one(data).inserted_id

    # Return the task_id along with the MongoDB-generated _id
    return jsonify({'message': 'Task created successfully!', '_id': str(inserted_id), 'task_id': data['task_id']}), 201

# API endpoint to update a Task
@app.route('/tasks/update/<string:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.json
    existing_task = tasks_col.find_one({'task_id': task_id})
    print(existing_task)
    if existing_task:
        updated_task = tasks_col.find_one_and_update(
            {'task_id': task_id}, {'$set': data}, return_document=True
        )

        return jsonify({'message': 'Task updated successfully!'}), 200

    return jsonify({'message': 'Task not found!'}), 404

# API endpoint to delete a Task
@app.route('/tasks/<string:task_id>', methods=['DELETE'])
def delete_task(task_id):
    result = tasks_col.delete_one({'task_id': task_id})
    if result.deleted_count > 0:
        return jsonify({'message': 'Task deleted successfully!'}), 200
    return jsonify({'message': 'Task not found!'}), 404

# API endpoint to retrieve a specific Task by ID
@app.route('/tasks/<string:task_id>', methods=['GET'])
def get_task(task_id):
    task = tasks_col.find_one({'task_id': task_id}, {'_id': 0})
    if task:
        return jsonify(task), 200
    return jsonify({'message': 'Task not found!'}), 404

# API endpoint to retrieve all Tasks by Project ID
@app.route('/tasks/project/<string:project_id>', methods=['GET'])
def get_tasks_by_project(project_id):
    tasks = list(tasks_col.find({'project_id': project_id}, {'_id': 0}))
    return json_util.dumps(tasks, default=str), 200

@app.route('/tasks', methods=['GET'])
def get_all_tasks():
    tasks = list(tasks_col.find({}, {'_id': 0}))
    return jsonify(tasks), 200

# Resourcess APIS

# Generate the next auto-incrementing resource ID
def get_next_resource_id():
    highest_resource = resources_col.find_one({}, sort=[('resource_id', -1)])

    if highest_resource:
        last_id = int(highest_resource['resource_id'][1:])  # Extract the numeric part of the last resource ID
        next_id = f"R{str(last_id + 1).zfill(3)}"  # Increment and format the new resource ID
    else:
        next_id = "R001"  # If no resources exist, start with R001

    return next_id

# API endpoint to create a new Resource
@app.route('/resources', methods=['POST'])
def create_resource():
    data = request.json
    # Generate the next auto-incrementing resource ID
    data['resource_id'] = get_next_resource_id()

    # Insert the new resource into the database
    inserted_id = resources_col.insert_one(data).inserted_id

    # Return the resource_id along with the MongoDB-generated _id
    return jsonify({'message': 'Resource created successfully!', '_id': str(inserted_id), 'resource_id': data['resource_id']}), 201

# API endpoint to update a Resource
@app.route('/resources/<string:resource_id>', methods=['PUT'])
def update_resource(resource_id):
    data = request.json
    existing_resource = resources_col.find_one({'resource_id': resource_id})

    if existing_resource:
        updated_resource = resources_col.find_one_and_update(
            {'resource_id': resource_id}, {'$set': data}, return_document=True
        )

        return jsonify({'message': 'Resource updated successfully!'}), 200

    return jsonify({'message': 'Resource not found!'}), 404

# API endpoint to delete a Resource
@app.route('/resources/<string:resource_id>', methods=['DELETE'])
def delete_resource(resource_id):
    result = resources_col.delete_one({'resource_id': resource_id})
    if result.deleted_count > 0:
        return jsonify({'message': 'Resource deleted successfully!'}), 200
    return jsonify({'message': 'Resource not found!'}), 404

# API endpoint to retrieve a specific Resource by ID
@app.route('/resources/<string:resource_id>', methods=['GET'])
def get_resource(resource_id):
    resource = resources_col.find_one({'resource_id': resource_id}, {'_id': 0})
    if resource:
        return jsonify(resource), 200
    return jsonify({'message': 'Resource not found!'}), 404

# API endpoint to retrieve all Resources
@app.route('/resources', methods=['GET'])
def get_all_resources():
    resources = list(resources_col.find({}, {'_id': 0}))
    return jsonify(resources), 200

# API endpoint to assign a resource to a task with status check
@app.route('/tasks/<string:task_id>/assign_resource', methods=['POST'])
def assign_resource_to_task(task_id):
    data = request.json
    resource_id = data.get('resource_id')

    # Check if the resource_id is provided in the request data
    if not resource_id:
        return jsonify({'message': 'Resource ID not provided in the request data'}), 400

    # Check if the task and resource exist in their respective collections
    task = tasks_col.find_one({'task_id': task_id})
    resource = resources_col.find_one({'resource_id': resource_id})

    if not task:
        return jsonify({'message': 'Task not found!'}), 404

    if not resource:
        return jsonify({'message': 'Resource not found!'}), 404

    # Check if the resource is available for assignment
    if resource['status'] != 'available':
        return jsonify({'message': 'Resource is not available for assignment!'}), 400

    # Check if the task_resource association already exists
    existing_association = task_resources_col.find_one({'task_id': task_id, 'resource_id': resource_id})

    if existing_association:
        return jsonify({'message': 'Resource is already assigned to the task!'}), 400

    # Create the association document in the task_resources collection
    association_data = {
        'task_id': task_id,
        'resource_id': resource_id
    }

    inserted_id = task_resources_col.insert_one(association_data).inserted_id

    # Update the task's resource_ids list with the new resource_id
    tasks_col.update_one({'task_id': task_id}, {'$push': {'resource_ids': resource_id}})

    # Update the resource status to "assigned"
    resources_col.update_one({'resource_id': resource_id}, {'$set': {'status': 'assigned'}})

    return jsonify({'message': 'Resource assigned to the task successfully!', '_id': str(inserted_id)}), 200

# API endpoint to unassign a resource from a task
@app.route('/tasks/<string:task_id>/unassign_resource', methods=['POST'])
def unassign_resource_from_task(task_id):
    data = request.json
    resource_id = data.get('resource_id')

    # Check if the resource_id is provided in the request data
    if not resource_id:
        return jsonify({'message': 'Resource ID not provided in the request data'}), 400

    # Check if the task and resource exist in their respective collections
    task = tasks_col.find_one({'task_id': task_id})
    resource = resources_col.find_one({'resource_id': resource_id})

    if not task:
        return jsonify({'message': 'Task not found!'}), 404

    if not resource:
        return jsonify({'message': 'Resource not found!'}), 404

    # Check if the task_resource association exists
    existing_association = task_resources_col.find_one({'task_id': task_id, 'resource_id': resource_id})

    if not existing_association:
        return jsonify({'message': 'Resource is not assigned to the task!'}), 400

    # Remove the association document from the task_resources collection
    task_resources_col.delete_one({'task_id': task_id, 'resource_id': resource_id})

    # Update the task's resource_ids list to remove the unassigned resource_id
    tasks_col.update_one({'task_id': task_id}, {'$pull': {'resource_ids': resource_id}})

    return jsonify({'message': 'Resource unassigned from the task successfully!'}), 200


if __name__ == '__main__':
    app.run(debug=True)

