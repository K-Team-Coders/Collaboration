/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./public/index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      fontFamily: {
        'TT_Firs_Neue':['TTFirsNeue-Regular']
      },
      colors:{
        'idealWhite':'#f5f5f5',
        'idealRed':'#FF1935',
        'idealDarkGray':'#2F3342',
        'idealSilver':'#E2E7EE',
        'idealLight Gray':'#BFCADA',
      },
      boxShadow: {
        '3xl': '0px 4px 7px 4px rgba(0, 0, 0, 0.3)',
        'cards': '4px 4px 4px 0px rgba(0, 0, 0, 0.5)'
      }
    },
  },
  plugins: [],
}