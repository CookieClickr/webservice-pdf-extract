<template>
  <div class="display-card-view">
    <h1 class="title">Deine Karteikarten</h1>

    <div v-if="currentCard" class="fixed-card-container">
      <DisplayCard :card="currentCard" ref="displayCard" />

      <DisplayCardNav
        @previous="previousCard"
        @flip="flipCard"
        @next="nextCard"
        :isFirst="currentIndex === 0"
        :isLast="currentIndex === (flashcards.length - 1)"
      />
    </div>
    <div v-else-if="flashcards.length === 0" class="no-cards-message">
      <h2>Keine Karten vorhanden.</h2>
      <p>Bitte lade eine PDF hoch, um Karteikarten zu erstellen.</p>
    </div>
    <div v-else class="completion-message">
      <h2>🎉 Herzlichen Glückwunsch!</h2>
      <p>Dieser Stapel ist erledigt!</p>
    </div>
  </div>
</template>

<script>
import { ref, computed } from 'vue'
import { store } from '@/store'
import DisplayCard from '@/components/DisplayCard.vue'
import DisplayCardNav from '@/components/DisplayCardNav.vue'

export default {
  name: 'DisplayCardView',
  components: {
    DisplayCard,
    DisplayCardNav,
  },
  setup() {
    const flashcards = computed(() => store.flashcards)
    const currentIndex = ref(0)

    const currentCard = computed(() => {
      if (flashcards.value.length === 0) return null
      if (currentIndex.value >= flashcards.value.length) return null
      return flashcards.value[currentIndex.value]
    })

    const nextCard = () => {
      if (currentIndex.value < flashcards.value.length - 1) {
        currentIndex.value++
      } else {
        // Alle Karten durch
        currentIndex.value = flashcards.value.length
      }
    }

    const previousCard = () => {
      if (currentIndex.value > 0) {
        currentIndex.value--
      }
    }

    const displayCard = ref(null)
    const flipCard = () => {
      displayCard.value?.flip()
    }

    return {
      flashcards,
      currentIndex,
      currentCard,
      nextCard,
      previousCard,
      flipCard,
      displayCard
    }
  }
}
</script>

<style scoped>
.display-card-view {
  padding: 2rem 1rem;
  text-align: center;
}

.title {
  margin-bottom: 1rem;
}

.fixed-card-container {
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
}

.no-cards-message,
.completion-message {
  margin-top: 2rem;
}
</style>
