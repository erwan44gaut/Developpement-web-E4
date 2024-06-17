<template>
    <div class="content">
      <div class="grid">
        <GlobalRanking :scores="scores" v-if="scores.length > 0" containerWidth="45vw" containerHeight="100%" />
        <GlobalChart containerWidth="45vw" containerHeight="100%" />
      </div>
    </div>
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

.content
{ 
  margin-top: 35px;
  padding: 2rem;
}

.grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  box-sizing: border-box;
  width: 100%;

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

</style>
