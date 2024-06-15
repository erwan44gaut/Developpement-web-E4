<template>
  <main>
    <GlobalChart />
  </main>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import GlobalRanking from '../components/Play/GlobalRanking.vue';
import GlobalChart from '../components/Play/GlobalChart.vue'; // Importez le composant de graphique
import { getAllScores } from '@/services/QuizApiService';
import { type Score } from '@/types';

const scores = ref<Score[]>([]);

// Fonction pour récupérer les scores au montage du composant
const fetchScores = async () => {
	try {
		const result = await getAllScores();
		scores.value = result;
	} catch (error) {
		console.error('Error fetching scores:', error);
	}
};

onMounted(() => {
	fetchScores();
});
</script>

<style scoped>
main {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
}
</style>