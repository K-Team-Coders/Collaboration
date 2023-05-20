/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./public/index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      fontFamily: {
        'TT_Firs_Neue':['TTFirsNeue']
      },
      colors:{
        'idealWhite':'#f5f5f5',
        'idealRed':'#FF1935',
        'idealDarkGray':'#2F3342',
        'idealSilver':'#E2E7EE',
        'idealLight Gray':'#BFCADA',
      }

    },
  },
  plugins: [],
}