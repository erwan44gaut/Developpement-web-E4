<script setup lang="ts">
import { type Quizz } from '@/types';
import { defineProps, type PropType } from 'vue';
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
	</div>
</template>

<style scoped>
</style>
