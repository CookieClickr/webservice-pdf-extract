<template>
  <div>
    <div
      class="drag-and-drop p-5 text-center"
      @dragover.prevent="onDragOver"
      @drop.prevent="onDrop"
      @click="triggerFileInput"
    >
      <template v-if="!selectedFile">
        <i class="bi bi-file-earmark-pdf display-3 mb-3 text-secondary"></i>
        <p class="mb-0 text-secondary">
          Ziehe deine PDF-Datei hierher oder klicke, um eine Datei auszuwählen.
        </p>
      </template>
      <template v-else>
        <i class="bi bi-file-earmark-pdf display-3 mb-3 text-primary"></i>
        <h4 class="mb-2 text-primary">{{ selectedFile.name }}</h4>
        <p class="text-muted small mb-0">
          Klicke, um eine andere Datei auszuwählen
        </p>
      </template>
      <input
        type="file"
        ref="fileInput"
        @change="onFileChange"
        style="display: none"
        accept="application/pdf"
      />
    </div>

    <!-- Overlay mit YouTube-nocookie-Video -->
    <div v-if="showOverlay" class="overlay-container">
      <div class="overlay-background"></div>
      <div class="overlay-content">
        <div class="video-wrapper">
          <iframe
            width="560"
            height="315"
            src="https://www.youtube-nocookie.com/embed/5KnSKS9S0AQ?autoplay=1&controls=0"
            frameborder="0"
            allow="autoplay; encrypted-media"
            allowfullscreen
          ></iframe>
        </div>
        <p class="overlay-text">Karten werden geladen ...</p>
      </div>
    </div>

    <DragAndDropNav
      @clear-input="clearInput"
      @start-analysis="startAnalysis"
      :file-selected="!!selectedFile"
      :disabled="generating"
      class="p-4"
    />
  </div>
</template>

<script>

import axios from 'axios'
import { store } from '@/store'
import DragAndDropNav from './DragAndDropNav.vue'

export default {
  name: 'DragAndDrop',
  components: {
    DragAndDropNav
  },
  data() {
    return {
      selectedFile: null,
      generating: false,   // Buttons deaktivieren
      showOverlay: false   // Subway Surfers (YouTube) Overlay
    }
  },
  methods: {
    onDragOver(event) {
      event.dataTransfer.dropEffect = 'copy'
    },
    onDrop(event) {
      const files = event.dataTransfer.files
      if (files.length > 0 && files[0].type === 'application/pdf') {
        this.handleFiles(files[0])
      } else {
        alert('Bitte nur eine PDF-Datei hochladen.')
      }
    },
    onFileChange(event) {
      const files = event.target.files
      if (files.length > 0 && files[0].type === 'application/pdf') {
        this.handleFiles(files[0])
      } else {
        alert('Bitte nur eine PDF-Datei hochladen.')
      }
    },
    handleFiles(file) {
      this.selectedFile = file
    },
    triggerFileInput() {
      this.$refs.fileInput.click()
    },
    clearInput() {
      this.selectedFile = null
      this.$refs.fileInput.value = ''
    },
    async startAnalysis() {
      if (!this.selectedFile) {
        alert('Bitte zuerst eine PDF-Datei auswählen.')
        return
      }
      // Buttons deaktivieren, Overlay einblenden
      this.generating = true
      this.showOverlay = true

      // Datei lesen und an Backend schicken
      const reader = new FileReader()
      reader.onload = async (e) => {
        const base64PDF = e.target.result.split(',')[1]
        try {
          const response = await axios.post('/analyse-pdf', { pdf: base64PDF })
          store.flashcards = response.data.flashcards || []
          // Ab hier fertig -> Overlay weg, Buttons wieder aktiv
          this.generating = false
          this.showOverlay = false
          // Navigation
          this.$router.push('/flashcards')
        } catch (error) {
          alert('Fehler beim Hochladen oder Generieren der Karteikarten.')
          console.error(error)
          this.generating = false
          this.showOverlay = false
        }
      }
      reader.readAsDataURL(this.selectedFile)
    }
  }
}
</script>

<style scoped>
.drag-and-drop {
  transition: all 0.2s ease;
  min-height: 240px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  border: 2px dashed #dee2e6;
  border-radius: 8px;
  background-color: #f8f9fa;
}

.drag-and-drop:hover {
  background-color: #e9ecef;
  border-color: #adb5bd;
  cursor: pointer;
}

.bi-file-earmark-pdf {
  transition: transform 0.2s ease;
}

.drag-and-drop:hover .bi-file-earmark-pdf {
  transform: scale(1.1);
}

/* Overlay-Stile */
.overlay-container {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 9999; /* ganz oben */
  display: flex;
  justify-content: center;
  align-items: center;
}

.overlay-background {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
}

.overlay-content {
  position: relative;
  z-index: 10000;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
  color: #fff;
}

.video-wrapper {
  background: #000;
  padding: 8px;
  border-radius: 8px;
}

.overlay-text {
  font-size: 1.2rem;
  margin-top: 0;
}
</style>
