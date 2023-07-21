<template>
    <div class="task-list-container">
      
      <table class="task-list-table">
        <!-- Table header -->
        <thead>
            <tr>
                <th colspan="8" align="center">
                    <h1>Task List</h1>
                </th>
            </tr>
          <tr>
            <th>Task ID</th>
            <th>Name</th>
            <th>Description</th>
            <th>Start Date</th>
            <th>Due Date</th>
            <th>Status</th>
            <th>Project ID</th>
            <th>Actions</th>
          </tr>
        </thead>
        <!-- Table body -->
        <tbody>
          <tr v-for="task in tasks" :key="task.task_id">
            <td>{{ task.task_id }}</td>
            <td>{{ task.name }}</td>
            <td>{{ task.description }}</td>
            <td>{{ formatDate(task.start_date) }}</td>
            <td>{{ formatDate(task.due_date) }}</td>
            <td>{{ task.status }}</td>
            <td>{{ task.project_id }}</td>
            <td>
              <router-link :to="`/tasks/update/${task.task_id}`">Edit</router-link>
              <button @click="deleteTask(task.task_id)">Delete</button>
            </td>
          </tr>
          <tr align="center">
            <td colspan="8" >
                <router-link to="/tasks/create" class="create-button">Create New Task</router-link>
   
            </td>
          </tr>
        </tbody>
      </table>
       </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'TaskList',
    data() {
      return {
        tasks: [], // Placeholder for the list of tasks
      };
    },
    created() {
      this.fetchTasks();
    },
    methods: {
      formatDate(date) {
        // Create a new Date object from the provided date string
        const formattedDate = new Date(date);
  
        // Extract the date components (day, month, year)
        const day = formattedDate.getDate();
        const month = formattedDate.getMonth() + 1; // Month starts from 0, so add 1
        const year = formattedDate.getFullYear();
  
        // Return the formatted date as a string (e.g., "DD/MM/YYYY")
        return `${day}/${month}/${year}`;
      },
      fetchTasks() {
        // Make a GET request to fetch all tasks from the backend API
        axios
          .get('http://localhost:5000/tasks')
          .then((response) => {
            this.tasks = response.data; // Update the local tasks array with the data from the API
          })
          .catch((error) => {
            console.error('Error fetching tasks:', error);
          });
      },
      deleteTask(taskId) {
        axios
          .delete(`http://localhost:5000/tasks/${taskId}`)
          .then(() => {
            // Remove the deleted task from the local tasks array
            this.tasks = this.tasks.filter((task) => task.task_id !== taskId);
            console.log('Task deleted successfully!');
            this.fetchTasks();
          })
          .catch((error) => {
            console.error('Error deleting task:', error);
          });
      },
    },
  };
  </script>
  
  <style scoped>
  
.task-list-container {
    display: flex;
  flex-direction: column;
  align-items: center;
  height: 100vh;
  
  
}

h1 {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 20px;
  text-align: center;
}

.task-list-table {
  width: 60%;
  border-collapse: collapse;
  color: #fff;
  background: linear-gradient(to bottom right, #836de5, #023B79);
 
}

th,
td {
  padding: 10px;
  text-align: left;
  border-bottom: 1px solid #ddd;
}

th {
  font-weight: bold;
  
}




td button {
  display: inline-block;
  margin-right: 5px;
  padding: 5px 10px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-weight: bold;
}

td button:hover {
  background-color: #0056b3;
}

td button:active {
  background-color: #00418a;
}

td a {
  display: inline-block;
  margin-right: 5px;
  padding: 5px 10px;
  background-color: #007bff;
  color: #fff;
  text-decoration: none;
  border-radius: 4px;
  cursor: pointer;
  font-weight: bold;
}

td a:hover {
  background-color: #0056b3;
}

td a:active {
  background-color: #00418a;
}

.create-button {
  display: inline-block;
  margin-top: 20px;
  padding: 10px;
  background-color:#007bff;
  /* Green color for the button */
  color: #fff;
  text-decoration: none;
  border-radius: 4px;
  cursor: pointer;
  font-weight: bold;
  text-align: center;
}

.create-button:hover {
  background-color:#00418a;
  /* Darker green on hover */
}

.create-button:active {
  background-color: #1e7e34;
  /* Even darker green on active state */
}

  
  </style>
  