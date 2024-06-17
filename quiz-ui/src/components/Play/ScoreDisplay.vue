<template>
  <div class="overlay">
	<div class="overlay-content">
		<div style="font-weight: normal;">Félicitations, {{ playerName }}!</div>
        <div style="font-weight: normal; font-size: 1.2rem;">Votre score : {{ score }}</div>
		<div style="font-weight: normal; font-size: 1.2rem;">Votre avez atteint le grade : {{ gradeString }}</div>
		<GradeDisplay
                    :grade="gradeString"
                    :height="200" 
        />
		<VueButton label="Rejouer" @click="Replay" style="margin-right: 0.5rem;"></VueButton>
		<VueButton label="Classements" @click="Leaderboard"></VueButton>
	</div>
  </div>
</template>

<script setup lang="ts">
import { ref, defineProps, onMounted, computed } from 'vue';
import { SaveScoreWithGrade } from '../../services/QuizApiService';
import { Grade, type Participation } from '@/types';
import { useRouter } from 'vue-router';
import GradeDisplay from './GradeDisplay.vue';

const router = useRouter();

const props = defineProps<{ avatarName: string; playerName: string; answerPositions: number[] }>();

const score = ref<number | null>(null);
const grade = ref<Grade | null>(null);

const gradeString = computed(() => {
	return grade.value ? grade.value.toString() : '';
});

onMounted(async () => {
	const participation: Participation = {
		answers: props.answerPositions,
		playerName: props.playerName,
		avatarName: props.avatarName
	};
	try {
		const result = await SaveScoreWithGrade(participation);
		if (result){
			score.value = result.score;
			grade.value = result.grade;
		}
	} catch (error) {
		console.error('Failed to save score', error);
	}

	// Trigger the animation
	const overlayElement = document.querySelector('.overlay');
	if (overlayElement) {
		overlayElement.classList.add('slide-up');
	}
});

const Replay = () =>
{
	// Force refresh
	window.location.href = '/play';
};

const Leaderboard = () =>
{
	router.push('/leadboard');
};

</script>

<style scoped>
.overlay {
  position: fixed;
  top: 100%;
  left: 0;
  width: 100vw;
  height: 100vh;
  background-color: rgba(0, 0, 0, 1);
  z-index: 1000; /* Ensure it covers the whole page */
  transition: transform 1s ease-in-out;
  opacity: 1;
}

.slide-up {
  transform: translateY(-100%);
}

.overlay-content {
  justify-content: center;
  text-align: center;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-size: 2rem;
  color: white;
}
</style>
