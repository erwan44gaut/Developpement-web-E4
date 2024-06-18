<!-- eslint-disable vue/no-mutating-props -->
<script setup lang="ts">
import { deleteQuestion, updateQuestion } from '@/services/QuizApiService';
import { type Answer, type Question } from '@/types';
import { defineEmits, defineProps, ref } from 'vue';

const props = defineProps<{ 
    question: Question | null,
    totalNumberOfQuestions: number
}>();
const editingAnswerId = ref<number | null>(null);
const newPosition = ref<number | null>(props.question?.position ?? 0);
const emits = defineEmits(['refresh-delete-question', 'refresh-change-position']);

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

const deleteQuestionEvent = () => {
	if (props.question) {
		deleteQuestion(props.question);
		emits('refresh-delete-question', props.question);
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
</script>

<template>
<div class="card">
    <div class="question">
      <h2>{{ question?.title }}</h2>
      <h3>{{ question?.text }}</h3>
      <div class="position">
            <p>Position</p>
            <VueInputText type="number" v-model.number="newPosition" :min="1" :max="props.totalNumberOfQuestions" class="nes-input"></VueInputText>
            <p>/{{ props.totalNumberOfQuestions }}</p>
            <i class="pi pi-check" @click="updatePosition()"></i>
      </div>
    <div class="image">
        <p>Image</p>
        <VueInputText :value="question?.image" class="nes-input"/>
        <i class="pi pi-check" @click="updatePosition()"></i>
    </div>
    <div class="answers">
      <div class="answer" v-for="answer in question?.possibleAnswers" :key="answer.answer_id">
        <div class="answer-text">
          <div v-if="editingAnswerId === answer.answer_id" class="foo">
            <VueInputText type="text" v-model="answer.text" class="nes-input"/>
            <i class="pi pi-check" @click="saveAnswer(answer.answer_id, answer.text)"></i>
          </div>
          <template v-else>
            {{ answer.text }}
            <i v-if="answer.isCorrect" class="pi pi-check-circle" id="right-answer-indicator"></i>
          </template>
        </div>
        <div class="icons">
          <i id="select-right-answer" class="pi pi-check-circle" :value="answer.answer_id" @click="setCorrectAnswer(answer.answer_id)"></i>
          <i class="pi pi-pencil" @click="startEditing(answer.answer_id)"></i>
          <i class="pi pi-trash" @click="deleteAnswer(answer.answer_id)"></i>
        </div>
      </div>
    </div>
    <div class="add-answer">
        <VueButton @click="addAnswer" class="add-button nes-btn is-primary">Add answer</VueButton>
        <VueButton @click="deleteQuestionEvent()" severity="danger" class="delete-button nes-btn is-error">Delete question</VueButton>
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
  gap: 2em;
  margin-left: auto;
}

.add-answer {
    display: flex;
    flex-direction: column;
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

#select-right-answer {
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

#select-right-answer:hover {
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
</style>
