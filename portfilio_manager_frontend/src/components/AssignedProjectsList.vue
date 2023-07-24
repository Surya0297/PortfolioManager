<template>
    <div class="assigned-projects">
     
      <table class="project-list">
        <thead>
            <tr>
                <th colspan="6" >
                    <router-link to="/manager/dashboard" class="home-icon">
      <i class="fas fa-home" style="color: white;"></i>
    </router-link>
                    <h2>Assigned Projects</h2>
                </th>
            </tr>
            <tr>
          <th th colspan="7">
            <div class="search-filters">
              <label for="project-id">Project ID: </label>
              <input type="text" id="project-id" v-model="projectIdFilter" @input="applyFilters" />

              <label for="status">Status: </label>
              <select id="status" v-model="statusFilter" @change="applyFilters">
                <option value="">All</option>
                <option value="not started">Not started</option>
                <option value="in progress">In Progress</option>
                <option value="completed">Completed</option>
              </select>
            </div>
          </th>
        </tr>
          <tr>
            <th>Project ID</th>
            <th>Name</th>
            <th>Status</th>
            <th>Start Date</th>
            <th>Due Date</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="project in assignedProjects" :key="project._id">
            <td>{{ project.project_id }}</td>
            <td>{{ project.project_name }}</td>
            <td>{{ project.status }}</td>
            <td>{{ formatDate(project.start_date) }}</td>
            <td>{{ formatDate(project.due_date) }}</td>
            <td>
              <router-link :to="`/projects/${project.project_id}`">View Details</router-link>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </template>
  <script>
  import axios from 'axios';
  import jwtDecode from 'jwt-decode';

  export default {
    name: 'AssignedProjectsList',
    data() {
      return {
        assignedProjects: [],
        managerId: null,
        projectIdFilter: '',
      statusFilter: '',
      };
    },
    created() {
        this.fetchManagerId();
      this.fetchAssignedProjects();
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
        // Implement the formatDate function to format the date as needed
      },
      fetchManagerId() {
      const token = localStorage.getItem('accessToken');
      if (token) {
        try {
          const decodedToken = jwtDecode(token);
          this.managerId = decodedToken.sub;
          
        } catch (error) {
          console.error('Error decoding JWT token:', error);
        }
      } else {
        console.log('No JWT token found in local storage');
      }
    },
    fetchAssignedProjects() {
        // Make a GET request to fetch assigned projects from the backend API
        axios
          .get(`http://localhost:5000/manager/projects/${this.managerId}`)
          .then((response) => {
            this.assignedProjects = response.data;
            this.applyFilters();
          })
          .catch((error) => {
            console.error('Error fetching assigned projects:', error);
          });
      },
    applyFilters() {
      let filteredProjects = this.assignedProjects;

      // Filter by Project ID
      if (this.projectIdFilter) {
        filteredProjects = filteredProjects.filter(
          (project) => project.project_id.toLowerCase().includes(this.projectIdFilter.toLowerCase())
        );
      }

      // Filter by Status
      if (this.statusFilter) {
        filteredProjects = filteredProjects.filter((project) => project.status.toLowerCase() === this.statusFilter.toLowerCase());
      }

     

      // Update the filtered projects to be displayed in the table
      this.filteredProjects = filteredProjects;
    },
     
    },
    computed: {
    // Computed property to handle the filtered projects
    
    filteredProjects() {
      // Return all projects if no filters are applied
      if (!this.projectIdFilter && !this.statusFilter) {
        return this.assignedProjects;
      }

      let filteredProjects = this.assignedProjects;

      // Filter by Project ID
      if (this.projectIdFilter) {
        filteredProjects = filteredProjects.filter(
          (project) => project.project_id.toLowerCase().includes(this.projectIdFilter.toLowerCase())
        );
      }

      // Filter by Status
      if (this.statusFilter) {
        filteredProjects = filteredProjects.filter((project) => project.status.toLowerCase() === this.statusFilter.toLowerCase());
      }
     

      return filteredProjects;
    },
  },
  };
  </script>
  <style scoped>
  /* Your custom styles for the assigned projects view */
  .assigned-projects {
    margin-top: 100px;
  display: flex;
  flex-direction: column;
  align-items: center;
  height: 100vh;
  font-family: 'Franklin Gothic Medium';
  }
  
  h2 {
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 20px;
    text-align: center;
  }
  
  .project-list {
    width: 60%;
  border-radius: 10px;
  border-collapse: collapse;
  background: linear-gradient(to bottom right, #836de5, #023b79);
  color: #fff;
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
  

  
  /* Styles for router-link */
  td a {
    display: inline-block;
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
  </style>