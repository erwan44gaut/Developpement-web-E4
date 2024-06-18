<script setup lang="ts">
import { createQuestion, getQuizInfo } from '@/services/QuizApiService';
import { type Question } from '@/types';
import { defineEmits, onMounted, ref } from 'vue';
import Dialog from 'primevue/dialog';

const dialogVisible = ref(false);
const emits = defineEmits(['refresh-new-question']);

const quizInfo = async () => {
	try {
		const quizInfo = await getQuizInfo();
		newQuestion.value.position = quizInfo.size + 1;
	} catch (error) {
		console.error('Error creation question:', error);
	}
};

const newQuestion = ref<Question>({
	id: Date.now(),
	title: '',
	text: '',
	image: '',
	position: 0,
	possibleAnswers: [
		{ answer_id: Date.now() + 1, text: '', isCorrect: false },
		{ answer_id: Date.now() + 2, text: '', isCorrect: false }
	]
});

const correctAnswerId = ref<number | null>(null);

const addAnswer = () => {
	newQuestion.value.possibleAnswers.push({
		answer_id: Date.now(),
		text: '',
		isCorrect: false
	});
};

const removeAnswer = (answer_id: number) => {
	newQuestion.value.possibleAnswers = newQuestion.value.possibleAnswers.filter(
		(answer) => answer.answer_id !== answer_id
	);
	if (correctAnswerId.value === answer_id) {
		correctAnswerId.value = null;
	}
};

const setRightAnswer = (answer_id: number) => {
	correctAnswerId.value = answer_id;
};

const saveQuestion = async () => {
	if (newQuestion.value.title === '') {
		alert('Title cannot be empty');
		return;
	}
	if (newQuestion.value.text === '') {
		alert('Text cannot be empty');
		return;
	}
	if (newQuestion.value.image === '') {
		alert('Image URL cannot be empty');
		return;
	}
	if (newQuestion.value.possibleAnswers.length < 2) {
		alert('At least two answers are required');
		return;
	}
	if (!correctAnswerId.value) {
		alert('Please select the correct answer');
		return;
	}
	if (newQuestion.value.possibleAnswers.filter((answer) => answer.text === '').length > 0) {
		alert('Answers cannot be empty');
		return;
	}

	try {
		newQuestion.value.possibleAnswers.forEach(answer => {
			answer.isCorrect = (answer.answer_id === correctAnswerId.value);
		});
		await createQuestion(newQuestion.value);
		emits('refresh-new-question');
		dialogVisible.value = false;

		newQuestion.value = {
			id: Date.now(),
			title: '',
			text: '',
			image: '',
			position: 0,
			possibleAnswers: [
				{ answer_id: Date.now() + 1, text: '', isCorrect: false },
				{ answer_id: Date.now() + 2, text: '', isCorrect: false }
			]
		};
		correctAnswerId.value = null;
	} catch (error) {
		console.error('Error adding question:', error);
	}
};

onMounted(quizInfo);
</script>

<template>
  <div>
    <div class="add nes-btn is-success" @click="dialogVisible = true">
      <span class="add-text">Add new question</span>
    </div>

	<div v-if="dialogVisible" modal headerless class="dialog">
		<div class="nes-container is-dark">
			<label for="title">Title</label>
			<VueInputText class="nes-input is-dark" id="title" v-model="newQuestion.title"/>

			<label for="text">Text</label>
			<VueInputText class="nes-input is-dark" id="text" v-model="newQuestion.text"/>

			<label for="image">Image URL</label>
			<VueInputText class="nes-input is-dark" id="image" v-model="newQuestion.image"/>

			<label for="position">Position</label>
			<VueInputText class="nes-input is-dark" id="position" v-model="newQuestion.position" disabled/>
			
			<br><br><br>
			<h1 class="">Answers</h1>
			<p class="info nes-text is-primary">Select the right answer using the blue buttons.</p>
			<VueButton label="+ Add Answer" @click="addAnswer" class="nes-btn is-primary" style="width: 100%; text-align: left;"/>
			<br><br>
			<div v-for="(answer, index) in newQuestion.possibleAnswers" :key="answer.answer_id">
				<label :for="'answer-' + index">Answer {{ index + 1 }}</label>
				<div class="answer-input">
					<VueInputText :id="'answer-' + index" v-model="answer.text" class="nes-input is-dark answer-text"/>
					<button style="margin-left: 1rem;" :disabled="answer.answer_id == correctAnswerId" :class="['nes-btn is-primary', {'is-disabled' : answer.answer_id == correctAnswerId}]" @click="setRightAnswer(answer.answer_id)">Set as true</button>
					<button style="margin-left: 0.5rem;" class="nes-btn is-error" @click="removeAnswer(answer.answer_id)">Remove</button>
				</div>
			</div>
			<br>
			<div class="footer-buttons">
				<VueButton label="Cancel" class="nes-btn is-error" severity="danger" @click="dialogVisible = false" />
				<VueButton label="Save" class="nes-btn is-success" @click="saveQuestion" />
			</div>
		</div>
	</div>
  </div>
</template>

<style scoped>
.add {
  width: 100%;
  height: 100%;
}

.dialog
{
	padding: 0;
	margin: 0;
	position: fixed;
	top: 0;
	left: 0;
	width: 100%;
	height: 100%;
	background-color: rgba(0, 0, 0, 0.5);
	overflow: auto;
}

.nes-container {
	  margin: 10%;
}

.answer-input
{
	display: flex;
	flex-direction: row;
	justify-content: space-between;
	align-items: center;
}

.answer-text
{
	widows: 70%;
}

.nes-btn {
	white-space: nowrap;
}
</style>
