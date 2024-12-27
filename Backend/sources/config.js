// config.js

const config = {
  PORT: process.env.PORT || 3000, // Usando variável de ambiente, se definida, ou 3000 como padrão
  TEST: false, // Corrigido com a vírgula aqui
  HOST: 'localhost' // Adicionada a string 'localhost' para o HOST
};

module.exports = config;
