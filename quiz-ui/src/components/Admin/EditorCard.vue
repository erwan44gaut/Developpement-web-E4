<!-- eslint-disable vue/no-mutating-props -->
<script setup lang="ts">
import UploadImage from '@/components/Admin/UploadImage.vue';
import { deleteQuestion, updateQuestion } from '@/services/QuizApiService';
import { type Answer, type Question } from '@/types';
import { defineEmits, defineProps, ref } from 'vue';

const props = defineProps<{ 
    question: Question | null,
    totalNumberOfQuestions: number
}>();
const editingAnswerId = ref<number | null>(null);
const newPosition = ref<number | null>(props.question?.position ?? 0);
const newTitle = ref<string>(props.question?.title ?? '');
const newText = ref<string>(props.question?.text ?? '');
const emits = defineEmits(['refresh-delete-question', 'refresh-change-position', 'close']);
const imageAsb64 = ref<string | null>(props.question?.image ?? '');
const uploaded = ref<boolean>(props.question?.image != null && props.question?.image !== '');

const startEditing = (answer_id: number) => {
	editingAnswerId.value = answer_id;
};

const stopEditing = () => {
	editingAnswerId.value = null;
};

const saveAnswer = (answer_id: number, newText: string) => {
	if (newText === '') {
		alert('Answer cannot be empty');
		return;
	}
	if (props.question) {
		const answer = props.question.possibleAnswers.find(ans => ans.answer_id === answer_id);
		if (answer) {
			answer.text = newText;
		}
		updateQuestion(props.question);
	}
	stopEditing();
};

const addAnswer = () => {
	if (editingAnswerId.value !== null)
	{
		alert('Finish editing first answer before adding a new one.');
		return;
	}
	if (props.question) {
		const newAnswer: Answer = {
			answer_id: Date.now(),
			text: '',
			isCorrect: false,
		};
		props.question.possibleAnswers.push(newAnswer);
		startEditing(newAnswer.answer_id);
	}
};

const deleteAnswer = (answer_id: number) => {
	if (props.question) {
		props.question.possibleAnswers = props.question.possibleAnswers.filter(ans => 
			ans.answer_id !== answer_id
		);
		updateQuestion(props.question);
	}
};

const closeEvent = () => {
	if (editingAnswerId.value != null)
	{
		alert('Finish editing answer before closing.');
		return;
	}
	emits('close');
};

const deleteQuestionEvent = () => {
	if (props.question) {
		deleteQuestion(props.question);
		emits('refresh-delete-question', props.question);
		closeEvent();
	}
};

const updatePosition = () => {
	if (newPosition.value == null || newPosition.value < 1 || newPosition.value > props.totalNumberOfQuestions) {
		alert(`Value out of range, please enter value between 1 and ${ props.totalNumberOfQuestions}`);
		return;
	}
	if (props.question && newPosition.value !== null) {
		emits('refresh-change-position', props.question.id, newPosition.value);
	}
};

const setCorrectAnswer = (answer_id: number) => {
	if (props.question) {
		props.question.possibleAnswers.forEach(answer => {
			answer.isCorrect = (answer.answer_id === answer_id);
		});
		updateQuestion(props.question);
	}
};

const imageFileChangedHandler = (newImage: string) => {
	if (props.question) {
		uploaded.value = newImage !== '';
		props.question.image = newImage;
		imageAsb64.value = newImage;
		updateQuestion(props.question);
	}
};

const saveTitle = () => {
	if (props.question) {
		props.question.title = newTitle.value;
		updateQuestion(props.question);
	}
};

const saveText = () => {
	if (props.question) {
		props.question.text = newText.value;
		updateQuestion(props.question);
	}
};
</script>

