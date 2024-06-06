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
  <div class="container">
    <div class="question">
      <p>{{ question.label }}</p>
    </div>
    <div class="answers" v-for="answer in answers" :key="answer.id">
      <VueRadioButton v-model="selectedCategory" name="dynamic" :value="answer.label" />
      <label>{{ answer.label }}</label>
    </div>
  </div>
</template>

<style scoped>
.container {

}

.answers {
    display: flex;
    gap: 10px;
    padding-top: 5px;
}
</style>
