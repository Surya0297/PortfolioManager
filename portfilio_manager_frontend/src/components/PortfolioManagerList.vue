<template>
  <div class="table-container">
    
    <table class="portfolio-manager-list">
      <!-- Table header -->
      <thead>
        <tr>
          <th colspan="7">
            <router-link to="/admin/dashboard" class="home-icon">
      <i class="fas fa-home" style="color: white;"></i>
    </router-link>
            <h1>Portfolio Manager List</h1>
    <div class="search-form">
      <label for="searchManagerId">Search by Manager ID:  </label>
      <input
        type="text"
        id="searchManagerId"
        v-model="searchManagerId"
        @input="searchManagers"
        placeholder="Enter Manager ID"
      />
    </div>
          </th>
        </tr>
        <tr>
          <th>Manager ID</th>
          <th>Name</th>
          <th>UserName</th>
          <th>Status</th>
          <th>Bio</th>
          <th>Joining Date</th>
          <th>Actions</th>
        </tr>
      </thead>
      <!-- Table body -->
      <tbody>
        <tr v-for="manager in filteredManagers" :key="manager._id">
          <td>{{ manager.manager_id }}</td>
          <td>{{ manager.name }}</td>
          <td>{{ manager.username }}</td>
          <td>{{ manager.status }}</td>
          <td>{{ manager.bio }}</td>
          <td>{{ formatDate(manager.joining_date) }}</td>
          <td>
            <router-link :to="`/update/${manager.manager_id}`">Edit</router-link>
            <button @click="deleteManager(manager.manager_id)">Delete</button>
          </td>
        </tr>
        <tr>
          <td colspan="7">
            <router-link to="/create" class="create-button">Create New Portfolio Manager</router-link>
          </td>
        </tr>
      </tbody>
    </table>
    <div v-if="filteredManagers.length === 0">
      <p>No managers found.</p>
    </div>
    
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'PortfolioManagerList',
  data() {
    return {
      managers: [], // Placeholder for the list of Portfolio Managers
      searchManagerId: '',
    };
  },
  created() {
    this.fetchManagers();
  },
  computed: {
    filteredManagers() {
      // Filter the managers based on the entered searchManagerId
      return this.managers.filter((manager) =>
        manager.manager_id.includes(this.searchManagerId)
      );
    },
  },
  methods: {
    formatDate(date) {
      // Create a new Date object from the provided date string
      const formattedDate = new Date(date);

      // Extract the date components (day, month, year)
      const day = formattedDate.getDate();
      const month = formattedDate.getMonth() + 1; // Month starts from 0, so add 1
      const year = formattedDate.getFullYear();

      // Return the formatted date as a string (e.g., "DD/MM/YYYY")
      return `${day}/${month}/${year}`;
    },
    fetchManagers() {
      // Make a GET request to fetch all managers from the backend API
      axios
        .get('http://localhost:5000/portfolio_managers')
        .then((response) => {
          this.managers = response.data; // Update the local managers array with the data from the API
        })
        .catch((error) => {
          console.error('Error fetching managers:', error);
        });
    },
    deleteManager(managerId) {
      axios
        .delete(`http://localhost:5000/portfolio_managers/${managerId}`)
        .then(() => {
          // Remove the deleted manager from the local managers array
          this.managers = this.managers.filter((manager) => manager._id !== managerId);
          console.log('Portfolio Manager deleted successfully!');
          this.fetchManagers();
        })
        .catch((error) => {
          console.error('Error deleting manager:', error);
        });
    },
    searchManagers() {
      // Fetch all managers if the searchManagerId is empty
      if (!this.searchManagerId.trim()) {
        this.fetchManagers();
        return;
      }

      // Filter the managers based on the entered searchManagerId
      this.managers = this.managers.filter((manager) =>
        manager.manager_id.includes(this.searchManagerId)
      );
    },
  },
};
</script>

<style scoped>
/* Your component's CSS styles go here */
.table-container {
 
  margin-top: 100px;
  display: flex;
  flex-direction: column;
  align-items: center;
  height: 100vh;
  font-family: 'Franklin Gothic Medium';
}

.portfolio-manager-list {
  width: 60%;
  border-radius: 10px;
  border-collapse: collapse;
  background: linear-gradient(to bottom right, #836de5, #023b79);
  color: #fff;
}

.create-button {
  width: 300px;
  text-align: center;
  display: block;
 /* Add margin-top to create space between table and button */
  padding: 10px;
  background-color: #007bff;
  color: #fff;
  text-decoration: none;
  border-radius: 4px;
  cursor: pointer;
  font-weight: bold;
}

th,
td {
  padding: 10px;
  text-align: left;
  border-bottom: 1px solid #ddd;
  
}

th {
  font-weight: bold;
  
}

/* Styles for table cell buttons */
td button {
  display: inline-block;
  margin-right: 5px;
  padding: 5px 10px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-weight: bold;
}

td button:hover {
  background-color: #0056b3;
}

td button:active {
  background-color: #00418a;
}

input,select{
  width: 20%;
  height: 30px;
  border-radius: 5px;
}
/* Styles for router-link (Edit button) */
td a {
  display: inline-block;
  margin-right: 5px;
  padding: 5px 10px;
  background-color: #007bff;
  color: #fff;
  text-decoration: none;
  border-radius: 4px;
  cursor: pointer;
  font-weight: bold;
}

td a:hover {
  background-color: #0056b3;
}

td a:active {
  background-color: #00418a;
}



.create-button:hover {
  background-color:#0056b3; /* Darker green on hover */
}

.create-button:active {
  background-color: #1e7e34; /* Even darker green on active state */
}
 h1{
  text-align: center;
 }

</style>





  