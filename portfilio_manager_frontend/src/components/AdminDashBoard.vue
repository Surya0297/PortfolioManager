<template>
  <div class="admin-dashboard">
    <h1>Welcome, Admin</h1>
    <div class="options-grid">
      <!-- Option 1 -->
      <div class="option" @click="navigateToPage('/portfolio_managers')">
        <img src="../image/ViewAllManager.png" alt="Option 1" />
        <span>View All Manager</span>
      </div>

      <!-- Option 2 -->
      <div class="option" @click="navigateToPage('/projects')">
        <img src="path/to/option2-image.jpg" alt="Option 2" />
        <span>Option 2</span>
      </div>

      <!-- Option 3 -->
      <div class="option" @click="navigateToPage('/option3')">
        <img src="path/to/option3-image.jpg" alt="Option 3" />
        <span>Option 3</span>
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
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 20px;
}

.options-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr); /* Adjust the number of columns as needed */
  gap: 20px; /* Adjust the gap between options */
}

.option {
  cursor: pointer;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.option img {
  width: 100px; /* Adjust the image size as needed */
  height: 100px; /* Adjust the image size as needed */
  object-fit: cover; /* Ensure the image maintains aspect ratio */
  border-radius: 50%;
  margin-bottom: 10px;
}

.option span {
  font-size: 16px;
  font-weight: bold;
}
</style>
