<template>
  <div class="update-manager-container">
    <h1>Update Portfolio Manager</h1>
    <form @submit.prevent="updateManager">
      <div class="form-group">
        <label for="name">Name:</label>
        <input type="text" id="name" v-model="form.name" required />
      </div>
      <div class="form-group">
        <label for="username">Username:</label>
        <input type="text" id="username" v-model="form.username" required />
      </div>
      <div class="form-group">
        <label for="status">Status:</label>
        <select id="status" v-model="form.status" required>
          <option value="Active">Active</option>
          <option value="Inactive">Inactive</option>
        </select>
      </div>
      <div class="form-group">
        <label for="role">Role:</label>
        <select id="role" v-model="form.role" required>
          <option value="Administrator">Administrator</option>
          <option value="Viewer">Viewer</option>
        </select>
      </div>
      <div class="form-group">
        <label for="bio">Bio:</label>
        <textarea id="bio" v-model="form.bio" required></textarea>
      </div>
      <div class="form-group">
        <label for="start_date">Start Date:</label>
        <input type="date" id="start_date" v-model="form.start_date" required />
      </div>
      <div class="form-group">
        <button type="submit">Update</button>
      </div>
    </form>
  </div>
</template>

<style>
/* Your component's CSS styles go here */
.update-manager-container {
  max-width: 500px;
  margin: auto;
  padding: 20px;
  border: 1px solid #ccc;
  background: linear-gradient(to bottom right, #836de5, #023B79);
  border-radius: 8px;
  color: #fff;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

h1 {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 20px;
  text-align: center;
}

form {
  display: flex;
  flex-direction: column;
}

.form-group {
  display: flex;
  flex-direction: column;
  margin-bottom: 15px;
}

.form-group label {
  font-weight: bold;
}

.form-group input[type="text"],
.form-group select,
.form-group textarea,
.form-group input[type="date"] {
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 16px;
}

.form-group select {
  width: 100%;
}

.form-group textarea {
  resize: vertical;
}

.form-group button {
  padding: 10px;
  width: 20%;
  margin: auto;
  background-color:#0056b3;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-weight: bold;
  transition: background-color 0.2s ease;
}

.form-group button:hover {
  background-color:#00418a;
}

.form-group button:active {
  background-color: #00418a;
}
</style>

  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'UpdatePortfolioManager',
    data() {
      return {
        form: {
          name: '',
          username: '',
          status: '',
          role: '',
          bio: '',
          start_date: '',
        },
      };
    },
    created() {
      this.fetchManager();
    },
    methods: {
      fetchManager() {
        const managerId = this.$route.params.id; // Corrected: Use 'id' to access the managerId from the route
        axios
          .get(`http://localhost:5000/portfolio_managers/${managerId}`)
          .then((response) => {
            this.form = response.data;
          })
          .catch((error) => {
            console.error('Error fetching Portfolio Manager:', error);
          });
      },
      updateManager() {
        const managerId = this.$route.params.id; // Corrected: Use 'id' to access the managerId from the route
        axios
          .put(`http://localhost:5000/portfolio_managers/${managerId}`, this.form)
          .then((response) => {
            // Handle the successful response, e.g., show a success message or redirect to the Portfolio Manager list page
            console.log('Portfolio Manager updated successfully:', response.data);
            // Redirect the user to the Portfolio Manager list page
            this.$router.push('/portfolio_managers');
          })
          .catch((error) => {
            // Handle errors, e.g., show an error message to the user
            console.error('Error updating Portfolio Manager:', error);
          });
      },
    },
  };
  </script>
  

  