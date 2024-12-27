// Importando dependências
const express = require('express');
const config = require('./config'); // Arquivo de configuração para constantes como a porta
const routes = require('./routes'); // Arquivo de rotas

// Criando a instância do aplicativo Express
const app = express();

// Usando middlewares
app.use(express.json()); // Para parsear JSON no corpo das requisições

// Registrando as rotas
app.use('/', routes); // Definindo as rotas da aplicação

// Iniciando o servidor
app.listen(config.PORT, () => {
  console.log(`Servidor rodando na porta ${config.PORT}\n https:\\\\${config.HOST}:${config.PORT}`);
});

