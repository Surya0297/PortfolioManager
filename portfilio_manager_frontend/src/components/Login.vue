<template>
    <div class="login-page">
      <h1>Login</h1>
      <form @submit.prevent="loginUser">
        <div class="form-group">
          <label for="username">Username:</label>
          <input type="text" v-model="username" required />
        </div>
        <div class="form-group">
          <label for="password">Password:</label>
          <input type="password" v-model="password" required />
        </div>
        <button type="submit">Login</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    name: 'LoginPage',
    data() {
      return {
        username: '',
        password: '',
      };
    },
    methods: {
      loginUser() {
        const adminUsername = 'admin';
      const adminPassword = 'admin123';

      if (this.username === adminUsername && this.password === adminPassword) {
        // If the username and password match, redirect to the admin dashboard page
        this.$router.push('/admin/dashboard');
      } else {
        // If the username and password don't match, display an error message (for demonstration purposes)
        alert('Invalid username or password. Please try again.');
      }
        this.username = '';
        this.password = '';
      },
    },
  };
  </script>
  
  <style scoped>
  /* Your CSS styles for the login page go here */
  .login-page {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  display: flex;
  background-color: #fff;
  opacity: 0.9; 
  width: 15%;
  border-radius: 10px;
  flex-direction: column;
  align-items: center;
  padding: 20px;
  justify-content: center; /* Center horizontally */
}





  
  h1 {
    font-size: 24px;
    margin-bottom: 20px;
    color: #007bff;
  }
  
  .form-group {
    display: flex;
    flex-direction: column;
    margin-bottom: 20px;
  }
  
  label {
    font-weight: bold;
    color: #007bff;
  }
  body {
    background-image: url("../image/Home.png");
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center;
    height: 100vh;
  }
  input {
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
  }
  
  button {
    padding: 10px 20px;
    background-color: #007bff;
    color: #fff;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-weight: bold;
  }
  
  button:hover {
    background-color: #0056b3;
  }
  
  button:active {
    background-color: #00418a;
  }
  </style>
  