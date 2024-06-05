<script setup lang="ts">
import { defineProps, type PropType, ref } from 'vue';
import { type Question, type Answer } from '@/types';

const props = defineProps({
	question: {
		type: Object as PropType<Question>,
		required: true
	},
	answers: {
		type: Array as PropType<Answer[]>,
		required: true
	}
});

const selectedCategory = ref('');
const options = ref(props.answers.map(answer => answer.label));
</script>

<template>
  <div class="quizz-card">
    <div class="question">
      {{ question.label }}
    </div>
    <VueSelectButton v-model="selectedCategory" :options="options" aria-labelledby="basic" />
  </div>
</template>

<style scoped>
</style>
