<template>
  <div class="table-container">
    

    <!-- Project List Table -->
    <table class="project-list">
      <!-- Table header -->
      <thead>
        <tr>
          <th colspan="7">
            <router-link to="/admin/dashboard" class="home-icon">
              <i class="fas fa-home" style="color: white;"></i>
            </router-link>
            <h1>Project List</h1>
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

              <label for="manager-id">Manager ID: </label>
              <input type="text" id="manager-id" v-model="managerIdFilter" @input="applyFilters" />
            </div>
          </th>
        </tr>
        <tr>
          <th>Project ID</th>
          <th>Name</th>
          <th>Status</th>
          <th>Start Date</th>
          <th>Due Date</th>
          <th>Manager ID</th>
          <th>Actions</th>
        </tr>
      </thead>
      <!-- Table body -->
      <tbody>
        <tr v-for="project in paginatedProjects" :key="project.project_id">
          <td>{{ project.project_id }}</td>
          <td>{{ project.project_name }}</td>
          <td>{{ project.status }}</td>
          <td>{{ formatDate(project.start_date) }}</td>
          <td>{{ formatDate(project.due_date) }}</td>
          <td>{{ project.manager_id }}</td>
          <td>
            <router-link :to="`/projects/update/${project.project_id}`">Edit</router-link>
            <button @click="deleteProject(project.project_id)">Delete</button>
          </td>
        </tr>
        <tr>
          <td colspan="7">
            <router-link to="/projects/create" class="create-button">Create New Project</router-link>
          </td>
        </tr>
      </tbody>
    </table>

    <!-- Pagination -->
    <div class="pagination">
      <button @click="prevPage" :disabled="currentPage === 1">Previous</button>
      <button @click="nextPage" :disabled="currentPage === totalPage">Next</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'ProjectList',
  data() {
    return {
      projects: [], // Placeholder for the list of projects
      projectIdFilter: '',
      statusFilter: '',
      managerIdFilter: '',
      currentPage: 1,
      pageSize: 5,
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
          this.applyFilters(); // Apply filters initially after fetching data
        })
        .catch((error) => {
          console.error('Error fetching projects:', error);
        });
    },
    applyFilters() {
      let filteredProjects = this.projects;

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

      // Filter by Manager ID
      if (this.managerIdFilter) {
        filteredProjects = filteredProjects.filter(
          (project) => project.manager_id.toLowerCase().includes(this.managerIdFilter.toLowerCase())
        );
      }

      // Update the filtered projects to be displayed in the table
      this.filteredProjects = filteredProjects;
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
    nextPage() {
      if (this.currentPage < this.totalPage) {
        this.currentPage++;
      }
    },
    prevPage() {
      if (this.currentPage > 1) {
        this.currentPage--;
      }
    },
  },
  computed: {
    // Computed property to handle the filtered projects
    paginatedProjects() {
      const startIdx = (this.currentPage - 1) * this.pageSize;
      return this.filteredProjects.slice(startIdx, startIdx + this.pageSize);
    },
    totalPage() {
      return Math.ceil(this.filteredProjects.length / this.pageSize);
    },
    filteredProjects() {
      // Return all projects if no filters are applied
      if (!this.projectIdFilter && !this.statusFilter && !this.managerIdFilter) {
        return this.projects;
      }

      let filteredProjects = this.projects;

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

      // Filter by Manager ID
      if (this.managerIdFilter) {
        filteredProjects = filteredProjects.filter(
          (project) => project.manager_id.toLowerCase().includes(this.managerIdFilter.toLowerCase())
        );
      }

      return filteredProjects;
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

.project-list {
  width: 60%;
  border-radius: 10px;
  border-collapse: collapse;
  background: linear-gradient(to bottom right, #836de5, #023B79);
  color: #fff;
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

input,
select {
  width: 20%;
  height: 30px;
  border-radius: 5px;
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

.search-filters {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 10px;
}

.search-filters label {
  margin-right: 5px;
}

.create-button {
  width: 300px;
  text-align: center;
  display: block;
 
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

/* Pagination styles */
.pagination {
  margin-top: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.pagination button {
  margin: 0 5px;
  padding: 5px 10px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-weight: bold;
}

.pagination button[disabled] {
  background-color: #ddd;
  cursor: not-allowed;
}

.pagination button:hover:not([disabled]) {
  background-color: #0056b3;
}

.pagination button:active:not([disabled]) {
  background-color: #00418a;
}
</style>
