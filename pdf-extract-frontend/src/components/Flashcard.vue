<template>
  <div class="flashcard-container" @click="flipCard">
    <div class="flashcard" :class="{ flipped: flipped }">
      <div class="front card">
        <div class="card-body">
          <h5 class="card-title">{{ card.title }}</h5>
          <p class="card-text">{{ card.front }}</p>
        </div>
      </div>
      <div class="back card">
        <div class="card-body">
          <p class="card-text">{{ card.back }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AppFlashcard',
  props: {
    card: {
      type: Object,
      required: true
    },
    flipped: {
      type: Boolean,
      default: false
    }
  },
  methods: {
    flipCard() {
      this.$emit('flip')
    }
  }
}
</script>

<style scoped>
.flashcard-container {
  perspective: 1000px;
  width: 300px;
  height: 200px;
  margin: 20px;
  cursor: pointer;
}
.flashcard {
  width: 100%;
  height: 100%;
  position: relative;
  transition: transform 0.6s;
  transform-style: preserve-3d;
}
.flashcard.flipped {
  transform: rotateY(180deg);
}
.flashcard .front, .flashcard .back {
  position: absolute;
  width: 100%;
  height: 100%;
  backface-visibility: hidden;
}
.flashcard .back {
  transform: rotateY(180deg);
}
</style>
