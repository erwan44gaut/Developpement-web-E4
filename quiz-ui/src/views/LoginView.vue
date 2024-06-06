<script setup lang="ts">
import LoginForm from '@/components/Admin/LoginForm.vue';
import { ref } from 'vue';

const showPopup = ref(true);
</script>

<template>
  <div>
    <LoginForm v-if="showPopup" @close="showPopup = false" />
  </div>
</template>
