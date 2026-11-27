
<template>
  <section class="task-grid" aria-label="Next tasks">
    <OnboardingCard
      v-for="task in starterTasks"
      :key="task.title"
      :task="task"
    />

    <article class="journey-card">
      <div class="journey-card__art">
        <span class="progress-badge">
          <AppIcon name="home" :size="20" />
          8 tasks completed
        </span>
        <div class="map-line">⌁</div>
        <span class="shop-symbol">⌂</span>
        <span class="briefcase-symbol">▣</span>
      </div>

      <div class="journey-card__copy">
        <h2>Set up B2B</h2>
        <p>Continue setting up your B2B store.</p>
        <button type="button">Continue</button>
      </div>
    </article>

    <article class="improvement-card">
      <p class="task-count">
        <AppIcon name="home" :size="20" />
        3 tasks completed
      </p>

      <h2>Improve your store</h2>
      <p class="improvement-card__description">
        Complete these tasks to improve your store.
      </p>

      <ul>
        <li v-for="item in improvements" :key="item">
          <span />
          {{ item }}
        </li>
      </ul>

      <button type="button">Start</button>
    </article>
  </section>
</template>

<script setup lang="ts">
import AppIcon from '../ui/AppIcon.vue'
import OnboardingCard from './OnboardingCard.vue'

type StarterTask = {
  title: string
  description: string
  action: string
  art: 'payment' | 'domain'
}

const starterTasks: StarterTask[] = [
  {
    title: 'Set up payments',
    description: 'Connect your payment provider to start accepting payments.',
    action: 'Get started',
    art: 'payment',
  },
  {
    title: 'Connect your domain',
    description: 'Connect your domain to make your store accessible.',
    action: 'Connect domain',
    art: 'domain',
  },
]

const improvements: string[] = [
  'Customize your store design',
  'Add more product information',
  'Set up your store policies',
]
</script>

<style scoped>
.task-grid { 
  display: grid; 
  grid-template-columns: repeat(3, minmax(0, 1fr)); 
  align-items: start; gap: 20px; width: min(1168px, 100%); margin: 0 auto; 
}
.journey-card, .improvement-card { 
  overflow: hidden; 
  background: white; 
  border: 1px solid #ddd; 
  border-radius: 23px; 
  box-shadow: 0 7px 16px rgb(0 0 0 / 4%); 
}
.journey-card { 
  min-height: 432px; 
}
.journey-card__art { 
  position: relative; 
  height: 174px; 
  overflow: hidden; 
  background: 
    radial-gradient(circle at 15% 66%, #0cbea4 0 28px, transparent 29px), 
    radial-gradient(circle at 80% 28%, #13a891 0 35px, transparent 36px), 
    linear-gradient(130deg, #43e1cb, #c3f1db); 
}
.journey-card__art::before { 
  position: absolute; 
  inset: 40px 70px 10px 100px; 
  content: ''; 
  background: 
    repeating-linear-gradient(48deg, #eee 0 18px, #e2f4ea 19px 30px); 
  clip-path: polygon(0 0, 100% 22%, 70% 100%, 7% 78%); 
}
.progress-badge { 
  position: absolute; 
  z-index: 2; 
  top: 10px; 
  left: 12px; 
  display: inline-flex; 
  align-items: center; 
  gap: 7px; 
  padding: 7px 11px; 
  color: white; 
  font-size: 14px; 
  background: rgb(44 80 75 / 77%); 
  border-radius: 15px; 
}
.map-line {
  position: absolute;
  z-index: 3;
  right: 90px;
  bottom: 38px;
  color: #168c79;
  font-size: 75px;
  transform: rotate(24deg);
}

.shop-symbol,
.briefcase-symbol {
  position: absolute;
  z-index: 3;
  display: grid;
  width: 53px;
  height: 53px;
  color: #041e19;
  font-size: 36px;
  background: #13b398;
  border-radius: 13px;
  place-items: center;
}

.shop-symbol {
  left: 43px;
  bottom: 33px;
}

.briefcase-symbol {
  top: 25px;
  right: 38px;
  background: #06947e;
}

.journey-card__copy {
  display: flex;
  flex-direction: column;
  min-height: 258px;
  padding: 15px 24px 23px;
}

h2 {
  margin: 0 0 9px;
  color: #151515;
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

.improvement-card {
  display: flex;
  flex-direction: column;
  grid-column: 2;
  min-height: 430px;
  padding: 25px 24px 23px;
}

.task-count {
  display: flex;
  align-items: center;
  gap: 9px;
  margin-bottom: 17px;
  color: #737373;
  font-size: 14px;
}

.improvement-card__description {
  margin-bottom: 22px;
}

ul {
  display: grid;
  gap: 14px;
  padding: 0;
  margin: 0;
  list-style: none;
}

li {
  display: flex;
  align-items: center;
  gap: 11px;
  color: #252525;
  font-size: 16px;
}

li span {
  width: 20px;
  height: 20px;
  border: 2px dotted #adadad;
  border-radius: 50%;
}

@media (max-width: 1060px) {
  .task-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }

  .improvement-card {
    grid-column: auto;
  }
}

@media (max-width: 680px) {
  .task-grid {
    grid-template-columns: 1fr;
  }

  .journey-card {
    min-height: 400px;
  }

  .improvement-card {
    min-height: 390px;
  }
}
</style>
