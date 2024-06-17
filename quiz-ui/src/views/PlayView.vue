<template>
  <div>
    <Overlay @overlay-gone="handleOverlayGone"/>
    <div class="progress-bar-container">
			<progress class="nes-progress is-primary" :value="((currentQuestionPosition - 1) / totalNumberOfQuestions) * 100" max="100"></progress>
		</div>
    <UserDisplay v-if="overlayGone && !userSelected" @user-selected="handleUserSelected" />
    <QuestionsManager v-if="userSelected" @quiz-ended="handleQuizEnded" @questions-amount-received="SetupProgress" @question-number-changed="UpdateProgress" :playerName="playerName" :avatarName="avatarName"/>
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

const currentQuestionPosition = ref(0);
const totalNumberOfQuestions = ref(1);

const SetupProgress = (amount: number) =>
{
  totalNumberOfQuestions.value = amount;
};

const UpdateProgress = (position: number) =>
{
  currentQuestionPosition.value = position;
};

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

<style scoped>

.progress-bar-container
{
    display: flex;
    justify-content: center;
    align-content: center;
    align-items: center;
    top: 35px;
    position: fixed;
    z-index: 1;
    width: 100%;
    margin: 0;
    padding: 0 0.5rem;
    background-color: var(--background-color);
    padding-bottom: 0.5rem;
    border-bottom: 4px solid black;
}

.nes-progress{
  height: 30px;
}

</style>