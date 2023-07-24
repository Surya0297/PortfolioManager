<template>
  <div class="assign-manager">
    <router-link to="/admin/dashboard" class="home-icon">
              <i class="fas fa-home" style="color: white;"></i>
                </router-link>
    <h1>Assign Manager to Project</h1>
    <form @submit.prevent="handleSubmit">
      <div class="form-group">
        <label for="manager">Select Manager:</label>
        <select v-model="selectedManager" id="manager" required>
          <option v-for="manager in activeManagers" :key="manager.manager_id" :value="manager.manager_id">
            {{ manager.manager_id +" - "+ manager.name }}
          </option>
        </select>
      </div>
      <button type="submit">Assign</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'AssignManager',
  data() {
    return {
      selectedManager: null,
      activeManagers: [],
    };
  },
  created() {
    this.fetchActiveManagers();
  },
  methods: {
    fetchActiveManagers() {
      axios
        .get('http://localhost:5000/managers/active')
        .then((response) => {
          this.activeManagers = response.data;
        })
        .catch((error) => {
          console.error('Error fetching active managers:', error);
        });
    },
    handleSubmit() {
      const projectId = this.$route.params.projectId;
      const data = {
        managerId: this.selectedManager,
      };
      console.log(data['managerId'])
      axios
        .put(`http://localhost:5000/projects/${projectId}/assign-manager`, data)
        .then(() => {
          console.log('Manager assigned successfully!');
          this.$router.push('/projects');
        })
        .catch((error) => {
          console.error('Error assigning manager:', error);
        });
    },
  },
};
</script>

<style scoped>
/* Your component's CSS styles go here */
.assign-manager {
  max-width: 500px;
  margin: auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 8px;
  background: linear-gradient(to bottom right, #836de5, #023B79);
  color: #fff;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

h1 {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 20px;
}

form {
  display: flex;
  flex-direction: column;
  align-items: center;
}

label {
  font-weight: bold;
  margin-bottom: 5px;
}

select {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  margin-bottom: 15px;
  font-size: 16px;
}

button {
  padding: 10px 20px;
  background-color: #007bff;
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
