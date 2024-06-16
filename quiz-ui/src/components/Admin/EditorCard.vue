<!-- eslint-disable vue/no-mutating-props -->
<script setup lang="ts">
import { updateQuestion, deleteQuestion } from '@/services/QuizApiService';
import { type Answer, type Question } from '@/types';
import { defineProps, ref, defineEmits } from 'vue';

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
</script>

<template>
<div class="card">
    <div class="question">
      <h3>{{ question?.title }}</h3>
      <p>{{ question?.text }}</p>
      <div class="position">
            <p>Position</p>
            <VueInputText type="number" v-model.number="newPosition" min="1" max="props.totalNumberOfQuestions"></VueInputText>
            <p>/{{ props.totalNumberOfQuestions }}</p>
            <i class="pi pi-check" @click="updatePosition()"></i>
      </div>
	<div class="image">
		<p>Image</p>
		<VueInputText :value="question?.image" />
		<i class="pi pi-check" @click="updatePosition()"></i>
    </div>
    <div class="answers">
      <div class="answer" v-for="answer in question?.possibleAnswers" :key="answer.answer_id">
        <div class="answer-text">
          <div v-if="editingAnswerId === answer.answer_id" class="foo">
            <VueInputText type="text" v-model="answer.text" />
            <i class="pi pi-check" @click="saveAnswer(answer.answer_id, answer.text)"></i>
          </div>
          <template v-else>
            {{ answer.text }}
          </template>
        </div>
        <div class="icons">
          <i class="pi pi-pencil" @click="startEditing(answer.answer_id)"></i>
          <i class="pi pi-trash" @click="deleteAnswer(answer.answer_id)"></i>
        </div>
      </div>
    </div>
    <div class="add-answer">
		<VueButton @click="addAnswer" class="add-button">Add answer</VueButton>
		<VueButton @click="deleteQuestionEvent()" severity="danger" outlined class="delete-button">Delete question</VueButton>
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

.answer-text {
  flex-grow: 1;
  margin-right: 1em;
}

.icons {
  display: flex;
  gap: 10px;
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
  color: #3C3C3C;
  cursor: pointer;
}

.pi.pi-trash {
  color: red;
  cursor: pointer;

}

.pi.pi-check {
    color: #10B981;
    cursor: pointer;
}

.position, .image {
    display: flex;
    gap: 1em;
    align-items: center;
    margin-top: 0.5em;
}
</style>
