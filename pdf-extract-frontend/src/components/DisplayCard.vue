<template>
  <div class="card" @click="flip">
    <div :class="['card-inner', { 'is-flipped': isFlipped }]">
      <div class="card-face card-front">
        <p>{{ card.front }}</p>
      </div>
      <div class="card-face card-back">
        <p>{{ card.back }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue'

export default {
  name: 'DisplayCard',
  props: {
    card: {
      type: Object,
      required: true,
    },
  },
  setup() {
    const isFlipped = ref(false)
    const flip = () => {
      isFlipped.value = !isFlipped.value
    }
    return { isFlipped, flip }
  },
}
</script>

<style scoped>
/* ÄUSSERE KARTE:
   max 900px breit (oder 90% des Viewports),
   und 500px Höhe. */
.card {
  width: min(75vw, 900px);
  height: 500px;
  margin: 0 auto;
  cursor: pointer;
  perspective: 1000px;
  border: 1px solid #ddd;
  border-radius: 8px;
  overflow: hidden;
}

.card-inner {
  width: 100%;
  height: 100%;
  transition: transform 0.8s;
  transform-style: preserve-3d;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.is-flipped {
  transform: rotateY(180deg);
}

.card-face {
  position: absolute;
  width: 100%;
  height: 100%;
  overflow-y: auto;
  backface-visibility: hidden;
  box-sizing: border-box;
  padding: 1.5rem;
  font-size: 1.1rem;
  line-height: 1.6;
}

/* Vorderseite */
.card-front {
  background-color: #ffffff;
  box-shadow: inset 0 0 20px rgba(0, 0, 0, 0.05);
}

/* Rückseite */
.card-back {
  background-color: #f8f9fa;
  transform: rotateY(180deg);
  box-shadow: inset 0 0 20px rgba(0, 0, 0, 0.05);
}
</style>
