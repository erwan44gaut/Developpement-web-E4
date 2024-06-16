import { createRouter, createWebHistory } from 'vue-router';
import AdminView from '../views/AdminView.vue';
import LeadboardView from '../views/LeadboardView.vue';
import LoginView from '../views/LoginView.vue';
import PlayView from '../views/PlayView.vue';

const routes = [
	{ path: '/', redirect: '/play' },
	{ path: '/play', component: PlayView, name: 'play' },
	{ path: '/leadboard', component: LeadboardView, name: 'leadboard' },
	{ path: '/admin', component: AdminView, name: 'admin' },
	{ path: '/login', component: LoginView, name: 'login' },
];

const router = createRouter({
	history: createWebHistory(),
	routes,
});

export default router;
