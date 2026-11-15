<template>
  <section class="welcome-panel">
    <h1><span>support</span> {{ t('dashboard.welcome') }}<br />{{ t('dashboard.nextStep') }}</h1>
    <form class="assistant-input" @submit.prevent="submitQuestion">
      <input v-model="question" :aria-label="t('dashboard.askSidekick')" :placeholder="t('dashboard.askPlaceholder')" />
      <div class="assistant-input__actions"><span class="sidekick-avatar">◉</span><button class="history-button" type="button"><AppIcon name="history" :size="18" />{{ t('dashboard.recentHistory') }}</button><span class="action-divider" /><button type="button" :aria-label="t('dashboard.addContent')"><AppIcon name="plus" :size="20" /></button><button type="submit" :aria-label="t('dashboard.voiceInput')"><AppIcon name="mic" :size="20" /></button></div>
    </form>
  </section>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import AppIcon from '../ui/AppIcon.vue'
import { t } from '../../stores/locale'
const question = ref('')
const submitQuestion = () => { question.value = '' }
</script>

<style scoped>
.welcome-panel { display: grid; justify-items: center; width: min(778px, 100%); margin: 0 auto 88px; } h1 { margin: 0 0 30px; color: #151515; font-size: clamp(29px, 2.25vw, 40px); font-weight: 500; line-height: 1.12; text-align: center; letter-spacing: -1.6px; } h1 span { text-decoration: underline dotted 2px #ddaf42; text-underline-offset: 7px; }.assistant-input { display: flex; flex-direction: column; width: 100%; min-height: 132px; padding: 20px; background: white; border: 1px solid #e2e2e2; border-radius: 27px; box-shadow: 0 2px 4px rgb(0 0 0 / 4%); } input { width: 100%; color: #242424; font-size: 16px; outline: 0; background: transparent; border: 0; } input::placeholder { color: #777; }.assistant-input__actions { display: flex; align-items: center; gap: 14px; margin-top: auto; }.sidekick-avatar { display: grid; width: 24px; height: 24px; color: white; font-size: 15px; background: #4f178e; border-radius: 9px; place-items: center; }button { display: inline-flex; align-items: center; gap: 7px; padding: 3px; color: #151515; font-size: 15px; background: transparent; border: 0; }.history-button { margin-left: auto; }.action-divider { width: 1px; height: 20px; background: #dedede; }
@media (max-width: 640px) { .welcome-panel { margin-bottom: 50px; }.assistant-input { min-height: 116px; padding: 16px; border-radius: 22px; }.history-button { font-size: 0; }.history-button svg { width: 20px; height: 20px; } }
</style>
