<template>
    <div :style="{ width: containerWidth, height: containerHeight }" class="classement-container">
        <h1>Classement</h1>
        <VueScrollPanel :style="{ width: '100%', height: '100%' }">
            <VueDataTable :value="sortedScores" scrollable>
                <VueColumn header="Rang">
                    <template #body="slotProps">
                        {{ slotProps.index + 1 }}
                    </template>
                </VueColumn>
                <VueColumn field="playerName" header="Joueur"></VueColumn>
                <VueColumn field="score" header="Score"></VueColumn>
            </VueDataTable>
        </VueScrollPanel>
    </div>
</template>
  
<script setup lang="ts">
import { computed, onMounted } from 'vue';
import { defineProps, type PropType } from 'vue';
import { type Score } from '@/types';

// Définir les props avec le type PropType
const props = defineProps({
	scores: {
		type: Array as PropType<Score[]>,
		required: true
	},
	containerWidth: {
		type: String,
		default: '100%'
	},
	containerHeight: {
		type: String,
		default: '400px'
	}
});

// Trier les scores en ordre décroissant
const sortedScores = computed(() => {
	return [...props.scores].sort((a, b) => b.score - a.score);
});

// Faire défiler jusqu'au dernier score après le montage du composant
onMounted(() => {
	const lastScoreElement = document.querySelector('.p-datatable-tbody tr:last-child') as HTMLElement;
	if (lastScoreElement) {
		lastScoreElement.scrollIntoView({ behavior: 'smooth' });
	}
});
</script>
  
<style scoped>
.classement-container {
    border: 1px solid #ccc;
    padding: 16px;
    box-sizing: border-box;
}
.p-datatable {
    width: 100%;
}
</style>