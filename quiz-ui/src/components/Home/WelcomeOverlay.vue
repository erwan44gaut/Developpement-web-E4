<template>
  <div>
    <div v-if="showOverlay" :class="['overlay', { 'slide-up': slideUp }]">
      <div :class="['overlay-content', { 'mounted': mounted }]">
        <div style="font-weight: normal;">Bienvenue sur le quiz retrogaming ultime !</div>
        <div style="font-weight: normal; font-size: 0.8rem;">Erwan GAUTIER, Thomas LE MAGNY, Alex FOULON</div>
        <br>
        <button type="button" class="nes-btn is-primary" @click="triggerSlideUp">
          <svg class="nav-icon" width="30" height="30" fill="none" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
            <path d="M10 20H8V4h2v2h2v3h2v2h2v2h-2v2h-2v3h-2v2z" fill="currentColor"/> 
          </svg> Jouer
        </Button>
        <br>
        <br>
      </div>
    </div>
  </div>
</template>

<script setup>
import Button from 'primevue/button';
import { ref, onMounted, defineEmits } from 'vue';

const mounted = ref(false);
const showOverlay = ref(true);
const slideUp = ref(false);
const emit = defineEmits(['overlay-gone']);

onMounted(() => {
  setTimeout(() => {
    mounted.value = true;
  }, 0);
});


const triggerSlideUp = () => {
  slideUp.value = true;
  
  emit('overlay-gone', 0);
  setTimeout(() => {
    showOverlay.value = false;
  }, 1000); // Duration of the slide-up animation
};
</script>

<style scoped>
.overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 1); /* Semi-transparent background */
  z-index: 1000; /* Ensure it covers the whole page */
  transition: transform 1s ease-in-out;
}

.slide-up {
  transform: translateY(-100%);
}

.overlay-content {
  justify-content: center;
  text-align: center;
  position: absolute;
  top: 50%;
  width: 100%;
  transform: translate(0, -50%);
  font-size: 1rem;
  color: white;
  opacity: 0;
  transition: opacity 1s;
}

.overlay-content.mounted
{
  opacity: 1;
}

</style>
