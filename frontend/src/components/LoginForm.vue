<script setup lang="ts">
</script>

<template>
    <div class="container">
        <div>
            <VueCard>
                <template #title>Advanced Card</template>
                <template #content>
                <p class="m-0">
                    Bienvenue sur le quizz de Thomas, Alex et Erwan !
                </p>
                </template>
                <template #footer>
                    <div class="flex gap-3 mt-1">
                        <VueButton label="Cancel" severity="secondary" />
                        <VueButton label="Save" class="w-full" />
                    </div>
                </template>
            </VueCard>
        </div>
    </div>
</template>

<style scoped>
.container {
    display: flex;
    justify-content: center;
    align-items: center;
}
</style>
