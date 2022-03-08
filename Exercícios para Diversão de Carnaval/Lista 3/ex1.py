"""
Faça um programa que responda as seguintes perguntas:

1.	Quantos alunos estão matriculados na escola, no total?
2.	Quantos e quais estão matriculados APENAS em INGLES?
3.	Quantos e quais estão matriculados APENAS em FRANCES?
4.	Quantos e quais estão matriculados EM AMBOS os cursos?
5.	Quantos alunos estão matriculados somente em francês ou somente em inglês, mas não em ambos os cursos?


"""
turma_ingles = {"João Alves dos Santos", "Maria Magalhães", 
                "Antônio da Silva Ferreira", "José Júnior Jarbas", 
                "Henrique da Silva Sauro", "Joaquina Ferreira da Silva", 
                "Fabiana Aparecida Bianco", "Marrone Gutierres", 
                "Carlos Magno Farad", "Antônio da Silva Júnior Amaral"}

turma_frances = {"João Alves dos Santos", "Antônio da Silva Ferreira", 
                "Fernanda Abdala Mohamed", "Abner Mignon Alib", 
                "Alisson Figueiredo", 
                "Henrique da Silva Sauro", 
                "Maria Magalhães", "Marrone Gutierres", 
                "Joaquina Ferreira da Silva"}

total_turmas = turma_frances | turma_ingles
somente_ingles = turma_ingles - turma_frances
somente_frances = turma_frances - turma_ingles
ambas_turmas = turma_ingles & turma_frances


print(f"Total de alunos: {len(total_turmas)}")
print("Estes são:")
for i in total_turmas:
    print(i)
print(f"\nAlunos que fazem somente inglês: {len(somente_ingles)}")
for i in somente_ingles:
    print(i)
print(f"\nAlunos que fazem somente francês: {len(somente_frances)}")
for i in somente_frances:
    print(i)
print(f"\nAlunos que estão em ambos: {len(ambas_turmas)}")
for i in ambas_turmas:
    print(i)
