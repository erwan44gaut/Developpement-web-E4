<template>
	<div class="content">
		<QuestionDisplay v-if="currentQuestion" :questionNumberText="questionNumberText" :question="currentQuestion" @answer-clicked="answerClickedHandler" />
		<div v-else>Loading question...</div>
	</div>
  </template>
  
<script setup lang="ts">
import { type Question } from '@/types';
import { onMounted, ref, defineProps, defineEmits, computed } from 'vue';
import { getQuestionByPosition, getTotalNumberOfQuestions } from '../../services/QuizApiService';
import QuestionDisplay from './QuestionsDisplay.vue';
  
// Props
const props = defineProps<{ playerName: string }>();
  
// Variables réactives
const currentQuestion = ref<Question | null>(null);
const currentQuestionPosition = ref<number>(1);
const totalNumberOfQuestions = ref<number>(0);
const answerPositions = ref<number[]>([]);
const questionNumberText = computed(() => `Question ${currentQuestionPosition.value} / ${totalNumberOfQuestions.value}`);
  

// Émettre un événement lorsque le quiz est terminé
const emit = defineEmits(['quiz-ended']);
  
// Fonction pour charger une question en fonction de sa position
const loadQuestionByPosition = async (position: number) => {
	console.log('load new questions');
	try {
		currentQuestion.value = await getQuestionByPosition(position);
		console.log(currentQuestion.value);
	} catch (error) {
		console.error('Error loading question:', error);
	}
};
  
// Gestionnaire de clic de réponse
const answerClickedHandler = (answerIndex: number) => {
	answerPositions.value.push(answerIndex + 1); // Ajouter la position de la réponse à la liste
	console.log('Answer clicked at position:', answerIndex + 1);
	console.log('Current position : ', currentQuestionPosition.value);
	const nextPosition = currentQuestionPosition.value + 1;
	if (nextPosition <= totalNumberOfQuestions.value) {
		console.log('Load question position : ', nextPosition);
		loadQuestionByPosition(nextPosition);
		currentQuestionPosition.value += 1;
	} else {
		emit('quiz-ended', answerPositions.value);
	}
};
  
// Initialisation du composant
onMounted(async () => {
	try {
		totalNumberOfQuestions.value = await getTotalNumberOfQuestions();
		await loadQuestionByPosition(currentQuestionPosition.value);
	} catch (error) {
		console.error('Error initializing quiz:', error);
	}
});
</script>
  

<style scoped>

.content 
{
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  overflow: hidden;
}

</style>