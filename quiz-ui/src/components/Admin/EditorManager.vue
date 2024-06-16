<script setup lang="ts">
import { type Question } from '@/types';
import { onMounted, ref } from 'vue';
import { getQuestionByPosition, getQuizInfo, updateQuestion } from '@/services/QuizApiService';
import EditorCard from './EditorCard.vue';
import AddQuestion from './AddQuestion.vue';

const questions = ref<Question[]>([]);
const totalNumberOfQuestions = ref<number>(0);

const loadQuestions = async () => {
	try {
		const quizInfo = await getQuizInfo();
		totalNumberOfQuestions.value = quizInfo.size;
		for (let i = 1; i <= totalNumberOfQuestions.value; i++) {
			const question = await getQuestionByPosition(i);
			if (question) {
				questions.value.push(question);
			}
		}
	} catch (error) {
		console.error('Error initializing quiz:', error);
	}
};

onMounted(loadQuestions);

const refreshDeleteQuestions = (question: Question) => {
	questions.value = questions.value.filter(q => q.id !== question.id);
	totalNumberOfQuestions.value -= 1;
};

const refreshChangePosition = async (id: number, newPosition: number) => {
	const oldPositionQuestion = questions.value.find(q => q.id === id);
	const targetPositionQuestion = questions.value.find(q => q.position === newPosition);

	if (oldPositionQuestion && targetPositionQuestion) {
		const oldPosition = oldPositionQuestion.position;
		oldPositionQuestion.position = newPosition;
		targetPositionQuestion.position = oldPosition;

		try {
			await updateQuestion(oldPositionQuestion);
			await updateQuestion(targetPositionQuestion);

			questions.value.sort((a, b) => a.position - b.position);
		} catch (error) {
			console.error('Error updating positions:', error);
		}
	}
};
</script>


<template>
	<div>
		<div class="editor-grid">
			<template v-for="question in questions" :key="question.id">
				<EditorCard 
				class="question" 
				:question="question"
				:totalNumberOfQuestions="totalNumberOfQuestions.valueOf()"
				@refresh-delete-question="refreshDeleteQuestions"
				@refresh-change-position="refreshChangePosition"
				/>
			</template>
			<AddQuestion />
		</div>
	</div>
  </template>
  

<style scoped>
.editor-grid {
	display: grid;
	gap: 10px;
	grid-template-columns: repeat(3, 1fr);
}

.question {
  border: 1px solid rgba(0, 0, 0, 0.8);
  text-align: center;
}

.question:hover {
	background-color: rgba(0, 0, 0, 0.02);
}
</style>
