<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router';

</script>

<template>
	<div class="header">
		<nav class="link">
			<RouterLink to="/">Home</RouterLink>
			<RouterLink to="/play">Play</RouterLink>
			<RouterLink to="/leadboard">Leadboard</RouterLink>
			<RouterLink to="/admin">Admin</RouterLink>
		</nav>
		<RouterView />
	</div>
</template>

<style scoped>
.header {
	position: fixed;
	top: 0;
	left: 0;
	width: 100%;
	background-color: var(--background-color);
}

.link {
	display: flex;
	justify-content: center;
	gap: 2em;
	font-size: large;
}
</style>
