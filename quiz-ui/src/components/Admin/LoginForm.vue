<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const visible = ref(true);
const password = ref('');
const correctPassword = 'test';
const router = useRouter();
let flag: boolean = false;

const validatePassword = () => {
	if (password.value == correctPassword) {
		visible.value = false;
		flag = true;
		router.push({
			name: 'admin'
		});
	} else {
		alert('Incorrect password');
		router.push({
			name: 'home'
		});
	}
};

</script>

<template>
  <VueDialog v-model:visible="visible" header="Admin Connection" :closable="false">
    <div class="message">
      <span>Enter your password.</span>
    </div>
    <div class="bottom">
      <VuePassword id="input" v-model="password" toggleMask :feedback="false" placeholder="******" />
      <VueButton id="button" type="button" label="Connection" @click="validatePassword"></VueButton>
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
</style>
