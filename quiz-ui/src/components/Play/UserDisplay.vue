<template>
    <div>
      <h1>Sélectionnez votre utilisateur</h1>
      <VueInputText v-model="playerName" placeholder="Entrez votre nom" />
      <VueButton label="Confirmer" @click="selectUser" />
    </div>
  </template>
  
<script setup lang="ts">
import { ref, defineEmits } from 'vue';
  
const playerName = ref<string>('');
const emit = defineEmits(['user-selected']);
  
const selectUser = () => {
	if (playerName.value.trim() === '') {
		alert('Veuillez entrer un nom');
		return;
	}
	emit('user-selected', playerName.value);
};
</script>