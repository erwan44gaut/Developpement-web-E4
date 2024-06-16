<template>
    <Overlay />
    <div v-if="question">
        <h2>{{ question.text }}</h2>
        <VueImage v-if="question.image" :src="question.image" :alt="question.text" width="250" height="250" preview />
        <div v-for="(answer, index) in question.possibleAnswers" :key="answer.answer_id" class="answers">
        <VueRadioButton v-model="selectedAnswer" :value="answer" @change="() => selectAnswer(index)" />
        <label>{{ answer.text }}</label>
        </div>
    </div>
    <div v-else>
        Loading...
    </div>
</template>

<script setup lang="ts">
import { ref, defineProps, defineEmits } from 'vue';
import { type Question, type Answer } from '@/types';
import Overlay from '@/components/Home/WelcomeOverlay.vue';

defineProps<{ question: Question | null }>();
const emit = defineEmits(['answer-clicked']);
const selectedAnswer = ref<Answer | null>(null);

const selectAnswer = (index: number) => { emit('answer-clicked', index); };
</script>

<style scoped>
.answers {
display: flex;
align-items: center;
margin-bottom: 8px;
}

.radio {
margin-right: 8px;
}

label {
margin-left: 8px;
}
</style>