<template>
  <div>
    <h1>Question {{ currentQuestionPosition }} / {{ totalNumberOfQuestions }}</h1>
    <QuestionDisplay v-if="currentQuestion" :question="currentQuestion" @answer-clicked="answerClickedHandler" />
    <div v-else>Loading question...</div>
  </div>
</template>

<script setup lang="ts">
import { type Question, type Participation } from '@/types';
import { onMounted, ref } from 'vue';
import { getQuestionByPosition, getTotalNumberOfQuestions, saveScore } from '../../services/QuizApiService';
import QuestionDisplay from './QuestionsDisplay.vue';

// Variables réactives
const currentQuestion = ref<Question | null>(null);
const currentQuestionPosition = ref<number>(1);
const totalNumberOfQuestions = ref<number>(0);
const answerPositions = ref<number[]>([]);

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
	answerPositions.value.push(answerIndex + 1);// Ajouter la position de la réponse à la liste
	console.log('Answer clicked at position:', answerIndex + 1);
	console.log('Current position : ', currentQuestionPosition.value);
	const nextPosition = currentQuestionPosition.value + 1;
	if (nextPosition <= totalNumberOfQuestions.value) {
		console.log('Load question position : ', nextPosition);
		loadQuestionByPosition(nextPosition);
		currentQuestionPosition.value += 1;
	} else {
		endQuiz();
	}
};


// Fonction pour terminer le quiz
const endQuiz = async () => {
	console.log('Quiz ended');
	console.log('Answer positions:', answerPositions.value); // Afficher les positions des réponses
	const participation: Participation = {
		answers: answerPositions.value,
		playerName: 'Thomas'
	};

	try {
		await saveScore(participation);
		console.log('Score saved successfully');
	} catch (error) {
		console.error('Failed to save score', error);
	}
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