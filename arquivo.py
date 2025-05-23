with open('to-do-list_notas.txt', 'w') as arquivo:
    arquivo.write("Estudar AWS.\n")
    arquivo.write("Praticar Inglês.\n")
    arquivo.write("Revisar anotações.\n")

with open('minhas_notas.txt', 'a') as arquivo:
    arquivo.write("relaxar.\n")
    arquivo.write("Ler.\n")

with open('to-do-list_notas.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)