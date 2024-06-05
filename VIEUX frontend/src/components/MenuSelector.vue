<script setup lang="ts">
import { type Quizz, } from '@/types';
import QuizzManager from './QuizzManager.vue';
import EditorManager from './Editor/EditorManager.vue';

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
    <VueTabView class="tab_view">
        <VueTabPanel header="Play Quizz">
			<div class="play-quizz">
				<QuizzManager :quizz-list="quizzList"></QuizzManager>
				<div class="play-quizz-footer">
					<VueButton label="Clear my answers" severity="danger" outlined/>
					<VueButton label="Validate my answers"/>
				</div>
			</div>
        </VueTabPanel>
        <VueTabPanel header="Results">
        </VueTabPanel>
        <VueTabPanel header="Edit Quizz">
			<!-- <EditorManager></EditorManager> -->
        </VueTabPanel>
    </VueTabView>
</template>

<style scoped>
.play-quizz {
	display: flex;
	flex-direction: column;
	align-items: center;
}

.play-quizz-footer {
  margin-top: 2em;
  width: 100%;
  display: flex;
  gap: 10px;
}

.play-quizz-footer > * {
  flex: 1;
}
</style>
