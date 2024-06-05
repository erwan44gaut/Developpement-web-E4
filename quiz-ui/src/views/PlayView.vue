<script setup lang="ts">
import QuizzManager from '@/components/Play/QuizzManager.vue';
import type { Quizz } from '@/types';

const quizzList: Quizz[] = ([
	{
		id: 1,
		question: {
			id: 1,
			label: 'What is the capital of France?',
			type: 1
		},
		answers: [
			{ id: 1, label: 'Paris', value: 1 },
			{ id: 2, label: 'London', value: 2 },
			{ id: 3, label: 'Berlin', value: 3 },
			{ id: 4, label: 'Madrid', value: 4 }
		]
	},
	{
		id: 2,
		question: {
			id: 2,
			label: 'What is 2 + 2?',
			type: 2
		},
		answers: [
			{ id: 5, label: '3', value: 1 },
			{ id: 6, label: '4', value: 2 },
			{ id: 7, label: '5', value: 3 },
			{ id: 8, label: '6', value: 4 }
		]
	},
	{
		id: 3,
		question: {
			id: 3,
			label: 'Is the earth flat?',
			type: 3
		},
		answers: [
			{ id: 9, label: 'True', value: 1 },
			{ id:10, label: 'False', value: 2 }
		]
	}
]);
</script>

<template>
  <main>
    <QuizzManager :quizzList="quizzList" />
  </main>
</template>
