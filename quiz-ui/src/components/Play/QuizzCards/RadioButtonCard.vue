<script setup lang="ts">
import { defineProps, type PropType, ref } from 'vue';
import { type Question, type Answer } from '@/types';

defineProps({
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
</script>

<template>
  <div class="quizz-card">
    <div class="question">
      {{ question.text }}
    </div>
    <div class="answers" v-for="answer in answers" :key="answer.answer_id">
      <VueRadioButton class="radio" v-model="selectedCategory" name="dynamic" :value="answer.text" />
      <label>{{ answer.text }}</label>
    </div>
  </div>
</template>

<style scoped>
.answers {
  margin-bottom: 8px;
}

.radio {
  margin-right: 8px;
}
</style>
