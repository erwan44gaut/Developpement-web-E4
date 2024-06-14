<!-- eslint-disable vue/no-mutating-props -->
<script setup lang="ts">
import { ref } from 'vue';
import { defineProps } from 'vue';
import { type Question, type Answer } from '@/types';

const props = defineProps<{ question: Question | null }>();
const editingAnswerId = ref<number | null>(null);

const startEditing = (answer_id: number) => {
	editingAnswerId.value = answer_id;
};

const stopEditing = () => {
	editingAnswerId.value = null;
};

const saveAnswer = (answer_id: number, newText: string) => {
	if (props.question) {
		const answer = props.question.possibleAnswers.find(ans => ans.answer_id === answer_id);
		if (answer) {
			answer.text = newText;
		}
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
		props.question.possibleAnswers = props.question.possibleAnswers.filter(ans => ans.answer_id !== answer_id);
	}
};
</script>

<template>
<div class="card">
	<div class="question">
	<h3>{{ question?.title }}</h3>
	<p>{{ question?.text }}</p>
	</div>
	<div class="answers">
	<div class="answer" v-for="answer in question?.possibleAnswers" :key="answer.answer_id">
		<div class="answer-text">
		<template v-if="editingAnswerId === answer.answer_id">
			<input type="text" v-model="answer.text" @blur="saveAnswer(answer.answer_id, answer.text)" />
		</template>
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
	<VueButton outlined @click="addAnswer">Add answer</VueButton>
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
	padding-left: 10px;
  }
  
  .icons {
	display: flex;
	gap: 10px;
	margin-left: auto;
  }
  
  .add-answer {
	margin-top: 10px;
  }
  
  input {
	width: 100%;
	box-sizing: border-box;
	padding: 5px;
  }
  </style>
  
