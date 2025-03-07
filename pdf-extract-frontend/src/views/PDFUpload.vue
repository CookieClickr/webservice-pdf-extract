<template>
  <div>
    <h2>PDF Upload</h2>
    <div class="mb-3">
      <label for="pdfFile" class="form-label">Wähle eine PDF-Datei aus:</label>
      <input type="file" class="form-control" id="pdfFile" accept="application/pdf" @change="handleFileChange">
    </div>
    <button class="btn btn-primary" :disabled="!file || generating" @click="uploadPDF">Generate Cards</button>

    <div v-if="generating" class="mt-3">
      <ProgressBar :progress="progress" />
      <p class="mt-2">Generierung läuft... {{ progress }}%</p>
    </div>
    <div v-if="errorMessage" class="alert alert-danger mt-3">{{ errorMessage }}</div>
  </div>
</template>

<script>
import axios from 'axios'
import ProgressBar from '../components/ProgressBar.vue'
import { store } from '../store'
import { ref } from 'vue'
import { useRouter } from 'vue-router'

export default {
  name: 'PDFUpload',
  components: { ProgressBar },
  setup() {
    const file = ref(null)
    const generating = ref(false)
    const progress = ref(0)
    const errorMessage = ref('')
    const router = useRouter()

    const handleFileChange = (event) => {
      if (event.target.files.length > 0) {
        file.value = event.target.files[0]
      }
    }

    const uploadPDF = () => {
      if (!file.value) {
        errorMessage.value = 'Bitte wähle eine PDF-Datei aus.'
        return
      }
      errorMessage.value = ''
      generating.value = true
      progress.value = 0

      const reader = new FileReader()
      reader.onload = async (e) => {
        const base64PDF = e.target.result.split(',')[1] // Entfernt den "data:"-Prefix
        try {
          // Simuliere einen Fortschrittsupdate (alternativ kann der Service echten Fortschritt liefern)
          const interval = setInterval(() => {
            if (progress.value < 90) {
              progress.value += 10
            } else {
              clearInterval(interval)
            }
          }, 500)

          // Sende die PDF (als Base64) an den Verwaltungs-Service
          const response = await axios.post('/analyse-pdf', { pdf: base64PDF })
          clearInterval(interval)
          progress.value = 100

          // Speichere die erhaltenen Flashcards im Store (alte Karteikarten werden überschrieben)
          store.flashcards = response.data.flashcards || []

          // Navigiere zur Flashcards-Ansicht
          router.push('/flashcards')
        } catch (error) {
          errorMessage.value = 'Fehler beim Hochladen oder Generieren der Karteikarten.'
          console.error(error)
        } finally {
          generating.value = false
        }
      }
      reader.readAsDataURL(file.value)
    }

    return {
      file,
      generating,
      progress,
      errorMessage,
      handleFileChange,
      uploadPDF
    }
  }
}
</script>

<style scoped>
/* Zusätzliche Styles können hier ergänzt werden */
</style>
