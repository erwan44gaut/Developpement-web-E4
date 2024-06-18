<template>
  <div class="overlay">
	<div class="overlay-content">
		<div style="font-weight: normal; width: 100%;">Félicitations, {{ playerName }}!</div>
        <div style="font-weight: normal; width: 100%; font-size: 1.2rem;">Votre score : {{ score }}</div>
		<div style="font-weight: normal; width: 100%; font-size: 1.2rem;">Votre avez atteint le grade : {{ gradeString }}</div>
		<br>
		<GradeDisplay
                    :grade="gradeString"
                    :height="200" 
        />
		<br>
		
		<div style="display: flex; align-items: center; justify-content: center;">
			<button type="button" class="nes-btn is-success" @click="Replay" style="margin-right: 0.5rem;">
				<svg class="nav-icon" width="40" height="40" fill="none" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
					<path d="M2 5h20v14H2V5zm18 12V7H4v10h16zM8 9h2v2h2v2h-2v2H8v-2H6v-2h2V9zm6 0h2v2h-2V9zm4 4h-2v2h2v-2z" fill="white"/>
				</svg> Accueil
			</button>
			<button class="nes-btn is-primary" label="Classements" @click="Leaderboard">
				<svg class="nav-icon" width="40" height="40" fill="none" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
					<path d="M5 3H3v18h18V3H5zm14 2v14H5V5h14zM9 11H7v6h2v-6zm2-4h2v10h-2V7zm6 6h-2v4h2v-4z" fill="white"/>
				</svg> <span style="padding-left: 0.5rem;">Classements</span>
			</button>
		</div>
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

.nes-btn
{
	display: flex;
	text-align: center;
	align-content: center;
	justify-content: center;
	align-items: center;
	font-size: 1.25rem;
}

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
  width: 100vw;

  transform: translate(-50%, -50%);
  font-size: 2rem;
  color: white;
}
</style>
