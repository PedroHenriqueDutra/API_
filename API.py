from flask import Flask, jsonify, request
import os

app = Flask(__name__)

# Lista de livros
livros = [
    {
        'id': 1,
        'título': 'O Senhor dos Anéis - A Sociedade do Anel',
        'autor': 'J.R.R Tolkien'
    },
    {
        'id': 2,
        'título': 'Harry Potter e a Pedra Filosofal',
        'autor': 'J.K Rowling'
    },
    {
        'id': 3,
        'título': 'Hábitos Atômicos',
        'autor': 'James Clear'
    },
]

# Pasta para armazenar as imagens
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


# Consultar todos os livros
@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)


# Consultar livro por id
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
    return jsonify({'message': 'Livro não encontrado'}), 404


# Editar livro por id
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])
    return jsonify({'message': 'Livro não encontrado'}), 404


# Criar novo livro
@app.route('/livros', methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(novo_livro), 201


# Excluir livro
@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
            return jsonify({'message': 'Livro excluído'})
    return jsonify({'message': 'Livro não encontrado'}), 404


# Subir imagem de capa
@app.route('/livros/<int:id>/capa', methods=['POST'])
def subir_imagem(id):
    if 'file' not in request.files:
        return jsonify({'message': 'Nenhum arquivo enviado'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'message': 'Nenhum arquivo selecionado'}), 400
    # Verificar a extensão do arquivo (opcional)
    if not file.filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        return jsonify({'message': 'Arquivo inválido. Apenas imagens são permitidas.'}), 400

    # Salvar o arquivo
    filename = f"livro_{id}_capa{os.path.splitext(file.filename)[1]}"
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)

    return jsonify({'message': 'Imagem de capa carregada com sucesso', 'caminho': filepath}), 201


# Rodar a aplicação
app.run(port=5000, host='localhost', debug=True)
