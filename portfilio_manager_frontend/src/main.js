import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import axios from 'axios';
import '@fortawesome/fontawesome-free/css/all.css';


const app = createApp(App);
app.use(router);
app.config.globalProperties.$http = axios; // Set Axios as a global property

app.mount('#app');
