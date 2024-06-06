<template>
    <div>
      <h2>{{ question.text }}</h2>
      <img v-if="question.image" :src="question.image" alt="Question Image" />
      <div v-for="answer in question.possibleAnswers" :key="answer.answer_id" class="answers">
        <VueRadioButton v-model="selectedAnswer" :value="answer" @change="selectAnswer(answer)" />
        <label>{{ answer.text }}</label>
      </div>
    </div>
  </template>
  
  <script setup lang="ts">
  import { ref, defineProps, defineEmits } from 'vue';
  import { type Question, type Answer } from '@/types';
  
  const props = defineProps<{ question: Question }>();
  const emit = defineEmits(['answer-clicked']);
  const selectedAnswer = ref<Answer | null>(null);
  
  const selectAnswer = (answer: Answer) => {
    emit('answer-clicked', answer.answer_id);
  };
  </script>