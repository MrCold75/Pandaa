/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          DEFAULT: '#2563EB',
          dark: '#1E40AF',
          light: '#3B82F6'
        },
        secondary: {
          DEFAULT: '#F97316',
          dark: '#EA580C',
          light: '#FB923C'
        },
        success: '#10B981',
        neutral: '#64748B'
      }
    },
  },
  plugins: [],
}
