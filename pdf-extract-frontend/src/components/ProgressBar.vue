<template>
  <div class="mt-3">
    <div class="progress">
      <div class="progress-bar progress-bar-striped progress-bar-animated" role="progressbar"
           :style="{ width: progress + '%' }" :aria-valuenow="progress" aria-valuemin="0" aria-valuemax="100">
        {{ progress }}%
      </div>
    </div>
    <p class="mt-2">{{ message }}</p>
  </div>
</template>

<script>
export default {
  name: "ProgressDisplay",
  props: {
    progress: {
      type: Number,
      required: true
    },
    message: {
      type: String,
      required: true
    }
  }
}
</script>

<style scoped>
/* Optionale Styles */
</style>
