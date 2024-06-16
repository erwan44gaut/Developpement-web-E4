<template>
  <div :class="['nes-container is-dark with-title', 'content', { 'fade': fadeOut }]">
    <p class="title">Préparation</p>
    <div style="display: flex; width: 100%; align-items: center;">
      <input type="text" v-model="playerName" class="nes-input" placeholder="Entrez votre nom" :disabled="isDisabled" @keyup.enter="selectUser"/>
      <button type="button" :class="['nes-btn is-primary', {'is-disabled': isDisabled || playerName === ''}]" @click="selectUser" :disabled="isDisabled || playerName === ''">Go!</button>
    </div>
    <div style="display: flex; width: 100%;">
      <img style="height: 10rem; image-rendering: pixelated;" :src="botImage"/>
      <p style="margin-top: 2rem;">> {{ readyText }}</p>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, defineEmits, onMounted } from 'vue';

const playerName = ref<string>('');
const emit = defineEmits(['user-selected']);
const readyText = ref<string>('');
const isDisabled = ref<boolean>(false);
const fadeOut = ref<boolean>(false);
const botImage = ref<string>('');


onMounted(() => {
  setTimeout(() => {
    const randomNumber = Math.floor(Math.random() * 12);
    botImage.value = `/public/avatars/avatar_${randomNumber}.png`;
  }, 0);
  typeText(`¤¤¤¤¤¤¤¤¤¤Ecrivez votre nom pour débuter.`, () => { });
});

const selectUser = () => {
  if (playerName.value.trim() === '')
  {
    return;
  }
  isDisabled.value = true; // Disable input and button
  typeText(`OK ${playerName.value},¤¤¤ voyons voir de quoi vous êtes capables.¤¤¤¤¤¤¤¤¤¤`, () => {
    fadeOut.value = true; // Trigger fade out
    setTimeout(() => {
      emit('user-selected', playerName.value);
      console.log('User selected:', playerName.value);
    }, 1000); // Wait for the fade out to complete
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
.content {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin: auto;
  margin-top: 2em;
  width: 80%;
  transition: opacity 0.5s ease-in;
}

.fade {
  opacity: 0;
}
</style>
