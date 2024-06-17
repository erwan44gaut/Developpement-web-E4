<script setup lang="ts">
import { createQuestion, getQuizInfo } from '@/services/QuizApiService';
import { type Question } from '@/types';
import { defineEmits, onMounted, ref } from 'vue';

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
    <div class="add" @click="dialogVisible = true">
      <span class="add-text">Add new question</span>
      <i class="pi pi-plus"></i>
    </div>

    <VueDialog header="Add Question" v-model:visible="dialogVisible" :modal="true" :closable="false">
      <div class="dialog">
        <label for="title">Title</label>
        <VueInputText id="title" v-model="newQuestion.title"/>

        <label for="text">Text</label>
        <VueInputText id="text" v-model="newQuestion.text"/>

        <label for="image">Image URL</label>
        <VueInputText id="image" v-model="newQuestion.image"/>

        <label for="position">Position</label>
        <VueInputText id="position" v-model="newQuestion.position" disabled/>

        <div v-for="(answer, index) in newQuestion.possibleAnswers" :key="answer.answer_id" class="answer-container">
          <label :for="'answer-' + index">Answer {{ index + 1 }}</label>
          <div class="answer-input">
            <VueInputText :id="'answer-' + index" v-model="answer.text" class="answer-text" />
            <VueRadioButton :value="answer.answer_id" v-model="correctAnswerId" />
            <i class="pi pi-trash" @click="removeAnswer(answer.answer_id)"></i>
          </div>
        </div>

        <VueButton label="Add Answer" @click="addAnswer" class="mb-3" />
      </div>
      <p class="info">Click on one of the radio buttons, to select the right answer.</p>

      <template #footer>
        <div class="footer-buttons">
          <VueButton label="Cancel" icon="pi pi-times" class="cancel-button" severity="danger" @click="dialogVisible = false" />
          <VueButton label="Save" icon="pi pi-check" class="save-button" @click="saveQuestion" />
        </div>
      </template>
    </VueDialog>
  </div>
</template>

<style scoped>
.add {
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  background-color: rgba(16, 185, 129, 0.7);
  color: white;
  border-radius: 10px;
  width: 100%;
  height: 100%;
  cursor: pointer;
}

.add:hover {
  background-color: rgba(16, 185, 129, 1);
  border: 1px solid white;
}

i.pi.pi-plus {
  font-size: 24px;
}

.pi.pi-trash {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 40px;
  height: 40px;
  color: red;
}

.pi.pi-trash:hover {
  background-color: red;
  border-radius: 100%;
  color: white;
}

.answer-text {
  flex-grow: 1;
  margin-right: 1em;
}

.add-text {
  margin-right: 1em;
}

.dialog {
  display: flex;
  flex-direction: column;
}

.answer-container {
  margin-bottom: 1em;
}

.answer-input {
  display: flex;
  align-items: center;
  gap: 1em;
}

.footer-buttons {
  display: flex;
  width: 100%;
}

.cancel-button, .save-button {
  flex: 1;
  width: 100%;
}

.cancel-button {
	margin-right: 0.5em;
}

.info {
  color: red;
  font-size: 0.8em;
  
}
</style>
