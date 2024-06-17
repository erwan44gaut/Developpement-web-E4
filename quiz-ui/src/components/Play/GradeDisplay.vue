<template>
	<div class="grade-display">
		<img :src="getGradePath(props.grade)" :alt="props.grade" :width="props.width" :height="props.height" preview class="pixelated"/>
	</div>
  </template>
  
<script setup lang="ts">
import { defineProps } from 'vue';
  
const props = defineProps({
	grade: {
		type: String,
		required: true
	},
	width: {
		type: [String, Number],
		default: 150
	},
	height: {
		type: [String, Number],
		default: 150
	}
});

// Fonction pour obtenir le chemin de l'avatar
const getGradePath = (grade: string | null) => {
	return grade ? `../../../public/grades/${grade}.gif` : '';
};

</script>
  
  <style scoped>
  .grade-display {
	text-align: center;
  }
  
  .pixelated {
	image-rendering: pixelated;
	image-rendering: -moz-crisp-edges;
	image-rendering: crisp-edges;
	image-rendering: -o-crisp-edges;
  }
  </style>
  