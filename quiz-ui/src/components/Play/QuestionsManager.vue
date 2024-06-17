<template>
	<div class="content">
		<transition name="fade" mode="out-in">
			<QuestionDisplay v-if="currentQuestion" :key="currentQuestion.id" :questionNumberText="questionNumberText" :question="currentQuestion" @answer-clicked="answerClickedHandler" />
			<div v-else>Loading question...</div>
		</transition>
	</div>
	</template>
  
<script setup lang="ts">
import { type Question } from '@/types';
import { onMounted, ref, defineProps, defineEmits, computed } from 'vue';
import { getQuestionByPosition, getTotalNumberOfQuestions } from '../../services/QuizApiService';
import QuestionDisplay from './QuestionsDisplay.vue';
  
// Props
const props = defineProps<{ avatarName: string; playerName: string }>();
  
// Variables réactives
const currentQuestion = ref<Question | null>(null);
const currentQuestionPosition = ref<number>(1);
const totalNumberOfQuestions = ref<number>(0);
const answerPositions = ref<number[]>([]);
const questionNumberText = computed(() => `Question ${currentQuestionPosition.value} / ${totalNumberOfQuestions.value}`);
  

// Émettre un événement lorsque le quiz est terminé
const emit = defineEmits(['quiz-ended']);
  
// Fonction pour charger une question en fonction de sa position
const loadQuestionByPosition = async (position: number) => {
	try {
		currentQuestion.value = null; // Trigger the animation
		setTimeout(async () => {
			currentQuestion.value = await getQuestionByPosition(position);
		}, 0); // Delay to ensure the transition occurs
	} catch (error) {
		console.error('Error loading question:', error);
	}
};

  
// Gestionnaire de clic de réponse
const answerClickedHandler = (answerIndex: number) => {
	answerPositions.value.push(answerIndex + 1); // Ajouter la position de la réponse à la liste
	const nextPosition = currentQuestionPosition.value + 1;
	if (nextPosition <= totalNumberOfQuestions.value) {
		loadQuestionByPosition(nextPosition);
		currentQuestionPosition.value += 1;
	} else {
		emit('quiz-ended', answerPositions.value);
	}
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
  

<style scoped>

.content 
{
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  overflow: hidden;
}

.fade-enter-active {
  transition: opacity 0.25s;
}

.fade-enter-from {
  opacity: 0;
}

.fade-leave-active {
  transition: opacity 0.25s;
}

.fade-leave-to {
  opacity: 0;
}

</style>