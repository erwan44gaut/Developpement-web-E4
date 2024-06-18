<template>
    <div>
        <div class="question-display nes-container is-dark with-title">
            <p v-if="question" class="title">{{  question.title }}</p>
            <div class="question-content" v-if="question">
                <div>
                    <div>
                        {{ question.text }}
                    </div>
                    <br>
                    <VueImage v-if="question.image" :src="question.image" :alt="question.text" height="250" preview />
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
        <div class="secret-spacing"></div>
        <div class="secret-container">
            <img class="secret" src="/secret.gif" @click="triggerSecret">
            <p v-if="foundSecret">Merci !</p>
        </div>
        <Dialog :visible="secretDialogOpen" modal :style="{ width: '25rem' }" class="nes-container is-dark" headerless>
            <template #container="{ closeCallback }">
                <div class="dialog-content">
                    <p class="nes-text is-success">Vous avez trouvé un point bonus !</p>
                    <p style="font-size: 0.75rem;">Ajoutez le à notre note :)</p>
                    <button class="secret-btn nes-btn is-success" @click="closeSecret">Ajouter à la note</button>
                    <button class="secret-btn nes-btn is-error" @click="confirmCloseSecret">Le laisser</button>
                </div>
            </template>
        </Dialog>

        <Dialog :visible="decliningSecret" modal :style="{ width: '25rem' }" class="nes-container is-dark" headerless>
            <template #container="{ closeCallback }">
                <div class="dialog-content">
                    <p>Êtes-vous sûr ?</p>
                    <button class="secret-btn nes-btn is-success" @click="closeSecret">Ajouter à la note</button>
                    <button class="secret-btn nes-btn is-success" @click="closeSecret">Ajouter à la note</button>
                </div>
            </template>
        </Dialog>
    </div>
</template>

<script setup lang="ts">
import { ref, defineProps, defineEmits } from 'vue';
import { type Question, type Answer } from '@/types';
import Dialog from 'primevue/dialog';

const props = defineProps<{ question: Question | null, questionNumber: number | null, questionsAmount: number | null }>();
const emit = defineEmits(['answer-clicked']);
const selectedAnswerIndex = ref<number | null>(null);
const selectedAnswer = ref<Answer | null>(null);
const canSubmit = ref<boolean>(false);

const secretDialogOpen = ref<boolean>(false);
const decliningSecret = ref<boolean>(false);
const foundSecret = ref<boolean>(false);

const triggerSecret = () =>
{
    secretDialogOpen.value = true;
}

const closeSecret = () =>
{
    secretDialogOpen.value = false;
    decliningSecret.value = false;
    foundSecret.value = true;
}

const confirmCloseSecret = () =>
{
    secretDialogOpen.value = false;
    decliningSecret.value = true;
}

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

.secret-spacing
{
    height: 100vh;
}

.secret-container
{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    margin: 5rem;
    color: white;
}

.secret
{
    position: relative;
    width: 100px;
    height: 100px;
    margin: 1rem;
    transition-duration: 0s;
}

.secret:hover
{
    transform: scale(1.2);
    animation: spin 1s linear infinite;
}

.secret-btn
{
    width: 100%;
}

#secret-dialog
{
    display: block;
}

</style>