<template>
  <div class="container">
    <h1>PDF Analyser</h1>
    <PdfUpload @file-selected="setFile" @reset="resetAll" />

    <div :class="{ 'dynamic-margin': jsonOutput }">
      <PdfAnalyser :file="selectedFile" @json-response="setJsonOutput" />
    </div>

    <PdfOutput :jsonData="jsonOutput" />
  </div>
</template>

<script>
import PdfUpload from "./components/PdfUpload.vue";
import PdfAnalyser from "./components/PdfAnalyser.vue";
import PdfOutput from "./components/PdfOutput.vue";

/**
 * Root App Component
 * Orchestrates PDF uploading, analysis, and output display.
 *
 * @component
 */
export default {
  name: "App",

  components: {
    PdfUpload,
    PdfAnalyser,
    PdfOutput,
  },

  data() {
    return {
      /**
       * Stores the selected PDF file.
       * @type {File|null}
       */
      selectedFile: null,

      /**
       * Stores the JSON analysis result.
       * @type {Object|null}
       */
      jsonOutput: null,
    };
  },

  methods: {
    /**
     * Sets the selected file from the PdfUpload component.
     * @param {File} file - The selected PDF file.
     */
    setFile(file) {
      this.selectedFile = file;
    },

    /**
     * Sets the JSON analysis result from the PdfAnalyser component.
     * @param {Object} data - The analysed JSON result.
     */
    setJsonOutput(data) {
      this.jsonOutput = data;
    },

    /**
     * Resets both the selected file and the JSON output when reset is triggered.
     */
    resetAll() {
      this.selectedFile = null;
      this.jsonOutput = null;
    },
  },
};
</script>

<style scoped>
/* Modern Glassmorphism Container */
.container {
  max-width: 600px;
  margin: 40px auto;
  padding: 30px;
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(12px);
  border-radius: 16px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
  transition: transform 0.3s ease-in-out;
  border: 1px solid rgba(255, 255, 255, 0.2);
  text-align: center;
}

h1 {
  font-size: 28px;
  font-weight: bold;
  margin-bottom: 20px;
  color: #fff;
  text-transform: uppercase;
  letter-spacing: 1.5px;
  text-shadow: 0 0 10px rgba(255, 255, 255, 0.2);
}

.dynamic-margin {
  margin-bottom: 30px;
}
</style>
