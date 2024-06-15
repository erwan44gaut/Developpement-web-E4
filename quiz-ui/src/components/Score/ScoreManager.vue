<template>
    <div>
      <h1>Félicitations!</h1>
      <p>Vous avez terminé le quiz avec succès.</p>
      <div v-if="savedScore === null">
        <input v-model="playerName" placeholder="Entrez votre nom" />
        <button @click="savePlayerScore">Confirmer</button>
      </div>
      <div v-else>
        <p>Votre nom : {{ playerName }}</p>
        <p>Votre score : {{ savedScore }}</p>
      </div>
    </div>
  </template>
  
<script setup lang="ts">
import { ref, defineProps, defineEmits } from 'vue';
import { saveScore } from '../../services/QuizApiService';
import { type Participation } from '@/types';
  
// Définir les props
const props = defineProps<{ answerPositions: number[] }>();
  
// Définir les événements émis
const emit = defineEmits(['user-confirmed']);
  
const playerName = ref<string>('');
const savedScore = ref<number | null>(null);
  
// Fonction pour sauvegarder le score
const savePlayerScore = async () => {
	if (playerName.value.trim() === '') {
		alert('Veuillez entrer un nom');
		return;
	}
  
	const participation: Participation = {
		answers: props.answerPositions,
		playerName: playerName.value
	};
  
	try {
		const score = await saveScore(participation);
		savedScore.value = score;
		emit('user-confirmed');
	} catch (error) {
		console.error('Failed to save score', error);
	}
};
</script>
  