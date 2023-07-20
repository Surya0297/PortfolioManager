// src/services/api.js
import axios from 'axios';

const apiClient = axios.create({
  baseURL: 'http://localhost:5000', // Replace this with your backend API base URL
});

export default apiClient;
