<template>
	<div class="grade-display">
		<img :src="getGradePath(props.grade)" :height="props.height" preview class="pixelated"/>
	</div>
  </template>
  
<script setup lang="ts">
import { defineProps } from 'vue';
  
const props = defineProps({
	grade: {
		type: String,
		required: true
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

  .responsive-image {
    width: 100%;
    height: 100%;
    object-fit: contain;
  }
  
  .pixelated {
	image-rendering: pixelated;
	image-rendering: -moz-crisp-edges;
	image-rendering: crisp-edges;
	image-rendering: -o-crisp-edges;
  }
  </style>
  