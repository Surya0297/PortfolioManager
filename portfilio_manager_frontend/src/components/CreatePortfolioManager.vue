
  
  <template>
    <div class="create-manager-container">
      <router-link to="/admin/dashboard" class="home-icon">
        <i class="fas fa-home" style="color: white;"></i>    </router-link>
      <h1>Create New Portfolio Manager</h1>
      <form @submit.prevent="createManager" class="create-manager-form">
        <div>
          <label for="name">Name:</label>
          <input type="text" id="name" v-model="form.name" required />
        </div>
        <div>
          <label for="username">Username:</label>
          <input type="text" id="username" v-model="form.username" required />
        </div>
        <div>
          <label for="status">Status:</label>
          <select id="status" v-model="form.status" required>
            <option value="Active">Active</option>
            <option value="Inactive">Inactive</option>
          </select>
        </div>
        <div>
          <label for="bio">Bio:</label>
          <textarea id="bio" v-model="form.bio" required></textarea>
        </div>
        <div>
          <label for="joining_date">Joining Date:</label>
          <input type="date" id="joining_date" v-model="form.joining_date" required />
        </div>
        <div>
          <label for="password">Password:</label>
          <input type="password" id="password" v-model="form.password" required />
        </div>
        <div>
          <button type="submit">Create</button>
        </div>
      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'CreatePortfolioManager',
    data() {
      return {
        form: {
          name: '',
          username: '',
          status: '',
          bio: '',
          joining_date: '',
          password: '',
        },
      };
    },
    methods: {
      createManager() {
        const generatedPassword = this.generateRandomPassword();
        console.log(generatedPassword)
        this.form.password = generatedPassword;
        
        axios
          .post('http://localhost:5000/portfolio_managers', this.form)
          .then((response) => {
            // Handle the successful response, e.g., show a success message or redirect to the Portfolio Manager list page
            console.log('Portfolio Manager created successfully:', response.data);
            this.sendPasswordEmail(this.form.username, generatedPassword);

            // Redirect the user to the Portfolio Manager list page
            this.$router.push('/portfolio_managers');

          })
          .catch((error) => {
            // Handle errors, e.g., show an error message to the user
            if (error.response && error.response.data && error.response.data.message) {
        // Display the error message to the user
        console.log(error.response.data.message);
        alert('Username already exists. Please choose a different username.');
            }
            console.error('Error creating Portfolio Manager:', error);
          });
      },
      generateRandomPassword() {
      // Function to generate a random password (You can customize this as per your requirement)
      const chars =
        'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
      let password = '';
      for (let i = 0; i < 8; i++) {
        const randomIndex = Math.floor(Math.random() * chars.length);
        password += chars.charAt(randomIndex);
      }
      console.log(password)
      return password;
    },
    sendPasswordEmail(email, password) {
      // Function to send an email with the generated password to the manager's email
      // Implement your email sending logic here (using an email service or backend endpoint)
      // For demonstration purposes, we'll simply log the email and password here.
      console.log('Sending email to:', email);
      console.log('Generated password:', password);
    },
    },
  };
  </script>
  
  <style scoped>
  /* Your component's CSS styles go here */
  .create-manager-container {
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

  
  .create-manager-form {
    display: grid;
    gap: 10px;
  }
  
  .create-manager-form label {
    font-weight: bold;
    color:#fff;
  }
  
  .create-manager-form input,
  .create-manager-form select,
  .create-manager-form textarea {
    width: 100%;
    padding: 5px;
    font-size: 16px;
    border: 1px solid #ccc;
    background-color:aliceblue;
    border-radius: 4px;
    
  }
  
  .create-manager-form textarea {
    resize: vertical;
  }
  
  .create-manager-form button {
    background-color: #007bff;
    color: #fff;
    padding: 10px 20px;
    border: none;
    border-radius: 4px;
    font-size: 16px;
    cursor: pointer;
  }
  
  .create-manager-form button:hover {
    background-color: #0056b3;
  }
  
  .create-manager-form button:active {
    background-color: #00418a;
  }
  
  </style>
  