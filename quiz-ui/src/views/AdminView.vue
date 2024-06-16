<script setup lang="ts">
import { useRouter } from 'vue-router';
import { onMounted } from 'vue';
import EditorManager from '@/components/Admin/EditorManager.vue';

const router = useRouter();

onMounted(() => {
	const token = sessionStorage.getItem('authToken');
	if (!token) {
		router.push('/login');
	}
});
</script>

<template>
  <div class="container">
    <EditorManager />
  </div>
</template>

<style scoped>
.container {
  max-height: 100vh;
  overflow-y: auto;
  padding: 10px;
}
</style>
