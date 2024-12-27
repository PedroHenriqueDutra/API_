// routes.js

const express = require('express');  // Importa o express
const router = express.Router();     // Cria um roteador para definir as rotas

// Definindo a primeira rota ("/")
router.get('/helloworld', (req, res) => {
  res.send('Olá, Mundo!'); // Quando acessar a raiz, o servidor responde com "Olá, Mundo!"
});


router.get('/users/:id', (req, res) => {
    const userId = req.params.id;  // Acessa o parâmetro 'id' da URL
    res.send(`User ID is: ${userId}`);
 });

router.get('/itens', (req,res)=>{
    const name = req.query.name;// parametro /search?name=John
    res.send(`nome informado por ? (query) ${name}`)
})

router.get('/corpo', (req,res)=>{
  const name = req.body.name;// parametro /search?name=John
  res.send(`nome informado por json{} ${name}`)
})

router.get('/itens/teste', (req,res)=>{
  const name = req.body.name;// parametro /search?name=John
  res.send(`nome informado ${name}`)
})
router.post('/itens/teste', (req, res) => {
  const name = req.body.name;  // Acessa o parâmetro 'name' do corpo da requisição
  res.send(`nome informado pelo post ${name}`);  // Responde com o valor de 'name'
});

// Exporta o router para ser usado em outros arquivose
module.exports = router;
