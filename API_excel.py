from flask import Flask, jsonify, request
import pandas as pd
import os

app = Flask(__name__)

# Caminho para o arquivo Excel (arquivo de "banco de dados")
excel_file = 'livros.xlsx'

# Função para ler os dados do arquivo Excel
def ler_livros():
    if os.path.exists(excel_file):
        # Ler o arquivo Excel e retornar os dados em forma de DataFrame
        df = pd.read_excel(excel_file)
        return df.to_dict(orient='records')
    else:
        # Se o arquivo não existir, retorna uma lista vazia
        return []

# Função para salvar os dados no arquivo Excel
def salvar_livros(df):
    df.to_excel(excel_file, index=False)

# Consultar todos os livros
@app.route('/livros', methods=['GET'])
def obter_livros():
    livros = ler_livros()
    return jsonify(livros)

# Consultar livro por ID
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_por_id(id):
    livros = ler_livros()
    for livro in livros:
        if livro['id'] == id:
            return jsonify(livro)
    return jsonify({"error": "Livro não encontrado"}), 404

# Criar novo livro
@app.route('/livros', methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros = ler_livros()
    
    # Criar um ID único para o novo livro
    if livros:
        novo_id = max(livro['id'] for livro in livros) + 1
    else:
        novo_id = 1

    novo_livro['id'] = novo_id
    livros.append(novo_livro)

    # Salvar os livros atualizados no arquivo Excel
    df = pd.DataFrame(livros)
    salvar_livros(df)

    return jsonify(novo_livro), 201

# Editar um livro existente
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro(id):
    livro_alterado = request.get_json()
    livros = ler_livros()
    for i, livro in enumerate(livros):
        if livro['id'] == id:
            livros[i].update(livro_alterado)
            # Salvar os livros atualizados no arquivo Excel
            df = pd.DataFrame(livros)
            salvar_livros(df)
            return jsonify(livros[i])
    return jsonify({"error": "Livro não encontrado"}), 404

# Excluir um livro
@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    livros = ler_livros()
    for i, livro in enumerate(livros):
        if livro['id'] == id:
            del livros[i]
            # Salvar os livros atualizados no arquivo Excel
            df = pd.DataFrame(livros)
            salvar_livros(df)
            return jsonify({"message": "Livro excluído com sucesso"})
    return jsonify({"error": "Livro não encontrado"}), 404

# Inicializar a API
if __name__ == '__main__':
    app.run(port=5000, host='localhost', debug=True)
