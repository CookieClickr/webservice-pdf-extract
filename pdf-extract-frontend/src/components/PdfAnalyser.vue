<template>
  <div>
    <button @click="analysePdf" :disabled="!file">Analyse</button>
    <div v-if="extractedText">
      <h3>Extracted Markdown:</h3>
      <pre>{{ extractedText }}</pre>
    </div>
  </div>
</template>

<script>
export default {
  name: "PdfAnalyser",
  props: {
    file: {
      type: File,
      required: true,
    },
  },
  data() {
    return {
      extractedText: "",
    };
  },
  methods: {
    analysePdf() {
      if (!this.file) return;
      console.log("Sending PDF for analysis:", this.file);

      // Optional: Überprüfe den MIME-Typ der Datei
      if (this.file.type !== "application/pdf") {
        console.error("Die ausgewählte Datei ist keine PDF.");
        this.$emit("json-response", { error: "Die ausgewählte Datei ist keine PDF." });
        return;
      }

      // Datei in Base64 umwandeln
      const reader = new FileReader();
      reader.onload = async (event) => {
        const result = event.target.result;
        // Entferne den data-URI Präfix, falls vorhanden
        const base64String = result.split(",")[1];

        // Logge einige Informationen zur Base64-Datenlänge und einem Ausschnitt
        console.log("Base64-String-Länge:", base64String.length);
        console.log("Erste 100 Zeichen:", base64String.slice(0, 100));

        try {
          // Sende die POST-Anfrage an den Verwaltungsservice
          const response = await fetch("/analyse-pdf", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ pdf: base64String }),
          });

          if (!response.ok) {
            throw new Error("Network response was not ok: " + response.statusText);
          }
          const data = await response.json();

          // Erwartet wird ein JSON mit einem "markdown" Feld
          this.extractedText = data.markdown;
          this.$emit("json-response", data);
        } catch (error) {
          console.error("Error analyzing PDF:", error);
          this.$emit("json-response", { error: error.message });
        }
      };

      reader.onerror = (error) => {
        console.error("Error reading file:", error);
        this.$emit("json-response", { error });
      };

      reader.readAsDataURL(this.file);
    },
  },
};
</script>
