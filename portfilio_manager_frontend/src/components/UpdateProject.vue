<template>
    <div class="update-project-container">
      <h1>Update Project</h1>
      <form @submit.prevent="updateProject" class="update-project-form">
        <div>
          <label for="name">Name:</label>
          <input type="text" id="name" v-model="form.name" required />
        </div>
        <div>
          <label for="description">Description:</label>
          <textarea id="description" v-model="form.description" required></textarea>
        </div>
        <div>
          <label for="start_date">Start Date:</label>
          <input type="date" id="start_date" v-model="form.start_date" required />
        </div>
        <div>
          <label for="end_date">End Date:</label>
          <input type="date" id="end_date" v-model="form.end_date" required />
        </div>
        <div>
          <label for="status">Status:</label>
          <select id="status" v-model="form.status" required>
            <option value="Not Started">Not Started</option>
            <option value="In Progress">In Progress</option>
            <option value="Completed">Completed</option>
          </select>
        </div>
        <div>
          <label for="manager_id">Manager ID:</label>
          <input type="text" id="manager_id" v-model="form.manager_id" required />
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
          name: '',
          description: '',
          start_date: '',
          end_date: '',
          status: '',
          manager_id: '',
        },
      };
    },
    created() {
      const projectId = this.$route.params.id;
      if (projectId) {
        this.fetchProject(projectId);
      }
    },
    methods: {
      fetchProject(projectId) {
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
    align-items: center;
    justify-content: center;
  }
  
  .update-project-container h1 {
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 20px;
  }
  
  .update-project-form {
    display: grid;
    gap: 10px;
  }
  
  .update-project-form label {
    font-weight: bold;
    color: #fff;
  }
  
  .update-project-form input,
  .update-project-form select,
  .update-project-form textarea {
    width: 100%;
    padding: 5px;
    font-size: 16px;
    border: 1px solid #ccc;
    background-color: aliceblue;
    border-radius: 4px;
  }
  
  .update-project-form textarea {
    resize: vertical;
  }
  
  .update-project-form button {
    background-color: #007bff;
    color: #fff;
    padding: 10px 20px;
    border: none;
    border-radius: 4px;
    font-size: 16px;
    cursor: pointer;
  }
  
  .update-project-form button:hover {
    background-color: #0056b3;
  }
  
  .update-project-form button:active {
    background-color: #00418a;
  }
  </style>
  