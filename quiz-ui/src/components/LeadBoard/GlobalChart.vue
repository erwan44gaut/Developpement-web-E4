<template>
<div :style="{ width: props.containerWidth, height: props.containerHeight }" class="chart-container">
	<VueChart type="bar" :data="chartData" :options="chartOptions"></VueChart>
</div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { getCorrectIncorrectCounts } from '@/services/QuizApiService';

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
			label: 'Incorrect',
			backgroundColor: '#EF5350',
			borderColor: '#D32F2F',
			data: [] as number[]
		},
		{
			label: 'Correct',
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
			position: 'top',
		},
		title: {
			display: true,
			text: 'Correct vs Incorrect Answers per Question'
		}
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
	const counts = await getCorrectIncorrectCounts();
	console.log(counts);

	chartData.value.labels = counts.map((item, index) => `Question ${index + 1}`);
	chartData.value.datasets[0].data = counts.map(item => item.is_not_correct);
	chartData.value.datasets[1].data = counts.map(item => item.is_correct);
};

// Charger les données du graphique lors du montage du composant
onMounted(loadChartData);
</script>

<style scoped>
.chart-container {
border: 1px solid #ccc;
padding: 16px;
box-sizing: border-box;
}
</style>
