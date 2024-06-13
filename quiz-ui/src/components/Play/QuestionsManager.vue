<template>
  <div>
    <h1>Question {{ currentQuestionPosition }} / {{ totalNumberOfQuestions }}</h1>
    <QuestionDisplay v-if="currentQuestion" :question="currentQuestion" @answer-clicked="answerClickedHandler" />
    <div v-else>Loading question...</div>
  </div>
</template>

<script setup lang="ts">
import { type Question } from '@/types';
import { onMounted, ref } from 'vue';
import { getQuestionByPosition, getTotalNumberOfQuestions } from '../../services/QuizApiService';
import QuestionDisplay from './QuestionsDisplay.vue';

// Variables réactives
const currentQuestion = ref<Question | null>(null);
const currentQuestionPosition = ref<number>(1);
const totalNumberOfQuestions = ref<number>(0);

// Fonction pour charger une question en fonction de sa position
const loadQuestionByPosition = async (position: number) => {
	try {
		currentQuestion.value = await getQuestionByPosition(position);
	} catch (error) {
		console.error('Error loading question:', error);
	}
};

// Gestionnaire de clic de réponse
const answerClickedHandler = (index: number) => {
	if (currentQuestionPosition.value < totalNumberOfQuestions.value) {
		currentQuestionPosition.value++;
		loadQuestionByPosition(currentQuestionPosition.value);
	} else {
		endQuiz();
	}
};

// Fonction pour terminer le quiz
const endQuiz = () => {
	// Logique pour terminer le quiz
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