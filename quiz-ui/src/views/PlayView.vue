<template>
  <div>
    <QuestionsManager v-if="!quizEnded" @quiz-ended="handleQuizEnded" />
    <ScoreManager v-if="quizEnded" :answerPositions="answerPositions" @user-confirmed="handleUserConfirmed" />
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import QuestionsManager from '../components/Play/QuestionsManager.vue';
import ScoreManager from '../components/Score/ScoreManager.vue';

const quizEnded = ref(false);
const answerPositions = ref<number[]>([]);

const handleQuizEnded = (answers: number[]) => {
	quizEnded.value = true;
	answerPositions.value = answers;
};

const handleUserConfirmed = () => {
	// Logic to handle after user confirmed, such as redirecting to ScoreView
	alert('User confirmed!');
};
</script>
