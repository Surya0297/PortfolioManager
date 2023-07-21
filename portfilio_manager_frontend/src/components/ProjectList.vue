<template>
    <div class="table-container">
      
      <table class="project-list">
        <!-- Table header -->
        <thead>
            <tr>
                <th colspan="5">
                    <h1>Project List</h1>
                </th>
            </tr>
          <tr>
            <th>Project ID</th>
            <th>Name</th>
            <th>Status</th>
            <th>Start Date</th>
            <th>Actions</th>
          </tr>
        </thead>
        <!-- Table body -->
        <tbody>
          <tr v-for="project in projects" :key="project.project_id">
            <td>{{ project.project_id }}</td>
            <td>{{ project.project_name }}</td>
            <td>{{ project.status }}</td>
            <td>{{ formatDate(project.start_date) }}</td>
            <td>
              <router-link :to="`/projects/update/${project.project_id}`">Edit</router-link>
              <button @click="deleteProject(project.project_id)">Delete</button>
            </td>
          </tr>
          <tr>
            <td colspan="5">
                <router-link to="/projects/create" class="create-button">Create New Project</router-link>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'ProjectList',
    data() {
      return {
        projects: [], // Placeholder for the list of projects
      };
    },
    created() {
      this.fetchProjects();
    },
    methods: {
      formatDate(date) {
        const formattedDate = new Date(date);
        const day = formattedDate.getDate();
        const month = formattedDate.getMonth() + 1;
        const year = formattedDate.getFullYear();
        return `${day}/${month}/${year}`;
      },
      fetchProjects() {
        axios
          .get('http://localhost:5000/projects')
          .then((response) => {
            this.projects = response.data;
          })
          .catch((error) => {
            console.error('Error fetching projects:', error);
          });
      },
      deleteProject(projectId) {
        axios
          .delete(`http://localhost:5000/projects/${projectId}`)
          .then(() => {
            this.projects = this.projects.filter((project) => project.project_id !== projectId);
            console.log('Project deleted successfully!');
          })
          .catch((error) => {
            console.error('Error deleting project:', error);
          });
      },
    },
  };
  </script>
  
  <style >
  /* Your component's CSS styles go here */
  .table-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    height: 100vh;
  }
  
  .project-list {
    width: 60%;
    border-collapse: collapse;
    background: linear-gradient(to bottom right, #836de5, #023B79);
    color: #fff;
    
  }
  
  h1 {
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 20px;
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
  
  
  
  tr:hover {
    background-color: #007bff;
  }
  
  /* Styles for table cell buttons */
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
  
  /* Styles for router-link (Edit button) */
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
    width: 300px;
    text-align: center;
    display: block;
    margin: auto; /* Center the button horizontally */
    padding: 10px;
    background-color: #007bff;
    color: #fff;
    text-decoration: none;
    border-radius: 4px;
    cursor: pointer;
    font-weight: bold;
  }
  
  .create-button:hover {
    background-color: #0056b3; /* Darker green on hover */
  }
  
  .create-button:active {
    background-color: #1e7e34; /* Even darker green on active state */
  }
  </style>
  