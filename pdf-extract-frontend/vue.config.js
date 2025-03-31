const proxyTarget = process.env.VUE_APP_PROXY_TARGET || "http://10.50.15.53:5004";

module.exports = {
  devServer: {
    proxy: {
      '/analyse-pdf': {
        target: proxyTarget,
        changeOrigin: true,
        secure: false
      }
    }
  }
}
