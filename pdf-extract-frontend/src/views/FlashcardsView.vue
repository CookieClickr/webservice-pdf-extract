<template>
  <div>
    <h2>Karteikarten</h2>
    <div v-if="!hasCards" class="text-center mt-5">
      <div class="card">
        <div class="card-body">
          <h5 class="card-title">Hier erscheinen deine Karten</h5>
        </div>
      </div>
    </div>
    <div v-else>
      <div class="d-flex justify-content-center">
        <Flashcard :card="currentCard" @flip="toggleFlip" :flipped="flipped"/>
      </div>
      <div class="d-flex justify-content-between mt-3">
        <button class="btn btn-secondary" @click="prevCard" :disabled="currentIndex === 0">Zurück</button>
        <button class="btn btn-secondary" @click="nextCard" :disabled="currentIndex === flashcards.length - 1">Weiter</button>
      </div>
    </div>
  </div>
</template>

<script>
import { computed, ref } from 'vue'
import { store } from '../store'
import Flashcard from '../components/Flashcard.vue'

export default {
  name: 'FlashcardsView',
  components: { Flashcard },
  setup() {
    const flashcards = computed(() => store.flashcards)
    const currentIndex = ref(0)
    const flipped = ref(false)

    const currentCard = computed(() => flashcards.value[currentIndex.value] || {})

    const nextCard = () => {
      if (currentIndex.value < flashcards.value.length - 1) {
        currentIndex.value++
        flipped.value = false
      }
    }

    const prevCard = () => {
      if (currentIndex.value > 0) {
        currentIndex.value--
        flipped.value = false
      }
    }

    const toggleFlip = () => {
      flipped.value = !flipped.value
    }

    const hasCards = computed(() => flashcards.value.length > 0)

    return {
      flashcards,
      currentCard,
      currentIndex,
      nextCard,
      prevCard,
      flipped,
      toggleFlip,
      hasCards
    }
  }
}
</script>

<style scoped>
/* Zusätzliche Styles können hier ergänzt werden */
</style>
