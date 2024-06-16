<template>
    <div class="question-display nes-container is-dark with-title">
        <p v-if="question" class="title">{{ questionNumberText }}: {{ question.title }}</p>
        <div v-if="question">
            <div>
                <div>
                    {{ question.text }}
                </div>
                <VueImage v-if="question.image" :src="question.image" :alt="question.text" width="250" height="250" preview />
                <div>
                    <div v-for="(answer, index) in question.possibleAnswers" :key="answer.answer_id" class="answers" @click="selectAnswer(index)">
                        <VueRadioButton v-model="selectedAnswer" :value="answer" @change="() => selectAnswer(index)" />
                        <label>{{ answer.text }}</label>
                    </div>
                </div>
            </div>
            <div>
                <div class="flex gap-4 mt-1">
                    <button type="button" class="nes-btn is-success" @click="Submit" :disabled="!canSubmit">Submit</button>
                </div>
            </div>
        </div>
        <div v-else class="content">
            Loading...
        </div>
    </div>
</template>

<script setup lang="ts">
import { ref, defineProps, defineEmits } from 'vue';
import { type Question, type Answer } from '@/types';

const props = defineProps<{ question: Question | null, questionNumberText: string | null }>();
const emit = defineEmits(['answer-clicked']);
const selectedAnswerIndex = ref<number | null>(null);
const selectedAnswer = ref<Answer | null>(null);
const canSubmit = ref<boolean>(false);

const selectAnswer = (index: number) =>
{
	if (props.question && props.question.possibleAnswers)
	{
		selectedAnswerIndex.value = index;
		selectedAnswer.value = props.question.possibleAnswers[index];
		canSubmit.value = true;
	}
};

const Submit = () =>
{
	if (selectedAnswer.value)
	{
		emit('answer-clicked', selectedAnswerIndex.value);
		canSubmit.value = false;
	}
};
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

.content
{
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100%;
  opacity: 1;
}


.card
{
    width: 50rem;
    max-height: 80vh;
    overflow-y: auto;
    transition-duration: 1s;
}
</style>