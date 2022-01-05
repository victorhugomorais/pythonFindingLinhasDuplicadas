leitura2 = open('texto2.txt', 'w',encoding='UTF8')

leitura = open('texto.txt', 'r', encoding='UTF8')

vetor = []

for line in leitura:

    if(len(vetor) > 0 ):
        if(line in vetor):
            leitura2.write(line)
    vetor.append(line)
