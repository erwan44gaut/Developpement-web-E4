<template>
	<div class="avatar-display">
		<VueImage :src="props.src" :alt="props.name" width="150" height="150" preview class="pixelated"/>
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
  