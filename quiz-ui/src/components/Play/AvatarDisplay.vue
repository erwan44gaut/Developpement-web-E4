<template>
	<div class="avatar-display">
		<img :src="props.src" :alt="props.name" :width="props.width" :height="props.height" preview class="pixelated"/>
	</div>
  </template>
  
<script setup lang="ts">
import { defineProps } from 'vue';
  
const props = defineProps({
	src: {
		type: String,
		required: true
	},
	name: {
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

</script>
  
  <style scoped>
  .avatar-display {
	text-align: center;
  }
  
  .pixelated {
	image-rendering: pixelated;
	image-rendering: -moz-crisp-edges;
	image-rendering: crisp-edges;
	image-rendering: -o-crisp-edges;
  }
  </style>
  