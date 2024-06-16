<script setup lang="ts">
import { ref } from 'vue';
import { createQuestion } from '@/services/QuizApiService';
import { type Question } from '@/types';

const dialogVisible = ref(false);

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
	try {
		newQuestion.value.possibleAnswers.forEach(answer => {
			answer.isCorrect = (answer.answer_id === correctAnswerId.value);
		});
		await createQuestion(newQuestion.value);
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
</script>

<template>
  <div>
    <div class="add" @click="dialogVisible = true">
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
		<VueInputText type="number" id="position" v-model="newQuestion.position"/>

        <div v-for="(answer, index) in newQuestion.possibleAnswers" :key="answer.answer_id" class="answer-container">
          <label :for="'answer-' + index">Answer {{ index + 1 }}</label>
          <div class="answer-input">
            <VueInputText :id="'answer-' + index" v-model="answer.text" class="w-full mr-2"/>
            <VueRadioButton :value="answer.answer_id" v-model="correctAnswerId" class="mr-2" />
            <i class="pi pi-trash" @click="removeAnswer(answer.answer_id)"></i>
          </div>
        </div>

        <VueButton label="Add Answer" @click="addAnswer" class="mb-3" />
      </div>
      <p class="info">Click on one of the radio buttons, to select</p>
      <p class="info">the right answer.</p>

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
  background-color: #10B981;
  color: white;
  border-radius: 10px;
  width: 100%;
  height: 50px;
  cursor: pointer;
}

.add:hover {
  background-color: white;
  color: #10B981;
  border: 1px solid #10B981;
}

i.pi.pi-plus {
  font-size: 24px;
}

.pi.pi-trash {
  color: red;
  cursor: pointer;
}

.dialog {
  display: flex;
  flex-direction: column;
}

.answer-container {
  margin-bottom: 10px;
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
