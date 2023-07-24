<template>
  <div class="table-container">
    <table class="resource-list">
      <!-- Table header -->
      <thead>
        <tr>
          <th colspan="5">
            <router-link to="/admin/dashboard" class="home-icon">
              <i class="fas fa-home" style="color: white;"></i>
                </router-link>
            <h1>Resource List</h1>
          </th>
        </tr>
        <tr>
          <th>Resource ID</th>
          <th>Name</th>
          <th>Description</th>
          <th>Status</th>
          <th>Actions</th>
        </tr>
      </thead>
      <!-- Table body -->
      <tbody>
        <tr v-for="resource in resources" :key="resource.resource_id">
          <td>{{ resource.resource_id }}</td>
          <td>{{ resource.name }}</td>
          <td>{{ resource.description }}</td>
          <td>{{ resource.status }}</td>
          <td>
            <router-link :to="`/resources/update/${resource.resource_id}`">Edit</router-link>
            <button @click="deleteResource(resource.resource_id)">Delete</button>
          </td>
        </tr>
        <tr>
          <td colspan="5">
            <router-link to="/resources/create" class="create-button">Create New Resource</router-link>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'ResourceList',
  data() {
    return {
      resources: [], // Placeholder for the list of resources
    };
  },
  created() {
    this.fetchResources();
  },
  methods: {
    fetchResources() {
      axios
        .get('http://localhost:5000/resources')
        .then((response) => {
          this.resources = response.data;
        })
        .catch((error) => {
          console.error('Error fetching resources:', error);
        });
    },
    deleteResource(resourceId) {
      axios
        .delete(`http://localhost:5000/resources/${resourceId}`)
        .then(() => {
          this.resources = this.resources.filter((resource) => resource.resource_id !== resourceId);
          console.log('Resource deleted successfully!');
        })
        .catch((error) => {
          console.error('Error deleting resource:', error);
        });
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
  border-radius: 10px;
}

.resource-list {
  
  width: 60%;
  border-collapse: collapse;
  background: linear-gradient(to bottom right, #836de5, #023B79);
  color: #fff;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  margin-top: 20px;
}

h1 {
  font-size: 24px;
  font-weight: bold;
  margin: 20px 0;
  text-align: center;
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

tr:hover {
  background-color: #007bff;
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
  font-size: 12px;
}

td button:hover {
  background-color: #0056b3;
}

td button:active {
  background-color: #00418a;
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
  font-size: 12px;
}

td a:hover {
  background-color: #0056b3;
}

td a:active {
  background-color: #00418a;
}

.create-button {
  width: 200px;
  text-align: center;
  display: block;

  padding: 10px;
  background-color: #007bff;
  color: #fff;
  text-decoration: none;
  border-radius: 4px;
  cursor: pointer;
  font-weight: bold;
  font-size: 14px;
}

.create-button:hover {
  background-color: #0056b3;
}

.create-button:active {
  background-color: #00418a;
}
</style>
