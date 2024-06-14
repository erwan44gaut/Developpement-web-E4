<script setup lang="ts">
import { type Question } from '@/types';
import { onMounted, ref } from 'vue';
import { getQuestionByPosition, getTotalNumberOfQuestions } from '@/services/QuizApiService';
import EditorCard from './EditorCard.vue';

const currentQuestion = ref<Question | null>(null);
const currentQuestionPosition = ref<number>(1);
const totalNumberOfQuestions = ref<number>(0);

const loadQuestionByPosition = async (position: number) => {
	try {
		currentQuestion.value = await getQuestionByPosition(position);
	} catch (error) {
		console.error('Error loading question:', error);
	}
};

onMounted(async () => {
	try {
		totalNumberOfQuestions.value = await getTotalNumberOfQuestions();
		await loadQuestionByPosition(currentQuestionPosition.value);
	} catch (error) {
		console.error('Error initializing quiz:', error);
	}
});
</script>

<template>
  <div class="editor-grid">
    <EditorCard class="question" v-if="currentQuestion" :question="currentQuestion" />
  </div>
  <div></div>
</template>

<style scoped>
.editor-grid {
  display: grid;
  gap: 10px;
}

.question {
  border: 1px solid rgba(0, 0, 0, 0.8);
  text-align: center;
  padding: 10px;
}
</style>
