<template>
  <div>
    <h1>Question {{ currentQuestionPosition }} / {{ totalNumberOfQuestions }}</h1>
    <QuestionDisplay v-if="currentQuestion" :question="currentQuestion" @answer-clicked="answerClickedHandler" />
    <div v-else>Loading question...</div>
  </div>
</template>

<script setup lang="ts">
<<<<<<< HEAD
=======
import { ref, onMounted } from 'vue';
import QuestionDisplay from './QuestionsDisplay.vue';
import { getTotalNumberOfQuestions, getQuestionByPosition } from '../../services/QuizApiService';
>>>>>>> 514e048737177fac95cd616b9198dd8bf3037738
import { type Question } from '@/types';
import { onMounted, ref } from 'vue';
import { getQuestionByPosition, getTotalNumberOfQuestions } from '../../services/QuizApiService';
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
<<<<<<< HEAD
const answerClickedHandler = (index: number) => {
	if (currentQuestionPosition.value < totalNumberOfQuestions.value) {
		currentQuestionPosition.value++;
		loadQuestionByPosition(currentQuestionPosition.value);
=======
const answerClickedHandler = (answerIndex: number) => {
	answerPositions.value.push(answerIndex + 1);// Ajouter la position de la réponse à la liste
	console.log('Answer clicked at position:', answerIndex + 1);
	console.log('Current position : ', currentQuestionPosition.value);
	const nextPosition = currentQuestionPosition.value + 1;
	if (nextPosition <= totalNumberOfQuestions.value) {
		console.log('Load question position : ', nextPosition);
		loadQuestionByPosition(nextPosition);
		currentQuestionPosition.value += 1;
>>>>>>> 514e048737177fac95cd616b9198dd8bf3037738
	} else {
		endQuiz();
	}
};


// Fonction pour terminer le quiz
const endQuiz = () => {
<<<<<<< HEAD
=======
	console.log('Quiz ended');
	console.log('Answer positions:', answerPositions.value); // Afficher les positions des réponses
>>>>>>> 514e048737177fac95cd616b9198dd8bf3037738
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