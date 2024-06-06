import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import PlayView from '../views/PlayView.vue';
import ScoreView from '@/views/ScoreView.vue';
import LeadboardView from '@/views/LeadboardView.vue';
import AdminView from '@/views/AdminView.vue';

const router = createRouter({
	history: createWebHistory(import.meta.env.BASE_URL),
	routes: [
		{
			path: '/',
			name: 'home',
			component: HomeView
		},
		{
			path: '/play',
			name: 'play',
			component: PlayView
		},
		{
			path: '/score',
			name: 'score',
			component: ScoreView
		},
		{
			path: '/leadboard',
			name: 'leadboard',
			component: LeadboardView
		},
		{
			path: '/admin',
			name: 'admin',
			component: AdminView
		},
	]
});

export default router;
