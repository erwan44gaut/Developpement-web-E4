<script setup lang="ts">
import { ref } from 'vue';

const visible = ref(false);
const value = ref('');
</script>

<template>
    <div class="card">
        <VueButton label="Connection" @click="visible = true" />
        <VueDialog v-model:visible="visible" modal header="Admin Connection">
            <div class="message">
                <span>Enter your password.</span>
            </div>
            <div class="bottom">
                <VuePassword id="input" v-model="value" toggleMask :feedback="false" placeholder="******"/>
                <VueButton id="button" type="button" label="Connection" @click="visible = false"></VueButton>
            </div>
        </VueDialog>
    </div>
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
