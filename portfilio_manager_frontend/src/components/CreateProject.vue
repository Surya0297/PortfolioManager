<template>
  <div class="create-project-container">
    <router-link to="/admin/dashboard" class="home-icon">
        <i class="fas fa-home" style="color: white;"></i>    </router-link>
      
    <h1>Create New Project</h1>
    <form @submit.prevent="createProject" class="create-project-form">
      <!-- Project Name -->
      <div>
        <label for="project_name">Project Name:</label>
        <input type="text" id="project_name" v-model="form.project_name" required />
      </div>
      <!-- Project Status -->
      <div>
        <label for="status">Status:</label>
        <select id="status" v-model="form.status" required>
          <option value="Not Started">Not Started</option>
          <option value="In Progress">In Progress</option>
          <option value="Completed">Completed</option>
        </select>
      </div>
      <!-- Project Start Date -->
      <div>
        <label for="start_date">Start Date:</label>
        <input type="date" id="start_date" v-model="form.start_date" required />
      </div>
      <div>
        <label for="due_date">Due Date:</label>
        <input type="date" id="start_date" v-model="form.due_date" required />
      </div>
      <!-- Project Description -->
      <div>
        <label for="description">Description:</label>
        <textarea id="description" v-model="form.description" required></textarea>
      </div>
      <!-- Manager ID -->
      <div>
        <label for="manager_id">Manager ID:</label>
        <select id="manager_id" v-model="form.manager_id" required>
          <option v-for="manager in managers" :key="manager.manager_id" :value="manager.manager_id">
            {{ manager.manager_id }} - {{ manager.name }}
          </option>
        </select>
      </div>
      <div>
        <button type="submit">Create</button>
      </div>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'CreateProject',
  data() {
    return {
      form: {
        project_name: '',
        status: 'Not Started',
        start_date: '',
        due_date:'',
        description: '',
        manager_id: '', // Selected manager ID
      },
      managers: [], // Placeholder for the list of active managers
    };
  },
  created() {
    this.fetchActiveManagers();
  },
  methods: {
    createProject() {
      axios
        .post('http://localhost:5000/projects', this.form)
        .then((response) => {
          console.log('Project created successfully:', response.data);
          this.$router.push('/projects');
        })
        .catch((error) => {
          console.error('Error creating project:', error);
        });
    },
    fetchActiveManagers() {
      // Fetch the list of active managers from the API
      axios
        .get('http://localhost:5000/managers/active')
        .then((response) => {
          this.managers = response.data;
        })
        .catch((error) => {
          console.error('Error fetching active managers:', error);
        });
    },
  },
};
</script>

<style scoped>
/* Your component's CSS styles go here */
.create-project-container {
  max-width: 500px;
  margin: 100px auto;
  padding: 20px;
  border: 1px solid #ccc;
  background: linear-gradient(to bottom right, #836de5, #023B79);
  border-radius: 8px;
  color: #fff;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.create-project-form {
  
  display: grid;
  gap: 10px;
}

.create-project-form label {
  font-weight: bold;
  color: #fff;
}

.create-project-form input,
.create-project-form select,
.create-project-form textarea {
  width: 100%;
  padding: 5px;
  font-size: 16px;
  border: 1px solid #ccc;
  background-color: aliceblue;
  border-radius: 4px;
}

.create-project-form textarea {
  resize: vertical;
}

.create-project-form button {
  background-color: #007bff;
  color: #fff;
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  font-size: 16px;
  cursor: pointer;
}

.create-project-form button:hover {
  background-color: #0056b3;
}

.create-project-form button:active {
  background-color: #00418a;
}
</style>
