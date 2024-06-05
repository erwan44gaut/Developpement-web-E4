<script setup lang="ts">
import { ref } from 'vue';
import draggable from 'vuedraggable';

const items = ref([
	{ id: 1, name: 'Item 1' },
	{ id: 2, name: 'Item 2' },
	{ id: 3, name: 'Item 3' },
	{ id: 4, name: 'Item 4' }
]);
</script>

<template>
  <div class="draggable-list">
    <draggable v-model="items">
      <template #item="{ element }">
        <div class="draggable-item">
          {{ element.name }}
        </div>
      </template>
    </draggable>
  </div>
</template>

<style scoped>
.draggable-list {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.draggable-item {
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  background-color: #f9f9f9;
  cursor: grab;
}
</style>
