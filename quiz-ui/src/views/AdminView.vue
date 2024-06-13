<script setup lang="ts">
import EditorManager from '@/components/Admin/EditorManager.vue';
</script>

<template>
  <div class="grid-container">
    <EditorManager />
</div>
</template>

<style scoped>
.grid-container {
  display: grid;
  grid-template-columns: repeat(3, 1fr); /* Ajuste pour que chaque colonne prenne une part égale de l'espace */
  gap: 10px; /* Optionnel : Espace entre les éléments */
}
</style>
