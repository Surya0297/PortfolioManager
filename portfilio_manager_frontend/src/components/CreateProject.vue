<template>
    <div class="create-project-container">
      <h1>Create New Project</h1>
      <form @submit.prevent="createProject">
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
          description: '',
        },
      };
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
    },
  };
  </script>
  
  <!-- Styles... -->
  
  
  <style>
  /* Your component's CSS styles go here */
  .create-project-container {
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
  