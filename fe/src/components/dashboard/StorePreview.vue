
<template>
  <section class="store-preview" aria-label="Store preview">
    <div class="preview-window">
      <div class="preview-bar">
        <span>your brand</span>
        <span>Products　About</span>
        <span>⌕　♙</span>
      </div>

      <div class="preview-hero">
        <div class="preview-copy">
          <strong>Generated data</strong>
          <small>Your store preview is ready to explore.</small>
          <button type="button">Explore</button>
        </div>
        <div class="skier">●</div>
      </div>

      <div class="preview-footer">Featured products</div>
      <span class="private-chip">♙　Private</span>
    </div>

    <button class="publish-button" type="button">
      <AppIcon name="rocket" :size="18" />
      Publish store
    </button>
  </section>
</template>

<script setup lang="ts">
import AppIcon from '../ui/AppIcon.vue'
</script>

<style scoped>
.store-preview {
  display: grid;
  width: min(402px, 100%);
  gap: 13px;
  margin: 5px auto 44px;
}

.preview-window {
  position: relative;
  overflow: hidden;
  height: 230px;
  background: #fff;
  border: 1px solid #dfdfdf;
  border-radius: 22px;
  box-shadow: 0 3px 8px rgb(0 0 0 / 9%);
}

.preview-bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 23px;
  padding: 0 11px;
  color: white;
  font-size: 5px;
  background: #080808;
}

.preview-hero {
  position: relative;
  height: 170px;
  padding: 56px 26px;
  overflow: hidden;
  background: linear-gradient(165deg, #c6d1dc 0%, #c6d1dc 32%, #91b5ce 33%, #e5eef1 100%);
}

.preview-hero::after {
  position: absolute;
  top: 18px;
  right: 56px;
  width: 28px;
  height: 62px;
  content: '';
  background: linear-gradient(145deg, transparent 45%, #122432 46% 52%, transparent 53%);
  transform: rotate(-28deg);
}

.preview-copy {
  position: relative;
  z-index: 1;
  display: grid;
  width: 210px;
  gap: 8px;
  padding: 14px;
  background: rgb(255 255 255 / 89%);
}

.preview-copy strong {
  font-size: 15px;
}

.preview-copy small {
  color: #555;
  font-size: 6px;
}

.preview-copy button {
  width: 54px;
  padding: 5px;
  color: white;
  font-size: 6px;
  background: #151515;
  border: 0;
}

.skier {
  position: absolute;
  top: 54px;
  right: 82px;
  z-index: 1;
  color: #0b2431;
  font-size: 22px;
}

.preview-footer {
  padding: 16px 25px;
  color: #333;
  font-size: 13px;
  font-weight: 700;
}

.private-chip {
  position: absolute;
  bottom: 12px;
  left: 12px;
  padding: 9px 14px;
  color: white;
  font-size: 14px;
  background: #5e5e5e;
  border-radius: 15px;
}

.publish-button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 36px;
  gap: 8px;
  color: white;
  font-weight: 600;
  background: linear-gradient(#202020, #111);
  border: 1px solid #333;
  border-radius: 19px;
  box-shadow: 0 2px 5px rgb(0 0 0 / 26%);
}

.publish-button:hover {
  background: #2e2e2e;
}
</style>
