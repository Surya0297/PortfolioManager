
  
  <template>
    <div class="create-manager-container">
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
          <label for="role">Role:</label>
          <select id="role" v-model="form.role" required>
            <option value="Administrator">Administrator</option>
            <option value="Viewer">Viewer</option>
          </select>
        </div>
        <div>
          <label for="bio">Bio:</label>
          <textarea id="bio" v-model="form.bio" required></textarea>
        </div>
        <div>
          <label for="start_date">Start Date:</label>
          <input type="date" id="start_date" v-model="form.start_date" required />
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
          role: '',
          bio: '',
          start_date: '',
          password: '',
        },
      };
    },
    methods: {
      createManager() {
        axios
          .post('http://localhost:5000/portfolio_managers', this.form)
          .then((response) => {
            // Handle the successful response, e.g., show a success message or redirect to the Portfolio Manager list page
            console.log('Portfolio Manager created successfully:', response.data);
            // Redirect the user to the Portfolio Manager list page
            this.$router.push('/portfolio_managers');

          })
          .catch((error) => {
            // Handle errors, e.g., show an error message to the user
            console.error('Error creating Portfolio Manager:', error);
          });
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
  