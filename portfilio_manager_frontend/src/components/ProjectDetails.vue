<template>
    
    <div class="project-details" v-if="projectDetails">
      <h2>
      <router-link to="/manager/dashboard" class="home-icon">
      <i class="fas fa-home" style="color: white;"></i>
    </router-link>
    </h2><h2>
    <router-link to="/manager/assigned-projects" class="home-icon">
      <i class="fas fa-users" style="color: white;"></i>
    </router-link>
    </h2>
    <h2> {{ projectDetails.project_name }}</h2>
    <p>Project Code: {{ projectDetails.project_id }}</p>
    <p>Status: {{ projectDetails.status }}</p>
    <p>Start Date: {{ formatDate(projectDetails.start_date) }}</p>
    <p>Due Date: {{ formatDate(projectDetails.due_date) }}</p>
    <p>
           Progress:  {{calculateProgress()}} %
        </p>
    <div class="progress-bar">
        
      <div class="progress" :style="{ width: calculateProgress() + '%' }"></div>
    </div>
    <!-- Add more project details as needed -->
    <div class="update-status">
      <label for="status">Update Status: </label>
      <select id="status" v-model="newStatus">
        <option value="Not started">Not Started</option>
        <option value="In progress">In Progress</option>
        <option value="Completed">Completed</option>
      </select>
      <button @click="updateStatus">Update</button>
    </div>
    <div class="project-tasks">
      <h3>Project Tasks</h3>
      <div v-for="task in tasks" :key="task.task_id" class="task">
        <span>{{ task.task_id}}:   </span>
        <span> {{ task.name }}</span>
        <div>
          <input
          type="radio"
        :id="`completed_${task.task_id}`"
        value="Completed"
        v-model="task.status"
        @change="updateTaskStatus(task)"
          />
          <label :for="`completed_${task.task_id}`">Completed</label>
          <input
          type="radio"
        :id="`completed_${task.task_id}`"
        value="Not Statred"
        v-model="task.status"
        @change="updateTaskStatus(task)"
          />
          <label :for="`not_completed_${task.task_id}`">Not Completed</label>
         
      <input
        type="radio"
        :id="`in_progress_${task.task_id}`"
        value="In Progress"
        v-model="task.status"
        @change="updateTaskStatus(task)"
      />
      <label :for="`in_progress_${task.task_id}`">In Progress</label>
    
        </div>
      </div>
    </div>
  </div>
  <div v-else>
    <p>Loading project details...</p>
  </div>
  </template>
  
  <script>
  import axios from 'axios';
//   import jwtDecode from 'jwt-decode';
  
  export default {
    name: 'ProjectDetails',
    data() {
      return {
        projectDetails: null,
        tasks:[],
        newStatus: '',
      };
    },
    created() {
      this.fetchProjectDetails();
      this.fetchProjectTasks();
    },
    methods: {
      formatDate(date) {
         // Create a new Date object from the provided date string
      const formattedDate = new Date(date);
    const day = formattedDate.getDate();
    const month = formattedDate.getMonth() + 1; // Month starts from 0, so add 1
    const year = formattedDate.getFullYear();
    return `${day}/${month}/${year}`;
      },
      fetchProjectDetails() {
        // Get the project ID from the route parameters
        const projectId = this.$route.params.project_id;
  
        // Make a GET request to fetch the project details from the backend API
        axios
          .get(`http://localhost:5000/projects/${projectId}`)
          .then((response) => {
            this.projectDetails = response.data;
          })
          .catch((error) => {
            console.error('Error fetching project details:', error);
          });
      },
      fetchProjectTasks() {
      // Get the project ID from the route parameters
      const projectId = this.$route.params.project_id;

      // Make a GET request to fetch the tasks for the current project from the backend API
      axios
        .get(`http://localhost:5000/tasks/project/${projectId}`)
        .then((response) => {
          this.tasks = response.data;
        })
        .catch((error) => {
          console.error('Error fetching project tasks:', error);
        });
    },
    calculateProgress() {
      // Calculate the progress percentage
      console.log(this.tasks.length);
      if (this.tasks.length === 0) {
        return 0; // Handle the case when there are no tasks in the project
      }
      const completedTasks = this.tasks.filter((task) => task.status === 'Completed');
      const progress = (completedTasks.length / this.tasks.length) * 100;
      return Math.round(progress);
    },
    updateStatus() {
      if (!this.newStatus) {
        return; // No status selected, do nothing
      }

      
      // Make a PUT request to update the project status
      const projectId = this.$route.params.project_id;
      axios
        .put(`http://localhost:5000/projects/${projectId}`, { status: this.newStatus })
        .then((response) => {
          console.log('Project status updated successfully:', response.data);
          // Optionally, you can fetch the updated project details after updating the status
          this.fetchProjectDetails();
        })
        .catch((error) => {
          console.error('Error updating project status:', error);
        });
    },
    updateTaskStatus(task) {
      // Update the status of a specific task
      axios
        .put(`http://localhost:5000/tasks/update/${task.task_id}`, { status: task.status })
        .then((response) => {
          console.log('Task status updated successfully:', response.data);
        })
        .catch((error) => {
          console.error('Error updating task status:', error);
        });
    },
  },
    
  };
  </script>
  
<style scoped>
/* Your CSS styles for the ProjectDetails component go here */
.project-details {
  max-width: 800px;
  margin: 100px auto;
  color: #fff;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  background: linear-gradient(to bottom right, #836de5, #023b79);
}

.project-name {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 10px;
}

h2{

}


.project-info {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
  margin-top: 20px;
}
.update-status{

  margin-top: 10px;
}

.update-status select{
  margin-left: 20px;
}

.update-status button {
  background-color: #023b79;
  padding: 4px;
  color: #fff;
  border-radius: 4px;
  border: 0px;
  margin-left: 20px;
}

.project-info p {
  margin: 0;
  font-size: 16px;
}

/* Progress bar styles */
.progress-bar {
  height: 20px;
  background-color: #ccc;
  border-radius: 8px;
  overflow: hidden;
}

.progress {
  height: 100%;
  background-color: #4caf50; /* Green */
}

/* Customize the styling of the loading message */
div[v-else] {
  text-align: center;
  font-size: 16px;
  color: #999;
  padding: 20px;
}
</style>