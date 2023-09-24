
from flask import Flask, jsonify, request

app = Flask (__name__)

aluno = [
{
    'id': 1,
    'nome': 'Nicoly',
    'idade': 18,
},
{
    'id': 2,
    'nome': 'Allan',
    'idade': 21,
},
{
    'id': 3,
    'nome': 'Helloysa',
    'idade': 16,
}
]

#Consultar (todos) - GET
#Eu coloco a barra para acrescentar no final do meu link(minhas rotas)
@app.route('/aluno', methods=['GET'])
def obter_nomes():
    return jsonify(aluno)

#Consultar (id)
#espero um  numero inteiro que sera identificado como id
@app.route('/aluno/<int:id>', methods = ['GET'])
def obter_aluno_com_id(id):
    for alunoid in aluno: #Ele vai percorrer todos os alunos
        if alunoid.get('id') == id:
            return jsonify(aluno)
        
        
@app.route('/aluno/<int:id>', methods = ['PUT']) 
def editar_aluno(id):
    aluno_alterado = request.get_json()
    for indice, alunoid in enumerate(aluno):
        if alunoid.get('id') == id:
            aluno[indice].update(aluno_alterado)
            return jsonify(aluno[indice])
        

@app.route('/aluno/', methods = ['POST'])
def incluir_novo_aluno():
    novo_aluno = request.get_json()
    aluno.append(novo_aluno)
    
    return jsonify(aluno)


@app.route('/aluno/<int:id>', methods = ['DELETE'])
def excluir_aluno(id):
    for indice, alunoid in enumerate(aluno):
        if alunoid.get('id') == id:
            del aluno[indice]
    return jsonify(aluno)


app.run(port=5000, host='localhost', debug =True )