<template>
  <div class="admin-dashboard">
    <h1>Welcome, Portfolio Manager</h1>

    <AssignedProjectsList :managerId="managerId" />

    <div class="options-grid">
      <!-- Option 1 -->
      <div class="option" @click="navigateToPage('/manager/assigned-projects')">
        <i class="fas fa-users"></i> <!-- Font Awesome icon for "users" -->
        <span>View All Assigned Projects</span>
      </div>

       <!-- Option 6 -->
       <div class="option" @click="navigateToPage('/login')">
        <i class="fa-solid fa-right-from-bracket"></i>    <span>Log Out</span>
      </div>

      <!-- Add more options as needed -->
      <!-- ... -->
    </div>
  </div>
</template>

<script>
import jwtDecode from 'jwt-decode';

export default {
  name: 'AdminDashboard',
  data() {
    return {
      managerId: null,
    };
  },
  created() {
    this.fetchManagerId();
  },
  methods: {
    navigateToPage(path) {
      this.$router.push(path);
    },
  
  fetchManagerId() {
      // Get the JWT token from local storage (you might have different storage mechanism)
      const token = localStorage.getItem('accessToken');

      if (token) {
        try {
      // Decode the JWT token to get the manager's ID from the payload
      const decodedToken = jwtDecode(token);
      this.managerId = decodedToken.sub;
      console.log(this.managerId);
    } catch (error) {
      console.error('Error decoding JWT token:', error);
    }
  } else {
    console.log('No JWT token found in local storage');
  }
    },
  },
};
</script>

<style scoped>
/* Your CSS styles for the Admin Dashboard go here */
.admin-dashboard {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 50px;
}

h1 {
  font-size:30px;
  font-weight: bold;
  margin-top: 100px;
  margin-bottom: 20px;
  color:#fff; /* Custom color for the heading */
}

.options-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr); /* Adjust the number of columns as needed */
  gap: 20px; /* Adjust the gap between options */

}

.option {
  cursor: pointer;
  display: flex;
  flex-direction: column;
  align-items: center;
  color: #fff;
  border: 1px solid #ccc; /* Border around each option */
  padding: 20px;
  border-radius: 8px;
  background: linear-gradient(to bottom right, #836de5, #023B79);
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* Add a subtle box shadow */
  transition: transform 0.2s ease-in-out; /* Add a smooth transform effect on hover */
}

.option:hover {
  transform: scale(1.05); /* Scale up the option on hover */
}

.option i {
  font-size: 36px; /* Adjust the icon size as needed */
  margin-bottom: 10px;
}

.option span {
  font-size: 16px;
  font-weight: bold;
  color:#fff; /* Custom color for the option text */
}
</style>
