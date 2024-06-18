<template>
        <VueChart class="chart" type="bar" :data="chartData" :options="chartOptions"></VueChart>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { getAllScores } from '@/services/QuizApiService';
import { Chart as ChartJS } from 'chart.js';
ChartJS.defaults.font.family = 'RetroFont';

// Interface pour les scores
interface Score {
    score: number;
}

// Props pour la taille du conteneur
const props = defineProps({
	containerWidth: {
		type: String,
		default: '80vw'
	},
	containerHeight: {
		type: String,
		default: '100vh'
	}
});

// Données et options pour le graphique
const chartData = ref({
	labels: [] as string[],
	datasets: [
		{
			label: 'Number of People',
			backgroundColor: '#9CCC65',
			borderColor: '#7CB342',
			data: [] as number[]
		}
	]
});

const chartOptions = ref({
	responsive: true,
	plugins: {
		legend: {
			display: false,
		},
		title: {
			display: true,
			text: 'Number of People by Score'
		}
	},
	animation: {
		duration: 200 // Disable all animations
	},
	scales: {
		x: {
			stacked: true
		},
		y: {
			stacked: true
		}
	}
});

// Fonction pour charger les données du graphique
const loadChartData = async () => {
	const scores: Score[] = await getAllScores();

	// Compter le nombre de personnes pour chaque score
	const scoreCounts = scores.reduce((acc, { score }) => {
		acc[score] = (acc[score] || 0) + 1;
		return acc;
	}, {} as Record<number, number>);

	// Mettre à jour les données du graphique
	chartData.value.labels = Object.keys(scoreCounts).map(score => `Score ${score}`);
	chartData.value.datasets[0].data = Object.values(scoreCounts);
};

// Charger les données du graphique lors du montage du composant
onMounted(loadChartData);
</script>

<style scoped>

</style>
