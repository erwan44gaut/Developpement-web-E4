<script setup lang="ts">
import { type Quizz, } from '@/types';
import { ref } from 'vue';

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
	}
]);

const computingResult = ref(true);
</script>

<template>
    <VueTabView class="tab_view">
        <VueTabPanel header="Play Quizz">
            <VueQuizzManager :quizz-list="quizzList"></VueQuizzManager>
            <VueButton id="result-button" label="See my results" :disabled="computingResult"/>
        </VueTabPanel>
        <VueTabPanel header="Results">
        </VueTabPanel>
        <VueTabPanel header="Edit Quizz">
        </VueTabPanel>
    </VueTabView>
</template>

<style scoped>
#result-button {
    width: 100%;
    margin-top: 2em;
}
</style>
