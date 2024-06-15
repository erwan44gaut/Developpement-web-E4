<template>
    <div class="chart-container">
      <Chart type="bar" :data="chartData" :options="chartOptions"></Chart>
    </div>
</template>
  
<script setup lang="ts">
import { ref } from 'vue';
import Chart from 'primevue/chart';
  
// Données pour le graphique
const chartData = ref({
	labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
	datasets: [
		{
			label: 'My First dataset',
			backgroundColor: '#42A5F5',
			borderColor: '#1E88E5',
			data: [65, 59, 80, 81, 56, 55, 40]
		},
		{
			label: 'My Second dataset',
			backgroundColor: '#9CCC65',
			borderColor: '#7CB342',
			data: [28, 48, 40, 19, 86, 27, 90]
		}
	]
});
  
// Options pour le graphique
const chartOptions = ref({
	responsive: true,
	plugins: {
		legend: {
			position: 'top',
		},
		title: {
			display: true,
			text: 'Chart.js Bar Chart'
		}
	}
});
</script>
  
  <style scoped>
  .chart-container {
    width: 100%;
    height: 400px;
  }
  </style>