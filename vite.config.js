import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  build: {
    // Configura la ruta de salida para que sea la carpeta 'dist' dentro del frontend
    outDir: 'dist',
    // Asegura que los assets se compilen en archivos únicos para el modo de producción
    rollupOptions: {
      output: {
        entryFileNames: 'assets/[name].js',
        chunkFileNames: 'assets/[name].js',
        assetFileNames: 'assets/[name].[ext]'
      }
    }
  },
  // La base debe apuntar al directorio raíz para que Streamlit pueda cargar los archivos
  base: './' 
})