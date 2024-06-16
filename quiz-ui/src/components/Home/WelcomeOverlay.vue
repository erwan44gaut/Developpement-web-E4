<template>
  <div>
    <div v-if="showOverlay" class="overlay" :class="{ 'slide-up': slideUp }">
      <div class="overlay-content">
        <div style="font-weight: normal;">Welcome to the ultimate retrogaming quiz</div>
        <div style="font-weight: normal; font-size: 1.2rem;">by Erwan GAUTIER, Thomas LE MAGNY, Alex FOULON</div>
        <Button label="Start" @click="triggerSlideUp"></Button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import Button from 'primevue/button';

const showOverlay = ref(true);
const slideUp = ref(false);

const triggerSlideUp = () => {
  slideUp.value = true;
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
  left: 50%;
  transform: translate(-50%, -50%);
  font-size: 2rem;
  color: white;
}
</style>
