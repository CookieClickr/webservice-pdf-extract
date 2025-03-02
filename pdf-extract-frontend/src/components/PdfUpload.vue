<template>
  <div class="drop-zone" @dragover.prevent @drop="handleDrop">
    <p v-if="!selectedFile">Drag a PDF here or click to select a file</p>
    <p v-else>{{ selectedFile.name }}</p>
    <input type="file" accept="application/pdf" @change="handleFileSelect" ref="fileInput" hidden />
    <button v-if="!selectedFile" @click="triggerFileInput">Select File</button>
    <button v-else class="reset-button" @click="resetFile">Reset</button>
  </div>
</template>

<script>
/**
 * PdfUpload Component
 * Provides drag-and-drop or manual selection for uploading PDF files.
 *
 * @component
 * @event file-selected - Emits the selected file to the parent component.
 * @event reset - Emits a reset event to clear selected file and output.
 */
export default {
  name: "PdfUpload",

  data() {
    return {
      /**
       * Stores the selected PDF file.
       * @type {File|null}
       */
      selectedFile: null,
    };
  },

  methods: {
    /**
     * Handles PDF file selection via drag-and-drop.
     * Emits the file if it's valid.
     * @param {DragEvent} event - The drag event.
     */
    handleDrop(event) {
      event.preventDefault();
      const files = event.dataTransfer.files;
      if (files.length > 0 && files[0].type === "application/pdf") {
        this.selectedFile = files[0];
        /**
         * @event file-selected
         * @type {File}
         */
        this.$emit("file-selected", this.selectedFile);
      } else {
        alert("Please upload only PDFs!");
      }
    },

    /**
     * Handles PDF file selection via file input dialog.
     * Emits the file if it's valid.
     * @param {Event} event - The change event.
     */
    handleFileSelect(event) {
      const file = event.target.files[0];
      if (file && file.type === "application/pdf") {
        this.selectedFile = file;
        this.$emit("file-selected", this.selectedFile);
      } else {
        alert("Please upload only PDFs!");
      }
    },

    /**
     * Triggers the hidden file input dialog.
     */
    triggerFileInput() {
      this.$refs.fileInput.click();
    },

    /**
     * Resets the selected file and emits a reset event.
     */
    resetFile() {
      this.selectedFile = null;
      this.$emit("reset");
    },
  },
};
</script>

<style scoped>
/* Modern Glassmorphic Drag & Drop Zone */
.drop-zone {
  border: 2px dashed rgba(255, 255, 255, 0.5);
  padding: 25px;
  border-radius: 12px;
  margin-bottom: 20px;
  background: rgba(255, 255, 255, 0.05);
  transition: 0.3s ease-in-out;
  cursor: pointer;
  text-align: center;
}

.drop-zone:hover {
  border-color: #00aeff;
  background: rgba(255, 255, 255, 0.1);
}

.drop-zone p {
  font-size: 14px;
  color: #ddd;
}

/* Select & Reset Buttons */
button {
  background: linear-gradient(135deg, #00aeff 0%, #007bff 100%);
  color: white;
  border: none;
  padding: 12px 18px;
  font-size: 16px;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.3s ease-in-out;
  font-weight: bold;
  box-shadow: 0 10px 30px rgba(0, 174, 255, 0.4);
  position: relative;
}

button:hover {
  background: linear-gradient(135deg, #007bff 0%, #0056b3 100%);
  box-shadow: 0 8px 20px rgba(0, 174, 255, 0.6);
}

/* Reset Button Styling */
.reset-button {
  background: linear-gradient(135deg, #ff5252 0%, #d32f2f 100%);
}

.reset-button:hover {
  background: linear-gradient(135deg, #d32f2f 0%, #b71c1c 100%);
}
</style>
