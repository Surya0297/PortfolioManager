<!-- TaskForm.vue -->

<template>
    <div class="task-form-container">
      <router-link to="/admin/dashboard" class="home-icon">
              <i class="fas fa-home" style="color: white;"></i>
                </router-link>
      <h1>{{ isUpdating ? 'Update Task' : 'Create New Task' }}</h1>
      <form @submit.prevent="submitForm">
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
          <label for="due_date">Due Date:</label>
          <input type="date" id="due_date" v-model="form.due_date" required />
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
          <label for="project_id">Project ID:</label>
          <input type="text" id="project_id" v-model="form.project_id" required />
        </div>
        <div>
          <button type="submit">{{ isUpdating ? 'Update' : 'Create' }}</button>
        </div>
      </form>
    </div>
  </template>
  

  <script>
  import axios from 'axios';
  
  export default {
    name: 'TaskForm',
    data() {
      return {
        isUpdating: false,
        form: {
          name: '',
          description: '',
          start_date: '',
          due_date: '',
          status: '',
          project_id: '',
        },
      };
    },
    created() {
      const taskId = this.$route.params.id;
      if (taskId) {
        this.isUpdating = true;
        this.fetchTask(taskId);
      }
    },
    methods: {
      fetchTask(taskId) {
        axios
          .get(`http://localhost:5000/tasks/${taskId}`)
          .then((response) => {
            this.form = response.data;
          })
          .catch((error) => {
            console.error('Error fetching task:', error);
          });
      },
      createTask() {
        console.log('Creating task:', this.form);
        axios
          .post('http://localhost:5000/tasks', this.form)
          .then((response) => {
            console.log('Task created successfully:', response.data);
            this.$router.push('/tasks');
          })
          .catch((error) => {
            console.error('Error creating task:', error);
          });
      },
      updateTask() {
        console.log('Updating task:', this.form);
        const taskId = this.$route.params.id;
        axios
          .put(`http://localhost:5000/tasks/update/${taskId}`, this.form)
          .then((response) => {
            console.log('Task updated successfully:', response.data);
            this.$router.push('/tasks');
          })
          .catch((error) => {
            console.error('Error updating task:', error);
          });
      },
      submitForm() {
      console.log('Form submitted');
      this.isUpdating ? this.updateTask() : this.createTask();
    },
    },
  };
  </script>
  
  
  <style>
  /* Your component's CSS styles go here */
  .task-form-container {
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
  
  .task-form-container h1 {
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 20px;
  }
  
  .task-form-container form {
    display: grid;
    gap: 10px;
  }
  
  .task-form-container label {
    font-weight: bold;
    color: #fff;
  }
  
  .task-form-container input,
  .task-form-container select,
  .task-form-container textarea {
    width: 100%;
    padding: 5px;
    font-size: 16px;
    border: 1px solid #ccc;
    background-color: aliceblue;
    border-radius: 4px;
  }
  
  .task-form-container textarea {
    resize: vertical;
  }
  
  .task-form-container button {
    background-color: #007bff;
    color: #fff;
    padding: 10px 20px;
    border: none;
    border-radius: 4px;
    font-size: 16px;
    cursor: pointer;
  }
  
  .task-form-container button:hover {
    background-color: #0056b3;
  }
  
  .task-form-container button:active {
    background-color: #00418a;
  }
  </style>
  
  