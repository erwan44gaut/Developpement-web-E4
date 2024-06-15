<template>
  <VueScrollPanel class="scroll-panel">
    <div class="content">
      <GlobalRanking :scores="scores" v-if="scores.length > 0" containerWidth="80vw" containerHeight="600px" />
      <GlobalChart />
    </div>
  </VueScrollPanel>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import GlobalRanking from '../components/LeadBoard/GlobalRanking.vue';
import GlobalChart from '../components/LeadBoard/GlobalChart.vue';
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
.scroll-panel {
  width: 100%;
  height: 100vh;
}
.content {
  padding: 20px;
  box-sizing: border-box;
  display: flex;
  flex-direction: column;
  align-items: center;
}
</style>
