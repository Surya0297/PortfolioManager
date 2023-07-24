
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
  import axios from 'axios';
  export default {
    name: 'LoginPage',
    data() {
      return {
        username: '',
        password: '',
      };
    },
    methods: {
      async loginUser() {
      const adminUsername = 'admin';
      const adminPassword = 'admin123';

      if (this.username === adminUsername && this.password === adminPassword) {
        // If the username and password match the admin credentials, redirect to the admin dashboard page
        this.$router.push('/admin/dashboard');
        this.username = '';
        this.password = '';
      } else {
        // If the credentials are not admin's, send a request to the backend API for manager authentication
        try {
          const response = await axios.post('http://localhost:5000/login', {
            username: this.username,
            password: this.password,
          });
          const accessToken = response.data.access_token;
          // Save the access token in localStorage or Vuex store for further authenticated requests
          localStorage.setItem('accessToken', accessToken);
          // Redirect to the manager dashboard page upon successful login
          this.$router.push('/manager/dashboard');
          this.username = '';
          this.password = '';
        } catch (error) {
          alert('Invalid username or password. Please try again.');
          console.error('Error logging in:', error);
        }
      }
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
  
  opacity: 0.9; 
  width: 15%;
  border-radius: 10px;
  flex-direction: column;
  align-items: center;
  padding: 20px;
  justify-content: center; /* Center horizontally */
  background: linear-gradient(to bottom right, #836de5, #023B79);

}





  
  h1 {
    font-size: 24px;
    margin-bottom: 20px;
    color:#00418a;
  }
  
  .form-group {
    display: flex;
    flex-direction: column;
    margin-bottom: 20px;
  }
  
  label {
    font-weight: bold;
    color:#00418a;
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
    background-color: #00418a;
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
  