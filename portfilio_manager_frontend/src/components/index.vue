<!-- src/components/index.vue -->
<template>
    <div class="landing-page">
  
      <div class="login-signup-button">
        <router-link to="/login" class="button">Login/Signup</router-link>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'LandingPage',
  };
  </script>
  
  <style >
  /* Your CSS styles for the landing page go here */
  /* Customize the styles to match your design preferences */
  .landing-page {
    /* Center the content vertically and horizontally */
    display: flex;
    flex-direction: column;
    align-items: center;
     /* Align the content to the right side */
    height: 100vh; /* Adjust the height as needed */
  }
  
  body {
    background-image: url("../image/Home.png");
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center;
    height: 100vh;
  }
  
  .logo h1 {
    /* Style the app name text */
    font-size: 24px;
    font-weight: bold;
    margin-top: 10px;
  }
  
  .login-signup-button {
    margin-top: 35%;
    margin-left: 50%;
  }
  
  .login-signup-button a {
    /* Style the login/signup button */
    display: inline-block;
    padding: 10px 20px;
    background-color: #fff;
    color: #007bff;
    text-decoration: none;
    border-radius: 4px;
    cursor: pointer;
    font-weight: bold;
  }
  
  .login-signup-button a:hover {
    background-color: #007bff;
    color: #fff;
  }
  
  .login-signup-button a:active {
    background-color: #a1c7f3;
  }
  </style>
  