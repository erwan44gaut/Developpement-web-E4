<template>
    <div class="avatar-selector">
      <VueButton icon="pi pi-chevron-up" @click="previousAvatar" />
      <AvatarDisplay v-if="currentAvatar" :src="currentAvatar.src" :name="currentAvatar.name" />
      <div v-else>Loading...</div>
      <VueButton icon="pi pi-chevron-down" @click="nextAvatar" />
    </div>
  </template>
  
<script setup lang="ts">
import { ref, computed, onMounted } from 'vue';
import { defineEmits } from 'vue';
import Button from 'primevue/button';
import AvatarDisplay from './AvatarDisplay.vue';
  
  // Typage des avatars
  interface Avatar {
    src: string;
    name: string;
  }
  
const emit = defineEmits(['avatar-selected']);
const avatars = ref<Avatar[]>([]);
const currentIndex = ref(0);
  
// Utilisation de import.meta.glob pour charger dynamiquement les images
const images = import.meta.glob('../../../public/avatars/*.png');
  
const fetchAvatars = async () => {
	console.log("BBBB");
	const avatarList: Avatar[] = [];
	for (const path in images) {
		const module = await images[path]();
		const src = module.default;
		const name = path.split('/').pop()?.replace('.png', '') || '';
		avatarList.push({ src, name });
	}
	avatars.value = avatarList;
	if (avatars.value.length > 0) {
		emit('avatar-selected', avatarList[currentIndex.value].name);
	}
};
  
const currentAvatar = computed(() => {
	console.log(images);
	console.log("a");
	console.log(avatars.value);
	return avatars.value.length > 0 ? avatars.value[currentIndex.value] : null;
});
  
const nextAvatar = () => {
	currentIndex.value = (currentIndex.value + 1) % avatars.value.length;
	emit('avatar-selected', avatars.value[currentIndex.value].name);
};
  
const previousAvatar = () => {
	currentIndex.value = (currentIndex.value - 1 + avatars.value.length) % avatars.value.length;
	emit('avatar-selected', avatars.value[currentIndex.value].name);
};
  
onMounted(fetchAvatars);
</script>
  
  <style scoped>
  .avatar-selector {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  </style>
  