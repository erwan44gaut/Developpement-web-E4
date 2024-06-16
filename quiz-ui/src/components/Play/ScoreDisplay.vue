<template>
  <div class="overlay">
	<div class="overlay-content">
		<div style="font-weight: normal;">Félicitations, {{ playerName }}!</div>
        <div style="font-weight: normal; font-size: 1.2rem;">Votre score : {{ score }}</div>
		<Button label="Rejouer" @click="Replay" style="margin-right: 0.5rem;"></Button>
		<Button label="Classements" @click="Leaderboard"></Button>
	</div>
  </div>
</template>

<script setup lang="ts">
import { ref, defineProps, onMounted } from 'vue';
import { saveScore } from '../../services/QuizApiService';
import { type Participation } from '@/types';
import { useRouter } from 'vue-router';
const router = useRouter();
import Button from 'primevue/button';

const props = defineProps<{ playerName: string; answerPositions: number[] }>();

const score = ref<number | null>(null);

onMounted(async () => {
  const participation: Participation = {
    answers: props.answerPositions,
    playerName: props.playerName
  };

  try {
    score.value = await saveScore(participation);
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
