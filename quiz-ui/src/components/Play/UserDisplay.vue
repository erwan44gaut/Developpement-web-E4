<template>
  <div :class="['nes-container is-dark with-title', 'content', { 'fade': fadeOut }]">
    <p class="title">Préparation</p>
    <div style="display: flex; width: 100%; align-items: center;">
      <input type="text" v-model="playerName" class="nes-input" placeholder="Entrez votre nom" :disabled="isDisabled" @keyup.enter="selectUser"/>
      <button type="button" :class="['nes-btn is-primary', {'is-disabled': isDisabled || playerName === ''}]" @click="selectUser" :disabled="isDisabled || playerName === ''">Go!</button>
    </div>
    <div style="display: flex; justify-content: space-between; width: 100%;">
      <p style="margin-top: 2rem;">> {{ readyText }}</p>
      <AvatarSelector @avatar-selected="handleAvatarSelected"/>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, defineEmits, onMounted } from 'vue';
import AvatarSelector from './AvatarSelector.vue';

const playerName = ref<string>('');
const avatarName = ref<string>('');
const emit = defineEmits(['user-selected']);
const readyText = ref<string>('');
const isDisabled = ref<boolean>(false);
const fadeOut = ref<boolean>(false);

onMounted(() => {
	typeText(`¤¤¤¤¤¤¤¤¤¤Ecrivez votre nom pour débuter.¤¤¤¤¤ N'oubliez pas de choisir votre avatar.`, () => { });
});

const handleAvatarSelected = (name: string) => {
	avatarName.value = name;
};

const selectUser = () => {
	if (playerName.value.trim() === '') {
		return;
	}
	isDisabled.value = true;
	typeText(`OK ${playerName.value},¤¤¤ voyons voir de quoi vous êtes capables.¤¤¤¤¤¤¤¤¤¤`, () => {
		fadeOut.value = true;
		setTimeout(() => {
			emit('user-selected', { name: playerName.value, avatar: avatarName.value });
		}, 1000);
	});
};

const typeText = (text: string, callback: () => void) => {
	readyText.value = '';
	let index = 0;

	const type = () => {
		if (index < text.length) {
			if (text[index] === '¤') {
				index++;
				setTimeout(type, 100);
			} else if (text[index] === ' ') {
				readyText.value += text[index];
				index++;
				setTimeout(type, 0);
			} else {
				readyText.value += text[index];
				index++;
				setTimeout(type, 50);
			}
		} else {
			callback();
		}
	};

	type();
};
</script>

<style scoped>
.content {
display: flex;
flex-direction: column;
align-items: center;
margin: auto;
margin-top: 2em;
width: 80%;
transition: opacity 0.5s ease-in;
}

.fade {
opacity: 0;
}
</style>
