<template>
	<div>
		<h1>Félicitations, {{ playerName }}!</h1>
		<p>Votre score : {{ score }}</p>
	</div>
  </template>
  
<script setup lang="ts">
import { ref, defineProps, onMounted } from 'vue';
import { saveScore } from '../../services/QuizApiService';
import { type Participation } from '@/types';
  
const props = defineProps<{ playerName: string; answerPositions: number[] }>();
  
const score = ref<number | null>(null);
  
onMounted(async () => {
	const participation: Participation = {
		answers: props.answerPositions,
		playerName: props.playerName
	};
  
	try {
		score.value = await saveScore(participation);
	} catch (error) {
		console.error('Failed to save score', error);
	}
});
</script>
  