<script setup lang="ts">
import { type Question } from '@/types';
import { onMounted, ref } from 'vue';
import { getQuestionByPosition, getQuizInfo } from '@/services/QuizApiService';
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

const refreshQuestions = (question: Question) => {
	questions.value = questions.value.filter(q => q.id !== question.id);
	totalNumberOfQuestions.value -= 1;
};
</script>


<template>
	<div>
		<div class="editor-grid">
			<template v-for="question in questions" :key="question.id">
				<EditorCard 
				class="question" 
				:question="question"
				@refresh="refreshQuestions"
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
