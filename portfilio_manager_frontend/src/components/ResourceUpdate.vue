<template>
  <div class="resource-form">
    <router-link to="/admin/dashboard" class="home-icon">
              <i class="fas fa-home" style="color: white;"></i>
                </router-link>
    <h1>Update Resource</h1>
    <form @submit.prevent="handleSubmit">
      <div class="form-group">
        <label for="name">Resource Name:</label>
        <input v-model="formData.name" type="text" id="name" required />
      </div>
      <div class="form-group">
        <label for="description">Resource Description:</label>
        <textarea v-model="formData.description" id="description" required></textarea>
      </div>
      <div class="form-group">
        <label for="status">Resource Status:</label>
        <select v-model="formData.status" id="status" required>
          <option value="Available">Available</option>
          <option value="Unavailable">Unavailable</option>
        </select>
      </div>
      <button type="submit">Update</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'ResourceUpdate',
  props: {
    resourceId: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      formData: {
        name: '',
        description: '',
        status: 'available',
      },
    };
  },
  created() {
    this.fetchResource();
  },
  methods: {
    fetchResource() {
      axios
        .get(`http://localhost:5000/resources/${this.resourceId}`)
        .then((response) => {
          this.formData = response.data;
        })
        .catch((error) => {
          console.error('Error fetching resource:', error);
        });
    },
    handleSubmit() {
      axios
        .put(`http://localhost:5000/resources/${this.resourceId}`, this.formData)
        .then(() => {
          console.log('Resource updated successfully!');
          this.$router.push('/resources');
        })
        .catch((error) => {
          console.error('Error updating resource:', error);
        });
    },
  },
};
</script>

<style scoped>
/* Your custom styles for the form */

.resource-form {
  max-width: 500px;
  margin: 100px auto;
  padding: 20px;
  border: 1px solid #ccc;
  background: linear-gradient(to bottom right, #836de5, #023B79);
  border-radius: 8px;
  color: #fff;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

h1 {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 20px;
  text-align: center;
}

form {
  display: flex;
  flex-direction: column;
  padding :10px
}

label {
  font-weight: bold;
  margin-bottom: 5px;
}

input[type="text"],
textarea,
select {
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  margin-bottom: 15px;
  font-size: 16px;
  width: 100%;
}

textarea {
  resize: vertical;
}

button {
  width:100px;
  padding: 10px;
  background-color: #00418a;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-weight: bold;
  transition: background-color 0.2s ease;

}

button:hover {
  background-color: #0056b3;
}

button:active {
  background-color: #00418a;
}
</style>
