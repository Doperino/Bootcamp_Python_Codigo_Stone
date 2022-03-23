"""
Modifique o programa anterior para que aceite respostas com letras 
maiúsculas e minúsculas em todas as questões.
"""
#Dicionários com os alunos, suas respostas e o gabarito
respostas_alunos = {'Igor': ['a', 'b', 'c', 'c', 'd', 'e' ], 'Joao': ['b','c', 'e', 'a', 'b', 'c']}
gabarito = {'1': 'b', '2': 'c', '3': 'a', '4': 'c', '5': 'd', '6': 'e'}

#Crio um dicionário vazio que receberá posteriormente os alunos e suas notas
resultado = dict()

#Itero sobre o aluno e sua lista de respotas
for aluno, resp in respostas_alunos.items():
    pontos = 0
    #Extraio a lista de respostas do dicionário do aluno respectivo
    resp_extraidas = respostas_alunos[aluno]
    #Crio in índice que será reutilizado para cada aluno
    index_resp = 0
    #Itero sobre a questão e sua resposta no dicionário do gabarito
    for quest, gab in gabarito.items():
        #Comparo a resposta extraída do aluno com a do gabarito
        if resp_extraidas[index_resp] == gab:
            pontos += 1
        index_resp += 1
    #Finalizando a checagem, adiciono ao dicionário do respectivo aluno sua nota
    resultado[aluno] = pontos

print(resultado)

