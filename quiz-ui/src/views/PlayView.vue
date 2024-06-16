<template>
  <div>
    <Overlay />
    <UserDisplay v-if="!userSelected" @user-selected="handleUserSelected" />
    <QuestionsManager v-if="userSelected && !quizEnded" @quiz-ended="handleQuizEnded" :playerName="playerName" />
    <ScoreDisplay v-if="quizEnded" :playerName="playerName" :answerPositions="answerPositions" />
  </div>
</template>

<script setup lang="ts">
import Overlay from '@/components/Home/WelcomeOverlay.vue';
import { ref } from 'vue';
import UserDisplay from '../components/Play/UserDisplay.vue';
import QuestionsManager from '../components/Play/QuestionsManager.vue';
import ScoreDisplay from '../components/Play/ScoreDisplay.vue';

const userSelected = ref(false);
const quizEnded = ref(false);
const playerName = ref<string>('');
const answerPositions = ref<number[]>([]);

const handleUserSelected = (name: string) => {
	playerName.value = name;
	userSelected.value = true;
};

const handleQuizEnded = (answers: number[]) => {
	quizEnded.value = true;
	answerPositions.value = answers;
};
</script>
