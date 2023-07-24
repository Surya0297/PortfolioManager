Introduction /n
This project is a web application for managing projects and tasks. It provides a user-friendly interface for managers to view and update project details, assign resources to tasks, and track project progress. The application allows managers to create, read, update, and delete projects and tasks, making it a comprehensive tool for project management.

Features
View a list of projects assigned to the manager
View project details, including name, status, start date, and due date
Update the status of a project (e.g., from "Not Started" to "In Progress" or "Completed")
View a list of tasks associated with a selected project
Create new tasks for a project
Update the status of tasks (e.g., mark them as "Completed")
Assign resources to tasks for project execution
Calculate and display project completion progress as a percentage
Installation
Clone the repository:
bash
Copy code
git clone https://github.com/your-username/project-name.git
Navigate to the project directory:
bash
Copy code
cd project-name
Install the required dependencies:
Copy code
npm install
Usage
Run the development server:
arduino
Copy code
npm run serve
Open the application in your web browser:
arduino
Copy code
http://localhost:8080
Sign in using your manager credentials to access the project dashboard.
API Endpoints
The project uses a backend API for data storage and retrieval. Below are the main API endpoints:

/manager/login: POST - Login endpoint for managers. Expects username and password fields in the request body.

/manager/projects/:manager_id: GET - Retrieve a list of projects assigned to a manager.

/projects/:project_id: GET - Retrieve project details by project ID.

/projects/:project_id: PUT - Update project details. Expects project details in the request body.

/tasks/project/:project_id: GET - Retrieve tasks for a specific project.

/tasks/:task_id: PUT - Update task details. Expects task details in the request body.

Technologies Used
Vue.js: Frontend JavaScript framework for building user interfaces.
Node.js: Backend JavaScript runtime environment for running the server.
Express.js: Backend web application framework for creating APIs.
MongoDB: NoSQL database for data storage.
Axios: Promise-based HTTP client for making API requests.
JWT (JSON Web Tokens): For user authentication and authorization.
Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to create a pull request or raise an issue on the GitHub repository.
