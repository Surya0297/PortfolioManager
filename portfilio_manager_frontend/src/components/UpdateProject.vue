<template>
    <div class="update-project-container">
      <h1>Update Project</h1>
      <form @submit.prevent="updateProject">
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
        <!-- Project Description -->
        <div>
          <label for="description">Description:</label>
          <textarea id="description" v-model="form.description" required></textarea>
        </div>
        <div>
          <button type="submit">Update</button>
        </div>
      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'UpdateProject',
    data() {
      return {
        form: {
          project_name: '',
          status: 'Not Started',
          start_date: '',
          description: '',
        },
      };
    },
    created() {
      this.fetchProject();
    },
    methods: {
      fetchProject() {
        const projectId = this.$route.params.id;
        axios
          .get(`http://localhost:5000/projects/${projectId}`)
          .then((response) => {
            this.form = response.data;
          })
          .catch((error) => {
            console.error('Error fetching project:', error);
          });
      },
      updateProject() {
        const projectId = this.$route.params.id;
        axios
          .put(`http://localhost:5000/projects/${projectId}`, this.form)
          .then((response) => {
            console.log('Project updated successfully:', response.data);
            this.$router.push('/projects');
          })
          .catch((error) => {
            console.error('Error updating project:', error);
          });
      },
    },
  };
  </script>
  
  <!-- Styles... -->
  
  
  <style>
  /* Your component's CSS styles go here */
  .update-project-container {
    max-width: 500px;
    margin: auto;
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
  
  h1 {
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 20px;
  }
  
  form {
    display: flex;
    flex-direction: column;
  }
  
  label {
    font-weight: bold;
    margin-bottom: 5px;
  }
  
  input[type="text"],
  select,
  textarea,
  input[type="date"] {
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
    margin-bottom: 15px;
    font-size: 16px;
  }
  
  select {
    width: 100%;
  }
  
  textarea {
    resize: vertical;
  }
  
  button {
    padding: 10px;
    background-color: #00418a;
    color: #fff;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-weight: bold;
    transition: background-color 0.2s ease;
  }
  
  button:hover {
    background-color: #0056b3;
  }
  
  button:active {
    background-color: #00418a;
  }
  </style>
  