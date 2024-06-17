<template>
    <div class="question-display nes-container is-dark with-title">
        <p v-if="question" class="title">{{  question.title }}</p>
        <div class="question-content" v-if="question">
            <div>
                <div>
                    {{ question.text }}
                </div>
                <br>
                <VueImage v-if="question.image" :src="question.image" :alt="question.text" width="250" height="250" preview />
                <br>
                <br>
                <div>
                    <div v-for="(answer, index) in question.possibleAnswers" :key="answer.answer_id" class="answers" @click="selectAnswer(index)">
                        <p :class="{'answer nes-text is-primary': selectedAnswerIndex == index}" @click="() => selectAnswer(index)">> {{ answer.text }}</p>
                    </div>
                </div>
            </div>
            <div>
                <div class="flex gap-4 mt-1">
                    <button type="button" :class="['nes-btn is-success', {'is-disabled' : !canSubmit }]" @click="Submit" :disabled="!canSubmit">Submit</button>
                </div>
            </div>
        </div>
        <div v-else class="question-content">
            Loading...
        </div>
    </div>
</template>

<script setup lang="ts">
import { ref, defineProps, defineEmits } from 'vue';
import { type Question, type Answer } from '@/types';

const props = defineProps<{ question: Question | null, questionNumber: number | null, questionsAmount: number | null }>();
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

.nes-container
{
    font-size: 0.8rem;
    width: 60rem;
    transition-duration: opacity 1s;
    margin-top: 6rem;
    margin-bottom: 2rem;
}

.question-content
{
}

</style>