
<template>
  <article class="onboarding-card">
    <div class="card-art" :class="'card-art--' + task.art">
      <div v-if="task.art === 'payment'" class="payment-card">
        <span />
        <i />
        <i />
      </div>
      <div v-else class="domain-label">helpspark.us</div>
    </div>

    <div class="card-copy">
      <h2>{{ task.title }}</h2>
      <p>{{ task.description }}</p>
      <button type="button">{{ task.action }}</button>
    </div>
  </article>
</template>

<script setup lang="ts">
type Task = {
  title: string
  description: string
  action: string
  art: 'payment' | 'domain'
}

defineProps<{
  task: Task
}>()
</script>

<style scoped>
.onboarding-card {
  display: flex;
  flex-direction: column;
  min-height: 432px;
  overflow: hidden;
  background: #fff;
  border: 1px solid #ddd;
  border-radius: 23px;
  box-shadow: 0 7px 16px rgb(0 0 0 / 4%);
}

.card-art {
  display: grid;
  height: 174px;
  overflow: hidden;
  place-items: center;
  background: linear-gradient(135deg, #fbfbfb, #f1f1f1);
}

.payment-card {
  display: grid;
  grid-template-columns: 1fr 1fr;
  width: 108px;
  height: 65px;
  padding: 12px 10px;
  background: white;
  border: 1px solid #e0e0e0;
  border-radius: 16px;
  box-shadow: 0 2px 4px rgb(0 0 0 / 4%);
}

.payment-card span {
  grid-column: 1 / -1;
  height: 12px;
  margin: -1px -10px 10px;
  background: #999;
}

.payment-card i {
  width: 26px;
  height: 6px;
  background: #d5d5d5;
}

.payment-card i:last-child {
  justify-self: end;
  width: 13px;
}

.card-art--domain {
  position: relative;
  background:
    linear-gradient(90deg, #ededed 0 2px, transparent 2px 100%),
    linear-gradient(#fcfcfc, #f2f2f2);
  background-size: 120px 100%, 100% 100%;
}

.card-art--domain::after {
  position: absolute;
  right: 46px;
  bottom: 20px;
  width: 30px;
  height: 58px;
  content: '';
  border-left: 2px solid #2d2d2d;
  transform: rotate(-30deg);
}

.domain-label {
  position: relative;
  z-index: 1;
  padding: 15px 66px;
  color: #6236d9;
  font-size: 18px;
  background: white;
  border: 1px solid #ddd;
  border-radius: 30px;
  box-shadow: 0 3px 8px rgb(0 0 0 / 10%);
}

.card-copy {
  display: flex;
  flex: 1;
  flex-direction: column;
  padding: 15px 24px 23px;
}

h2 {
  margin: 0 0 9px;
  color: #141414;
  font-size: 20px;
  font-weight: 500;
  line-height: 1.25;
  letter-spacing: -.4px;
}

p {
  margin: 0;
  color: #6c6c6c;
  font-size: 16px;
  line-height: 1.43;
}

button {
  align-self: flex-start;
  padding: 9px 15px;
  margin-top: auto;
  color: #1d1d1d;
  background: white;
  border: 1px solid #dedede;
  border-radius: 22px;
  box-shadow: 0 2px 4px rgb(0 0 0 / 4%);
}

button:hover {
  background: #f6f6f6;
}
</style>