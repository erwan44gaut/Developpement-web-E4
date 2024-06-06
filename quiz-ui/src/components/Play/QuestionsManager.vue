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
import { getTotalNumberOfQuestions, getQuestionByPosition } from '../../services/QuizApiService.ts';
import { type Question } from '@/types';

// Variables réactives
const currentQuestion = ref<Question | null>(null);
const currentQuestionPosition = ref<number>(1);
const totalNumberOfQuestions = ref<number>(0);

// Fonction pour charger une question en fonction de sa position
const loadQuestionByPosition = async (position: number) => {
  try {
    currentQuestion.value = await getQuestionByPosition(position);
    console.log(currentQuestion.value);
  } catch (error) {
    console.error("Error loading question:", error);
  }
};

// Gestionnaire de clic de réponse
const answerClickedHandler = (answerId: number) => {
  console.log("Answer clicked:", answerId);
  if (currentQuestionPosition.value < totalNumberOfQuestions.value) {
    currentQuestionPosition.value++;
    loadQuestionByPosition(currentQuestionPosition.value);
  } else {
    endQuiz();
  }
};

// Fonction pour terminer le quiz
const endQuiz = () => {
  console.log("Quiz ended");
  // Logique pour terminer le quiz
};

// Initialisation du composant
onMounted(async () => {
  try {
    console.log("a");
    totalNumberOfQuestions.value = await getTotalNumberOfQuestions();
    console.log(totalNumberOfQuestions.value);
    console.log("b");
    await loadQuestionByPosition(currentQuestionPosition.value);
  } catch (error) {
    console.log("c");
    console.error("Error initializing quiz:", error);
  }
});
</script>