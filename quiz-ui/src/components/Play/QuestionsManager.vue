<template>
  <div>
    <h1>Question {{ currentQuestionPosition }} / {{ totalNumberOfQuestions }}</h1>
    <QuestionDisplay :question="currentQuestion" @answer-clicked="answerClickedHandler" />
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import QuestionDisplay from '../components/QuestionDisplay.vue';
import { getTotalNumberOfQuestions, getQuestionByPosition } from '../services/QuizApiService.ts';
import { type Question } from '@/types';

// Variables réactives
const currentQuestion = ref<Question | null>(null);
const currentQuestionPosition = ref<number>(1);
const totalNumberOfQuestions = ref<number>(0);

// Fonction pour charger une question en fonction de sa position
const loadQuestionByPosition = async (position: number) => {
  try {
    currentQuestion.value = await getQuestionByPosition(position);
  } catch (error) {
    console.error("Error loading question:", error);
  }
};

// Gestionnaire de clic de réponse
const answerClickedHandler = (index: number) => {
  console.log("Answer clicked:", index);
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
    totalNumberOfQuestions.value = await getTotalNumberOfQuestions();
    await loadQuestionByPosition(currentQuestionPosition.value);
  } catch (error) {
    console.error("Error initializing quiz:", error);
  }
});
</script>