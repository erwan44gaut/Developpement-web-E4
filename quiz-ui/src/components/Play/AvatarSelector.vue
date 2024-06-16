<template>
<div class="avatar-selector">
	<VueButton type="button" :class="['nes-btn is-primary']" @click="previousAvatar"><</VueButton>
	<AvatarDisplay v-if="currentAvatar" :src="currentAvatar.src" :name="currentAvatar.name" />
	<div v-else>Loading...</div>
	<VueButton type="button" :class="['nes-btn is-primary']" @click="nextAvatar">></VueButton>
</div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue';
import { defineEmits } from 'vue';
import AvatarDisplay from './AvatarDisplay.vue';
import { type Avatar } from '@/types';

const emit = defineEmits(['avatar-selected']);
const avatars = ref<Avatar[]>([]);
const currentIndex = ref(0);

const images = import.meta.glob('../../../public/avatars/*.png');

const fetchAvatars = async () => {
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
flex-direction: row;
align-items: center;
}
</style>
