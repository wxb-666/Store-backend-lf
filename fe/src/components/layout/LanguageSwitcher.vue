<template>
  <Transition name="language-switcher">
    <button v-if="visible" class="language-button" type="button" @click="toggleLocale">
      <span class="language-button__globe" aria-hidden="true">A</span>
      <span>{{ locale === 'zh-CN' ? t('settings.switchToEnglish') : t('settings.switchToChinese') }}</span>
      <span class="language-button__code">{{ locale === 'zh-CN' ? 'EN' : '中' }}</span>
    </button>
  </Transition>
</template>

<script setup lang="ts">
import { locale, t, toggleLocale } from '../../stores/locale'

defineProps<{ visible: boolean }>()
</script>

<style scoped>
.language-button { position: absolute; right: 0; bottom: 48px; display: inline-flex; align-items: center; min-width: 196px; gap: 9px; padding: 10px 11px; color: #f6f6f6; font-size: 13px; text-align: left; background: #292929; border: 1px solid #494949; border-radius: 12px; box-shadow: 0 10px 24px rgb(0 0 0 / 28%); }.language-button:hover { background: #383838; }.language-button__globe { display: grid; width: 22px; height: 22px; color: #1b1b1b; font-size: 12px; font-weight: 700; background: #a5d65c; border-radius: 50%; place-items: center; }.language-button__code { padding: 2px 5px; margin-left: auto; color: #bbb; font-size: 11px; background: #171717; border-radius: 5px; }.language-switcher-enter-active, .language-switcher-leave-active { transition: opacity .16s ease, transform .16s ease; }.language-switcher-enter-from, .language-switcher-leave-to { opacity: 0; transform: translateY(6px) scale(.97); }
</style>
