<template>
  <div class="admin-dashboard">
    <h1>Welcome, Admin</h1>
    <div class="options-grid">
      <!-- Option 1 -->
      <div class="option" @click="navigateToPage('/portfolio_managers')">
        <i class="fas fa-users"></i> <!-- Font Awesome icon for "users" -->
        <span>View All Managers</span>
      </div>

      <!-- Option 2 -->
      <div class="option" @click="navigateToPage('/projects')">
        <i class="fas fa-project-diagram"></i> <!-- Font Awesome icon for "project-diagram" -->
        <span>View All Projects</span>
      </div>

      <!-- Option 3 -->
      <div class="option" @click="navigateToPage('/tasks')">
        <i class="fas fa-tasks"></i> <!-- Font Awesome icon for "tasks" -->
        <span>View All Tasks</span>
      </div>

      <!-- Option 4 -->
      <div class="option" @click="navigateToPage('/resources')">
        <i class="fa-solid fa-database" style="color: #eff1f5;"></i>        <span>View All Resources</span>
      </div>

      <!-- Option 5 -->
      <div class="option" @click="navigateToPage('/projects/available')">
        <i class="fa-solid fa-hand-holding-hand"></i>        <span>Assign Projects</span>
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
export default {
  name: 'AdminDashboard',
  methods: {
    navigateToPage(path) {
      this.$router.push(path);
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
