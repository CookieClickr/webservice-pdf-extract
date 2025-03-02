<template>
  <div class="output" v-if="jsonData">
    <h3>Analysis Result</h3>
    <font-awesome-icon
        icon="copy"
        class="clipboard-icon"
        @click="copyToClipboard"
        title="Copy to clipboard"
    />
    <pre>{{ formattedJson }}</pre>
  </div>
</template>

<script>
import { library } from "@fortawesome/fontawesome-svg-core";
import { faCopy } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";

// Add FontAwesome icons to the library
library.add(faCopy);

export default {
  name: "PdfOutput",
  components: { FontAwesomeIcon },

  /**
   * Component displaying JSON analysis results in a high-contrast, modern UI.
   * Provides a copy-to-clipboard function.
   *
   * @component
   * @prop {Object} jsonData - The JSON response from the processing service.
   */
  props: {
    jsonData: {
      type: Object,
      required: true,
    },
  },

  computed: {
    /**
     * Formats the JSON data with indentation for readability.
     * @returns {string} Pretty-formatted JSON string.
     */
    formattedJson() {
      return this.jsonData ? JSON.stringify(this.jsonData, null, 2) : "";
    },
  },

  methods: {
    /**
     * Copies the formatted JSON output to the clipboard.
     * Displays an alert on success and logs errors if any occur.
     */
    copyToClipboard() {
      navigator.clipboard.writeText(this.formattedJson)
          .then(() => alert("JSON copied to clipboard!"))
          .catch(err => console.error("Error copying", err));
    },
  },
};
</script>

<style scoped>
/* High-End Glassmorphic Design */
.output {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(12px);
  padding: 20px;
  border-radius: 10px;
  text-align: left;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
  border: 1px solid rgba(255, 255, 255, 0.2);
  position: relative;
  color: white;
  font-size: 15px;
  max-height: 300px;
  overflow-y: auto;
}

/* Styling for JSON output */
pre {
  white-space: pre-wrap;
  word-wrap: break-word;
  font-size: 14px;
  background: rgba(0, 0, 0, 0.3);
  padding: 12px;
  border-radius: 8px;
  color: #e0e0e0;
}

/* Copy to Clipboard Icon */
.clipboard-icon {
  position: absolute;
  top: 12px;
  right: 12px;
  cursor: pointer;
  font-size: 22px;
  color: #ddd;
  transition: 0.3s;
}

.clipboard-icon:hover {
  color: #00aeff;
}
</style>
