<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router';

const playRefresh = () => {
  window.location.href = "/play";
};

</script>

<template>
	<div class="app">
		<div class="header">
			<nav class="link">
				<!-- <RouterLink to="/">Home</RouterLink> -->
				<div class="nav-item">
					<svg class="nav-icon" width="30" height="30" fill="none" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
						<path d="M2 5h20v14H2V5zm18 12V7H4v10h16zM8 9h2v2h2v2h-2v2H8v-2H6v-2h2V9zm6 0h2v2h-2V9zm4 4h-2v2h2v-2z" fill="black"/>
					</svg>
					<RouterLink to="/play" @click.prevent="playRefresh()">Jouer</RouterLink>
				</div>
				<div class="nav-item">
					<svg class="nav-icon" width="30" height="30" fill="none" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
						<path d="M5 3H3v18h18V3H5zm14 2v14H5V5h14zM9 11H7v6h2v-6zm2-4h2v10h-2V7zm6 6h-2v4h2v-4z" fill="black"/>
					</svg>
					<RouterLink to="/leadboard">Classement</RouterLink>
				</div>
				<div class="nav-item">
					<svg class="nav-icon" width="30" height="30" fill="none" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
						<path d="M3 3h18v18H3V3zm16 16V5H5v14h14zM14 7h-4v4h4V7zm1 6H9v2H7v2h2v-2h6v2h2v-2h-2v-2z" fill="black"/>
					</svg>
					<RouterLink to="/login">Administration</RouterLink>
				</div>
			</nav>
		</div>
		<div class="main">
			<div>
				<RouterView />
			</div>
		</div>
	</div>
</template>

<style scoped>

RouterView {
  margin: 0;
  padding: 0;
  width: 100%;
  height: 100%;
}

.header {
	width: 100%;
	height: 35px;
	background-color: var(--background-color);
}

.main {
  position: relative;
  flex: 1;
  width: 100%;
  overflow: hidden;
}

.main::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: url('world-map.png');
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  opacity: 0.5;
  z-index: -1;
}
.link {
	display: flex;
	justify-content: center;
	align-items: center;
	gap: 2em;
	font-size: large;
}

.nav-item {
	display: flex;
	align-items: center;
	gap: 0.5em;
}

.nav-icon {
	display: inline-block;
	vertical-align: middle;
}
</style>
