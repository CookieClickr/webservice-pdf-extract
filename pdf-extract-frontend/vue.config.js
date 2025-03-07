module.exports = {
  devServer: {
    proxy: {
      '/analyse-pdf': {
        target: 'http://localhost:5004',
        changeOrigin: true
      }
    }
  }
}
