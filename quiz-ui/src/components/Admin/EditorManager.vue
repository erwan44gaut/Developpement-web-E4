<script setup lang="ts">
import { getQuestionByPosition, getQuizInfo, updateQuestion } from '@/services/QuizApiService';
import { Question } from '@/types';
import { onMounted, ref } from 'vue';
import AddQuestion from './AddQuestion.vue';
import EditorCard from './EditorCard.vue';
import Dialog from 'primevue/dialog';
const questions = ref<Question[]>([]);
const totalNumberOfQuestions = ref<number>(0);
const isLoading = ref(true);
const selectedQuestion = ref<Question | null>(null);

const selectQuestion = (question: Question) =>
{
	selectedQuestion.value = question;
};

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
		isLoading.value = false;
	} catch (error) {
		console.error('Error initializing quiz:', error);
	}
};

onMounted(loadQuestions);

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

			totalRefresh();
		} catch (error) {
			console.error('Error updating positions:', error);
		}
	}
};

const totalRefresh = () => {
	isLoading.value = true;
	questions.value = [];
	loadQuestions();
	isLoading.value = false;
};


</script>

<template>
	<div>
		<div v-if="isLoading" class="loader-container">
			<VueProgressSpinner />
		</div>
		<Dialog :visible="selectedQuestion != null" modal :style="{ width: '25rem' }" class="editor-card-container nes-container is-dark" headerless>
            <template #container="{ closeCallback }">
                <div class="dialog-content">
					<EditorCard
						class="question"
						:question="selectedQuestion"
						:totalNumberOfQuestions="totalNumberOfQuestions.valueOf()"
						@refresh-delete-question="totalRefresh"
						@refresh-change-position="refreshChangePosition"
					/>
                </div>
            </template>
        </Dialog>
		<div class="editor-grid">
			<template v-for="question in questions" :key="question.id">
				<div class="question nes-btn" @click="selectQuestion(question)">
  					<span>{{ question?.position }} {{ question?.title }}</span>
				</div>
			</template>
			<AddQuestion 
				@refresh-new-question="totalRefresh"
			/>
		</div>
	</div>
</template>
  

<style scoped>
.loader-container {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(255, 255, 255, 0.7);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 9999;
}

.editor-grid {
	margin: 1rem;
	margin-top: 35px;
	display: flex;
	flex-direction: column;
}

.question
{
  width: 100%;
  text-align: left;
}

.editor-card-container 
{
  padding: 0;
}

</style>
