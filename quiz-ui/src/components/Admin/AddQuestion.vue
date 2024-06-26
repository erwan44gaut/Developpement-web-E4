<script setup lang="ts">
import UploadImage from '@/components/Admin/UploadImage.vue';
import { createQuestion, getQuizInfo } from '@/services/QuizApiService';
import { type Question } from '@/types';
import { defineEmits, onMounted, ref } from 'vue';

const imageAsb64 = ref<string | null>('');
const dialogVisible = ref(false);
const emits = defineEmits(['refresh-new-question']);
const uploaded = ref(false);  // Changement ici

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

const imageFileChangedHandler = (newImage: string) => {
	uploaded.value = newImage !== '';
	newQuestion.value.image = newImage;
};

onMounted(quizInfo);
</script>

<template>
  <div>
    <div class="add nes-btn is-success" @click="dialogVisible = true">
      <span class="add-text">Ajouter une question</span>
    </div>

	<div v-if="dialogVisible" modal headerless class="dialog">
		<div class="nes-container is-dark">
			<label for="title">Titre</label>
			<VueInputText class="nes-input is-dark" id="title" v-model="newQuestion.title"/>

			<label for="text">Texte</label>
			<VueInputText class="nes-input is-dark" id="text" v-model="newQuestion.text"/>

			<label for="image">Image</label><br>
			<div style="display: flex; justify-content: space-between;">
				<div>
					<UploadImage @file-change="imageFileChangedHandler" :fileDataUrl="imageAsb64"></UploadImage>
				</div>
				<VueImage v-if="uploaded" :src="newQuestion.image" alt="question image" width="100"></VueImage>
			</div>
			<br> <br>
			
			<label for="position">Position</label>
			<VueInputText class="nes-input is-dark" id="position" v-model="newQuestion.position" disabled/>
			
			<br><br><br>
			<h1 class="">Réponses</h1>
			<p class="info nes-text is-primary">Selectionnez la bonne réponse en utilisant les boutons bleus.</p>
			<VueButton label="+ Ajouter une réponse" @click="addAnswer" class="nes-btn is-primary" style="width: 100%; text-align: left;"/>
			<br><br>
			<div v-for="(answer, index) in newQuestion.possibleAnswers" :key="answer.answer_id">
				<label :for="'answer-' + index">Réponse {{ index + 1 }}</label>
				<div class="answer-input">
					<VueInputText :id="'answer-' + index" v-model="answer.text" class="nes-input is-dark answer-text"/>
					<button style="margin-left: 1rem;" :disabled="answer.answer_id == correctAnswerId" :class="['nes-btn is-primary', {'is-disabled' : answer.answer_id == correctAnswerId}]" @click="setRightAnswer(answer.answer_id)">Bonne réponse</button>
					<button style="margin-left: 0.5rem;" class="nes-btn is-error" @click="removeAnswer(answer.answer_id)">Supprimer</button>
				</div>
			</div>
			<br>
			<div class="footer-buttons">
				<VueButton label="Annuler" class="nes-btn is-error" severity="danger" @click="dialogVisible = false" />
				<VueButton label="Créer" class="nes-btn is-success" @click="saveQuestion" />
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

#text, #title, #position, #image {
	margin-bottom: 2em;
}
</style>
