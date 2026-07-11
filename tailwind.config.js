/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        // Dark theme
        dark: {
          bg: '#0f0f11',
          'bg-alt': '#121214',
          surface: '#1a1a1d',
          border: '#2a2a2e',
          text: '#e4e4e7',
          'text-muted': '#8b8b8f',
        },
        // Light theme
        light: {
          bg: '#fafafa',
          'bg-alt': '#f4f4f5',
          surface: '#ffffff',
          border: '#e4e4e7',
          text: '#18181b',
          'text-muted': '#71717a',
        },
        // Accent colors
        profit: {
          DEFAULT: '#3ecf8e',
          light: '#22c55e',
        },
        loss: {
          DEFAULT: '#ef4444',
          light: '#dc2626',
        },
        accent: {
          DEFAULT: '#f97316',
          secondary: '#fb923c',
        }
      },
      fontFamily: {
        sans: ['Inter', 'Geist', 'sans-serif'],
      },
      borderRadius: {
        'md': '6px',
      }
    },
  },
  plugins: [],
}
