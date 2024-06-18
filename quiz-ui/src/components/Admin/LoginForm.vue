<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { authenticate } from '@/services/QuizApiService';

const visible = ref(true);
const password = ref('');
const router = useRouter();
let flag: boolean = false;

const validatePassword = async () => {
	try {
		const result = await authenticate(password.value);
		if (result) {
			sessionStorage.setItem('authToken', result);
			visible.value = false;
			flag = true;
			router.push({ name: 'admin' });
		}
	} catch (error) {
		alert('Incorrect password');
		router.push({ name: 'home' });
	}
};

</script>

<template>
  <VueDialog class="dialog" v-model:visible="visible" header="Admin Connection" :closable="false">
    <div class="nes-container is-dark">
      <div class="message">
        <span>Enter your password.</span>
      </div>
      <div class="bottom">
        <input type="password" id="input" v-model="password" class="nes-input" toggleMask :feedback="false" placeholder="......"/>
        <button id="button" type="button" label="" @click="validatePassword" class="nes-btn is-success">Connection</button>
      </div>
    </div>
  </VueDialog>
</template>

<style scoped>
.bottom {
  display: flex;
  gap: 10px;
  width: 100%;
}

.message {
  margin-bottom: 10px;
}

#input {
  flex: 1;
}

.dialog *
{
  border-radius: 0px !important;
}
</style>
