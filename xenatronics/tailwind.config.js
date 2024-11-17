/** @type {import('tailwindcss').Config} */
module.exports = {
   content: [
    './templates/**/*.html', // Inclure tous les fichiers HTML dans templates
    './templates/**/*.twig', // (si Twig est utilisé)
    './static/**/*.js', // Inclure les fichiers JS si des classes dynamiques sont utilisées
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

