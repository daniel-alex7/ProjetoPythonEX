nomes = []
notas = []
cursos = []

N = int(input("Quantos alunos deseja cadastrar? "))

for i in range(N):
    nome = input(f"Digite o nome do aluno {i+1}: ")
    nota = float(input(f"Digite a nota do aluno {i+1}: "))
    curso = input(f"Digite o curso do aluno {i+1} (ccp ou tads): ")
    
    nomes.append(nome)
    notas.append(nota)
    cursos.append(curso)


alunos_tads = cursos.count('tads')


media_notas = sum(notas) / len(notas)


alunos_acima_media = sum(1 for nota in notas if nota > media_notas)

print(f"Quantidade de alunos do curso TADS: {alunos_tads}")
print(f"Média das notas dos alunos: {media_notas:.2f}")
print(f"Quantidade de alunos com nota acima da média: {alunos_acima_media}")
