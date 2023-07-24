import { createRouter, createWebHistory } from 'vue-router';
import Index from './components/index.vue'; // Import the Index component (formerly LandingPage)
import LoginPage from './components/Login.vue';
import AdminDashboard from './components/AdminDashBoard.vue'
import PortfolioManagerList from './components/PortfolioManagerList.vue';
import CreatePortfolioManager from './components/CreatePortfolioManager.vue';
import UpdatePortfolioManager from './components/UpdatePortfolioManager.vue';
import ProjectList from './components/ProjectList.vue';
import CreateProject from './components/CreateProject.vue';
import UpdateProject from './components/UpdateProject.vue';
import TaskList from './components/TaskList.vue';
import TaskForm from './components/TaskForm.vue';
import ResourceList from './components/ResourceList.vue';
import ResourceCreate from './components/ResourceCreate.vue';
import ResourceUpdate from './components/ResourceUpdate.vue';
import AvailableProjects from './components/AvailableProjects.vue';
import AssignManager from './components/AssignManager.vue';
import AssignedProjectsList from './components/AssignedProjectsList.vue';
import ManagerDashboard from './components/ManagerDashBoard.vue'
import ProjectDetails from './components/ProjectDetails.vue'

// import apiClient from '../services/api';
const routes = [
  { path: '/', component: Index }, // Use Index as the landing page component
  { path: '/login', component: LoginPage },
  { path: '/admin/dashboard', component: AdminDashboard },
  { path: '/portfolio_managers', component: PortfolioManagerList },
  { path: '/create', component: CreatePortfolioManager },
  { path: '/update/:id', component: UpdatePortfolioManager },
  { path: '/projects', component: ProjectList },
  { path: '/projects/create', component: CreateProject },
  { path: '/projects/update/:projectId', component: UpdateProject, props: true },
  { path: '/tasks', component: TaskList },
  { path: '/tasks/create', component: TaskForm },
  { path: '/tasks/update/:id', component: TaskForm },
  { path: '/resources', component: ResourceList },
  { path: '/resources/create', component: ResourceCreate },
  { path: '/resources/update/:resourceId', component: ResourceUpdate, props: true },
  { path: '/projects/available', component: AvailableProjects },
  { path: '/manager/assigned-projects', component: AssignedProjectsList },
{ path: '/projects/assign/:projectId', component: AssignManager, props: true },
{ path: '/Manager/dashboard', component: ManagerDashboard },
{ path: '/projects/:project_id', component: ProjectDetails },

];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
