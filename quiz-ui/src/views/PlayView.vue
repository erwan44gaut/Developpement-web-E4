<template>
  <div>
    <Overlay @overlay-gone="handleOverlayGone"/>
    <UserDisplay v-if="overlayGone && !userSelected" @user-selected="handleUserSelected" />
    <QuestionsManager v-if="userSelected" @quiz-ended="handleQuizEnded" :playerName="playerName" :avatarName="avatarName"/>
    <ScoreDisplay v-if="quizEnded" :playerName="playerName" :avatarName="avatarName" :answerPositions="answerPositions" />
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
const avatarName = ref<string>('');
const answerPositions = ref<number[]>([]);
const overlayGone = ref(false);

const handleOverlayGone = () => {
	overlayGone.value = true;
};

const handleUserSelected = (data: { name: string, avatar: string }) => {
	playerName.value = data.name;
	avatarName.value = data.avatar;
	userSelected.value = true;
};

const handleQuizEnded = (answers: number[]) => {
	quizEnded.value = true;
	answerPositions.value = answers;
};
</script>