<template>
<div modal headerless class="dialog">
    <div class="nes-container is-dark">
      <div class="title">
        <p>Titre:</p>
        <input type="text" v-model="newTitle" class="nes-input" placeholder="Titre de la question"/>
        <button class="nes-btn is-success" @click="saveTitle">Save</button>
        <br><br>
      </div>
      <div class="text">
        <p>Texte:</p>
        <textarea v-model="newText" class="nes-textarea" placeholder="Texte de la question"></textarea>
        <button class="nes-btn is-success" @click="saveText">Save</button>
      </div>
      <div class="position">
            <p>Position:</p>
            <input class="nes-input" style="width: 5rem;" type="number" v-model.number="newPosition" :min="1" :max="props.totalNumberOfQuestions"/>
            <p>/ {{ props.totalNumberOfQuestions }}</p>
            <button class="nes-btn is-success" @click="updatePosition()">Save</button>
      </div>
      <div class="image">
          <p>Image:</p>
          <UploadImage @file-change="imageFileChangedHandler" :fileDataUrl="imageAsb64"></UploadImage>
          <VueImage v-if="uploaded" :src="question?.image" alt="question image" width="100" height="100"></VueImage>
      </div>
      <br><br>
      <div class="answers">
        <p>Réponses:</p>
        <VueButton @click="addAnswer" class="add-button nes-btn is-primary">Ajouter une réponse</VueButton>
        <div class="answer" v-for="answer in question?.possibleAnswers" :key="answer.answer_id">
          <div class="answer-text">
            <div v-if="editingAnswerId === answer.answer_id" style="display: flex;">
              <input type="text" v-model="answer.text" class="nes-input"/>
              <button class="nes-btn is-success" @click="saveAnswer(answer.answer_id, answer.text)">Save</button>
            </div>
            <template v-else>
              - {{ answer.text }}
            </template>
          </div>
          <div class="icons">
            <button class="nes-btn is-primary" @click="startEditing(answer.answer_id)">Editer</button>
            <button :disabled="answer.isCorrect" :class="['nes-btn is-primary', {'is-disabled' : answer.isCorrect}]" id="select-right-answer" :value="answer.answer_id" @click="setCorrectAnswer(answer.answer_id)">Bonne réponse</button>
            <button class="nes-btn is-error" @click="deleteAnswer(answer.answer_id)">Supprimer</button>
          </div>
        </div>
      </div>
      <div class="add-answer">
          <button @click="deleteQuestionEvent()" severity="danger" class="delete-button nes-btn is-error">Supprimer la question</button>
          <button @click="closeEvent()" class="delete-button nes-btn">Fermer</button>
      </div>
    </div>
  </div>
</template>

<style scoped>
.card {
  border: 1px solid rgba(0, 0, 0, 0.8);
  text-align: center;
  padding: 10px;
  border-radius: 10px;
  background-color: rgba(255, 255, 255, 0.7);
}

.card:hover {
  background-color: rgba(255, 255, 255, 0.9);
}

.question {
  text-align: left;
  padding-left: 10px;
}

.answer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 10px 0;
}

.radio-answer {
  margin-right: 2em;
}

.answer-text {
  flex-grow: 1;
  margin-right: 1em;
}

.icons {
  display: flex;
  margin-left: auto;
}

.add-answer {
    display: flex;
    flex-direction: row;
    margin-top: 30px;
    gap: 1em;
}

.add-button, .delete-button {
    flex: 1;
    width: 100%;
}

input {
  width: 100%;
  box-sizing: border-box;
  padding: 5px;
}

.pi.pi-pencil {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 40px;
  height: 40px;
  border-radius: 100%;
  border: 1px solid #3C3C3C;
  color: #3C3C3C;
}

.pi.pi-pencil:hover {
  background-color: #3C3C3C;
  color: white;
}

.pi.pi-trash {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 40px;
  height: 40px;
  border-radius: 100%;
  border: 1px solid red;
  color: red;
}

.pi.pi-trash:hover {
  background-color: red;
  color: white;
}

.pi.pi-check {
    display: flex;
    align-items: center;
    justify-content: center;
    min-width: 40px;
    min-height: 40px;
    max-width: 40px;
    max-height: 40px;
    border-radius: 50%;
    border: 1px solid #10B981;
    color: #10B981;
}

.pi.pi-check:hover {
    background-color: #10B981;
    color: white;
}

.position, .image {
    display: flex;
    gap: 1em;
    align-items: baseline;
    margin-top: 0.5em;
}

#right-answer-indicator {
  color: #10B981;
}

/* ALEX */

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
  z-index: 9999;
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
