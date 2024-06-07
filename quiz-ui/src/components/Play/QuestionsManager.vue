<template>
  <div>
    <h1>Question {{ currentQuestionPosition }} / {{ totalNumberOfQuestions }}</h1>
    <QuestionDisplay v-if="currentQuestion" :question="currentQuestion" @answer-clicked="answerClickedHandler" />
    <div v-else>Loading question...</div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import QuestionDisplay from './QuestionsDisplay.vue';
import { getTotalNumberOfQuestions, getQuestionByPosition } from '../../services/QuizApiService';
import { type Question } from '@/types';

// Variables réactives
const currentQuestion = ref<Question | null>(null);
const currentQuestionPosition = ref<number>(1);
const totalNumberOfQuestions = ref<number>(0);
const answerPositions = ref<number[]>([]);

// Fonction pour charger une question en fonction de sa position
const loadQuestionByPosition = async (position: number) => {
	try {
		currentQuestion.value = await getQuestionByPosition(position);
	} catch (error) {
		console.error('Error loading question:', error);
	}
};

// Gestionnaire de clic de réponse
const answerClickedHandler = (answerIndex: number) => {
	answerPositions.value.push(answerIndex + 1);// Ajouter la position de la réponse à la liste
	console.log('Answer clicked at position:', answerIndex + 1);
	const nextPosition = currentQuestionPosition.value + 1;
	if (nextPosition <= totalNumberOfQuestions.value) {
		loadQuestionByPosition(nextPosition);
	} else {
		endQuiz();
	}
};


// Fonction pour terminer le quiz
const endQuiz = () => {
	console.log('Quiz ended');
	console.log('Answer positions:', answerPositions.value); // Afficher les positions des réponses
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