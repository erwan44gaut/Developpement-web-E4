<template>
    <div :style="{ width: containerWidth, height: containerHeight }" class="classement-container nes-container is-dark with-title">
      <p class="title">Classement:</p>
      <VueScrollPanel>
        <VueDataTable :value="props.scores" scrollable>
          <VueColumn header="Rang">
            <template #body="slotProps">
              {{ slotProps.index + 1 }}
            </template>
          </VueColumn>
          <VueColumn>
            <template #body="slotProps">
                <AvatarDisplay 
                    :src="getAvatarPath(slotProps.data.avatarName)" 
                    :name="slotProps.data.avatarName" 
                    :width="50" 
                    :height="50" 
                />
            </template>
          </VueColumn>
          <VueColumn field="playerName" header="Joueur"></VueColumn>
          <VueColumn field="score" header="Score"></VueColumn>
        </VueDataTable>
      </VueScrollPanel>
    </div>
  </template>
  
<script setup lang="ts">
import { onMounted } from 'vue';
import { defineProps, type PropType } from 'vue';
import { type Score } from '@/types';
import AvatarDisplay from '../Play/AvatarDisplay.vue';
  
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
		default: '100vh'
	}
});
  
// Fonction pour obtenir le chemin de l'avatar
const getAvatarPath = (avatarName: string | null) => {
	return avatarName ? `../../../public/avatars/${avatarName}.png` : '../../../public/avatars/avatar_0.png';
};
  
// Faire défiler jusqu'au dernier score après le montage du composant
onMounted(() => {
	const lastScoreElement = document.querySelector('.p-datatable-tbody tr:last-child') as HTMLElement;
	if (lastScoreElement) {
		lastScoreElement.scrollIntoView({ behavior: 'smooth' });
	}
});
</script>
  
  <style scoped>
  .p-datatable {
    width: 100%;
    height: 70vh;
  }
  .avatar-image {
    width: 32px;
    height: 32px;
    object-fit: cover;
  }
  </style>
  