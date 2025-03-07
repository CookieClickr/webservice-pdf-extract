<template>
  <nav class="navbar navbar-expand-lg navbar-dark navbar-custom">
    <div class="container">
      <router-link class="navbar-brand d-flex align-items-center" to="/upload">
        <i class="bi bi-lightning-charge-fill me-2"></i>
        Flashcard Generator
      </router-link>
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarNav"
        aria-controls="navbarNav"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse justify-content-end" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item me-2">
            <router-link class="nav-link" to="/upload">PDF Upload</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/flashcards">Karteikarten</router-link>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'AppNavbar'
}
</script>

<style scoped>
.navbar-custom {
  /* Dezenten Farbverlauf von links nach rechts */
  background: linear-gradient(45deg, #3b82f6, #1e40af);
  /* Du kannst hier eigene Farben oder andere Farbtöne verwenden */
}

/* Brand-Icon (Blitzsymbol) etwas größer machen */
.bi-lightning-charge-fill {
  font-size: 1.3rem;
}
</style>
