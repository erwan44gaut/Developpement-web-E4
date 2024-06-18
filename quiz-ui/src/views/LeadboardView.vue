<template>
  <div class="content">
    <div class="grid">
      <GlobalRanking :scores="scores" v-if="scores.length > 0" containerWidth="45vw" containerHeight="80vh" />
      <div :style="{ width: '45vw', height: '80vh' }" class="chart-container nes-container is-dark with-title">
        <p class="title">Réponses:</p>
        <div class="combined-charts">
          <GlobalChart class="chart global-chart"/>
          <ScoreChart class="chart score-chart"/>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import GlobalRanking from '../components/LeadBoard/GlobalRanking.vue';
import GlobalChart from '../components/LeadBoard/GlobalChart.vue';
import ScoreChart from '../components/LeadBoard/ScoreChart.vue'
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
  margin-top: 35px;
  padding: 2rem;
}

.grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  box-sizing: border-box;
  width: 100%;
  gap: 20px; /* Add some gap between the columns */

  opacity: 0; /* Start with opacity 0 */
  animation: fadeIn 0.5s ease 0.2s forwards; /* Animation definition */
}

@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

.chart-container {
  width: 45vw;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
}

.combined-charts {
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  height: 100%;
}

.chart {
  width: 100%;
  height: 45%;
  margin-bottom: 20px;
}

.chart:last-child {
  margin-bottom: 0;
}
</style>
