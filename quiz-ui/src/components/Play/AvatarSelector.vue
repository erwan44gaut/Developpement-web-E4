<template>
    <div class="avatar-selector">
      <div
        v-for="avatar in avatars"
        :key="avatar.name"
        class="avatar-item"
        @click="selectAvatar(avatar)"
      >
        <Image :src="avatar.src" :alt="avatar.name" class="avatar-image"/>
        <p>{{ avatar.name }}</p>
      </div>
    </div>
  </template>
  
<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { defineEmits } from 'vue';
import Image from 'primevue/image';
  
  // Typage des avatars
  interface Avatar {
    src: string;
    name: string;
  }
  
const emit = defineEmits(['avatar-selected']);
const avatars = ref<Avatar[]>([]);
  
// Utilisation de import.meta.glob pour charger dynamiquement les images
const images = import.meta.glob('@/assets/avatars/*.png');
  
const fetchAvatars = async () => {
	const avatarList: Avatar[] = [];
	for (const path in images) {
		const module = await images[path]();
		const src = module.default;
		const name = path.split('/').pop()?.replace('.png', '') || '';
		avatarList.push({ src, name });
	}
	avatars.value = avatarList;
};
  
const selectAvatar = (avatar: Avatar) => {
	emit('avatar-selected', avatar.name);
};
  
onMounted(fetchAvatars);
</script>
  
<style scoped>
    .avatar-selector {
    display: flex;
    gap: 16px;
    flex-wrap: wrap;
    }
    .avatar-item {
    cursor: pointer;
    text-align: center;
    }
    .avatar-image {
    width: 100px;
    height: 100px;
    object-fit: cover;
    }
</style>
  