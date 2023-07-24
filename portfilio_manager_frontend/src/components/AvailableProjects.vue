<template>
  <div class="table-container">
    <table class="available-project-list">
      <!-- Table header -->
      <thead>
        <tr>
          <th colspan="5">
            <router-link to="/admin/dashboard" class="home-icon">
              <i class="fas fa-home" style="color: white;"></i>
            </router-link>
            <h1>Available Projects</h1>
          </th>
        </tr>
      </thead>
      <thead>
        <tr>
          <th>Project ID</th>
          <th>Name</th>
          <th>Status</th>
          <th>Manager</th>
          <th>Actions</th>
        </tr>
      </thead>
      <!-- Table body -->
      <tbody>
        <tr v-for="project in availableProjects" :key="project._id">
          <td>{{ project.project_id }}</td>
          <td>{{ project.project_name }}</td>
          <td>{{ project.status ? 'Active' : 'Inactive' }}</td>
          <td>{{ project.manager_id ? 'Assigned' : 'Not Assigned' }}</td>
          <td v-if="!project.manager_id">
            <router-link :to="`/projects/assign/${project.project_id}`">Assign Manager</router-link>
          </td>
          <td v-else>
            <router-link :to="`/projects/update/${project.project_id}`">Edit</router-link>
            <button @click="deleteProject(project.project_id)">Delete</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'AvailableProjectList',
  data() {
    return {
      availableProjects: [], // Placeholder for the list of available projects
    };
  },
  created() {
    this.fetchAvailableProjects();
  },
  methods: {
    fetchAvailableProjects() {
      // Make a GET request to fetch projects with no manager assigned
      axios
        .get('http://localhost:5000/projects/available')
        .then((response) => {
          this.availableProjects = response.data;
        })
        .catch((error) => {
          console.error('Error fetching available projects:', error);
        });
    },
    deleteProject(projectId) {
      axios
        .delete(`http://localhost:5000/projects/${projectId}`)
        .then(() => {
          this.availableProjects = this.availableProjects.filter((project) => project._id !== projectId);
          console.log('Project deleted successfully!');
        })
        .catch((error) => {
          console.error('Error deleting project:', error);
        });
    },
  },
};
</script>

<style scoped>
/* Your component's CSS styles go here */
.table-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  height: 100vh;
  margin-top: 100px;
}

.available-project-list {
  width: 50%;
  border-radius: 10px;
  border-collapse: collapse;
  background: linear-gradient(to bottom right, #836de5, #023B79);
  color: #fff;
  margin-bottom: 30px;
}

h1 {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 20px;
  text-align: center;
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

/* Styles for router-link (Edit and Assign Manager buttons) */
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

/* Create New Project Button */
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
  background-color: #0056b3; /* Darker blue on hover */
}

.create-button:active {
  background-color: #1e7e34; /* Even darker blue on active state */
}
</style>
