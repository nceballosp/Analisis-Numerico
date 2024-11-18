/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.htm",
    "./src/**/*.jsx",
  ],
  theme: {
    extend: {
      colors:{
        'azul1':'#184E77',
        'azul2':'#1E6091',
        'azul3':'#1A759F',
        'azul4':'#168AAD',
        'azul5':'#34A0A4',
        'verde1':'#52B69A',
        'verde2':'#76C893',
        'verde3':'#99D98C',
        'verde4':'#B5E48C',
        'verde5':'#D9ED92',
        'black':'#000000'
      }
    },
  },
  plugins: [],
}

