<template>
    <div class="content">
      <h1>Avant de commencer, entrez votre nom.</h1>
      <div>
        <VueInputText v-model="playerName" placeholder="Entrez votre nom" :disabled="isDisabled"/>
        <VueButton label="Go !" @click="selectUser" :disabled="isDisabled"/>
      </div>
      <h3>
        {{ readyText }}
      </h3>
    </div>
  </template>
  
<script setup lang="ts">
import { ref, defineEmits } from 'vue';
  
const playerName = ref<string>('');
const emit = defineEmits(['user-selected']);
const readyText = ref<string>('');
const isDisabled = ref<boolean>(false);

const selectUser = () => {
  if (playerName.value.trim() === '') {
    alert('Veuillez entrer un nom');
    return;
  }
  isDisabled.value = true; // Disable input and button
  typeText(`OK ${playerName.value}¤¤¤, voyons voir de quoi vous êtes capables.¤¤¤¤¤¤¤¤¤¤`, () => {
    emit('user-selected', playerName.value);
  });
};

const typeText = (text: string, callback: () => void) => {
  readyText.value = '';
  let index = 0;

  const type = () => {
    if (index < text.length) {
      if (text[index] === '¤') // Used for temporisation
      {
        index++;
        setTimeout(type, 100);
      }
      else if (text[index] === ' ')
      {
        readyText.value += text[index];
        index++;
        setTimeout(type, 0);
      }
      else
      {
        readyText.value += text[index];
        index++;
        setTimeout(type, 50);
      }
    } else {
      callback();
    }
  };

  type();
};

</script>

<style scoped>
.content
{
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1em;
  margin-top: 5em;
}

</style>