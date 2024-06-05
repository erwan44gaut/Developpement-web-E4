<script setup lang="ts">
import { type Quizz } from '@/types';
import { defineProps, type PropType } from 'vue';
import BoolCard from './QuizzCards/BoolCard.vue';
import CheckboxCard from './QuizzCards/CheckboxCard.vue';
import RadioButtonCard from './QuizzCards/RadioButtonCard.vue';

defineProps({
	quizzList: {
		type: Array as PropType<Quizz[]>,
		required: true
	}
});
</script>

<template>
	<div v-for="quizz in quizzList" :key="quizz.id">
		<div v-if="quizz.question.type === 1">
			<RadioButtonCard :question="quizz.question" :answers="quizz.answers"></RadioButtonCard>
		</div>
		<div v-else-if="quizz.question.type === 2">
			<CheckboxCard :question="quizz.question" :answers="quizz.answers"></CheckboxCard>
		</div>
		<div v-else-if="quizz.question.type === 3">
			<BoolCard :question="quizz.question" :answers="quizz.answers"></BoolCard>
		</div>
	</div>
</template>

<style scoped>
</style>
