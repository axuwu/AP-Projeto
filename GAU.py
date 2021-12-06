#IMPORTAÇÕES
import matplotlib.pyplot as plt; plt.rcdefaults()#importações de bibliotecas
import numpy as np
import matplotlib.pyplot as plt
import time
import pickle

print("---"*20) #INFORMAÇÕES INICIAIS

aluno = input("Indique o seu nome: ")#informações iniciais do utilizador
naluno = int(input("Indique o seu número de estudante: "))
nomedocurso = input("Indique o seu curso: ") 

print("---"*20) #PERCENTAGEM

test=float(input("Introduza o peso dos testes na sua avaliação para a disciplina pretendida , de 0 a 1 , ex: 0.1=10%: "))#peso das avaliações na disciplina
group=float(input("Introduza o peso dos trabalhos na sua avaliação , de 0 a 1 , ex: 0.1=10%: "))
presence=float(input("Introduza o peso das presenças ou outro restante elemento da sua avaliação , de 0 a 1 , ex:0.1=10%: "))
somatgp=((test)+(group)+(presence))
somartudo=np.round(somatgp,2)

if somartudo != 1:
  while True:
    print("Os pesos estão mal, a soma devia dar 1!")#se a soma dos pesos der diferente de 1 houve um erro do utilizador
    test=float(input("Introduza o peso dos testes na sua avaliação , de 0 a 1 , ex: 0.1=10%: "))
    group=float(input("Introduza o peso dos trabalhos na sua avaliação , de 0 a 1 , ex: 0.1=10%: "))
    presence=float(input("Introduza o peso das presenças ou outro restante elemento da sua avaliação , de 0 a 1 , ex:0.1=10%: "))
    somatgp=((test)+(group)+(presence))
    somartudo=np.round(somatgp,2)
    if somartudo == 1:
      break

print("---"*20) #Nota Desejada

mediao=input("Deseja simular quanto deverá ter na proxima avaliação para atingir a média desejada? [s/n] ")#nota que o utilizador deseja alcançar se ainda nao fez todas a avaliações
if mediao=="s" or mediao=="S":
    t1=float(input("Digite a sua nota do 1º teste: "))
    t2=float(input("Digite a sua nota do 2º teste, se falta a nota disto teste mete 0: "))
    tg=float(input("Digite a sua nota de trab. grupo, se falta a nota disto mete 0: "))
    pres=float(input("Digite a sua nota de presença, se fala a nota disto mete 0:"))
    desm=float(input("Que média final deseja obter? "))
    mediatesto=(((t1)+(t2))/2)
    while True: #que avaliações estão em falta 
        print("""ESCOLHA UMA OPCÇÃO , PARA QUAIS OS ELEMENTOS EM FALTA NA SUA AVALIAÇÃO
    [1] - 2º TESTE EM FALTA
    [2] - TRABALHO EM FALTA
    [3] - PRESENÇAS EM FALTA
    [4] - SAIR
    """)
        escolha=input("Escolhe uma opcção: ")      
        if escolha=="1":
            x=((((desm)-((tg)*(group))-((pres)*(presence)))*(2))/(test))-(t1)
            if x>20:
                print ("É matemáticamente impossivel obter a média selecionada dado as suas avaliações " )#se o utilizador selecionar uma nota impossivel de atingir
            else:
                print ("Necessita de obter classificação mínima de ",round(x,2), "valores , para atingir a classificação de ", (desm) ," valores")
        elif escolha=="2":
            x2=((desm)-((mediatesto)*(test))-((pres)*(presence)))/(group)
            if x2>20:
                print ("É matemáticamente impossivel obter a média selecionada dado as suas avaliações " )
            else:
                print ("Necessita de obter classificação mínima de ",round(x2,2), "valores , para atingir a classificação de ", (desm) ," valores")
        elif escolha=="3":
            x3=((desm)-((mediatesto)*(test))-((tg)*(group)))/(presence)
            if x3>20:
                print ("É matemáticamente impossivel obter a média selecionada dado as suas avaliações " )
            else:
                print ("Necessita de obter classificação mínima de ",round(x3,2), "valores , para atingir a classificação de ", (desm) ," valores")
        else:
            break


print("---"*20) #ADIÇÃO DAS DISCIPLINAS

curso = []#recolha de informação sobre as notas do utlizador
professores = []
nota_1teste = []
nota_2teste = []
nota_3teste = []
trabgrupo = []
trabgrupo2 = []
trabgrupo3 = []
presenca = []

escolha=True
while escolha: #Quando V mostra menu. Regime de avaliação do utilizador
    print ("""
    ESCOLHE UMA OPCÇÃO
    [1] - 2 TESTES + 1 TRAB. GRUPO/MINI-TESTE
    [2] - 2 TESTES + 2 TRAB. GRUPO/MINI-TESTE
    [3] - 2 TESTES + 3 TRAB. GRUPO/MINI-TESTE
    [4] - 3 TESTES + 1 TRAB. GRUPO/MINI-TESTE
    [5] - 3 TESTES + 2 TRAB. GRUPO/MINI-TESTE
    [6] - 3 TESTES + 3 TRAB. GRUPO/MINI-TESTE
    [7] - SAIR
    """)
    escolha=input("Escolhe uma opcção: ") 
    if escolha=="1": 
      print("\n 2 TESTES + 1 TRAB. GRUPO/MINI-TESTE") 
      while True:
          curso.append(input("Introduza uma disciplina: "))
          professores.append(input("Introduza o docente dessa disciplina: "))
          nota_1teste.append(float(input("Introduza a nota do 1º teste dessa disciplina: ")))
          nota_2teste.append(float(input("Introduza a nota do 2º teste dessa disciplina: ")))
          trabgrupo.append(float(input("Introduza a nota do trabalho de grupo dessa disciplina: ")))
          presenca.append(float(input("Introduza a nota da presença das aulas dessa disciplina: ")))
          print("As disciplinas são: {} e os seus respectivos docentes são: {}!".format(curso, professores))
          print("As disciplinas são: {} e as suas respectivas notas são: {} para o 1ºteste, {} para o 2º teste, {} para o trabalho de grupo e {} para a presença!".format(curso, nota_1teste, nota_2teste, trabgrupo, presenca))
          try_again = (input('''Deseja continuar a adicionar disciplinas? [s/n]
          R:'''))
          if try_again != "s" and try_again !="S":
              break # Sair do while loop
    elif escolha=="2":
      print("\n 2 TESTES + 2 TRAB. GRUPO/MINI-TESTE")
      while True:
          curso.append(input("Introduza uma disciplina: "))
          professores.append(input("Introduza o docente dessa disciplina: "))
          nota_1teste.append(float(input("Introduza a nota do 1º teste dessa disciplina: ")))
          nota_2teste.append(float(input("Introduza a nota do 2º teste dessa disciplina: ")))
          trabgrupo.append(float(input("Introduza a nota do trabalho de 1º grupo dessa disciplina: ")))
          trabgrupo2.append(float(input("Introduza a nota do trabalho de 2º grupo dessa disciplina: ")))
          presenca.append(float(input("Introduza a nota da presença das aulas dessa disciplina: ")))
          print("As disciplinas são: {} e os seus respectivos docentes são: {}!".format(curso, professores))
          print("As disciplinas são: {} e as suas respectivas notas são: {} para o 1ºteste, {} para o 2º teste, {} para o 1º trab de grupo, {} para o 2º trab grupo e {} para a presença!".format(curso, nota_1teste, nota_2teste, trabgrupo, trabgrupo2, presenca))
          try_again = (input('''Deseja continuar a adicionar disciplinas? [s/n]
          R:'''))
          if try_again != "s" and try_again !="S":
              break # Sair do while loop
    elif escolha=="3":
      print("\n 2 TESTES + 3 TRAB. GRUPO/MINI-TESTE")
      while True:
          curso.append(input("Introduza uma disciplina: "))
          professores.append(input("Introduza o docente dessa disciplina: "))
          nota_1teste.append(float(input("Introduza a nota do 1º teste dessa disciplina: ")))
          nota_2teste.append(float(input("Introduza a nota do 2º teste dessa disciplina: ")))
          trabgrupo.append(float(input("Introduza a nota do trabalho de 1º grupo dessa disciplina: ")))
          trabgrupo2.append(float(input("Introduza a nota do trabalho de 2º grupo dessa disciplina: ")))
          trabgrupo3.append(float(input("Introduza a nota do trabalho de 3º grupo dessa disciplina: ")))
          presenca.append(float(input("Introduza a nota da presença das aulas dessa disciplina: ")))
          print("As disciplinas são: {} e os seus respectivos docentes são: {}!".format(curso, professores))
          print("As disciplinas são: {} e as suas respectivas notas são: {} para o 1ºteste, {} para o 2º teste, {} para o 1º trab de grupo, {} para o 2º trab grupo, {} para o 3º trab de grupo e {} para a presença!".format(curso, nota_1teste, nota_2teste, trabgrupo, trabgrupo2, trabgrupo3, presenca))
          try_again = (input('''Deseja continuar a adicionar disciplinas? [s/n]
          R:'''))
          if try_again != "s" and try_again !="S":
              break # Sair do while loop
    elif escolha=="4":
        print("\n 3 TESTES + 1 TRAB. GRUPO/MINI-TESTE") 
        while True:
          curso.append(input("Introduza uma disciplina: "))
          professores.append(input("Introduza o docente dessa disciplina: "))
          nota_1teste.append(float(input("Introduza a nota do 1º teste dessa disciplina: ")))
          nota_2teste.append(float(input("Introduza a nota do 2º teste dessa disciplina: ")))
          nota_3teste.append(float(input("Introduza a nota do 3º teste dessa disciplina: ")))
          trabgrupo.append(float(input("Introduza a nota do trabalho de grupo dessa disciplina: ")))
          presenca.append(float(input("Introduza a nota da presença das aulas dessa disciplina: ")))
          print("As disciplinas são: {} e os seus respectivos docentes são: {}!".format(curso, professores))
          print("As disciplinas são: {} e as suas respectivas notas são: {} para o 1ºteste, {} para o 2º teste, {} para o 3º teste, {} para o 1º trab de grupo e {} para a presença!".format(curso, nota_1teste, nota_2teste, nota_3teste, trabgrupo, presenca))
          try_again = (input('''Deseja continuar a adicionar disciplinas? [s/n]
          R:'''))
          if try_again != "s" and try_again !="S":
              break # Sair do while loop
    elif escolha=="5":
        print("\n 3 TESTES + 2 TRAB. GRUPO/MINI-TESTE")
        while True:
          curso.append(input("Introduza uma disciplina: "))
          professores.append(input("Introduza o docente dessa disciplina: "))
          nota_1teste.append(float(input("Introduza a nota do 1º teste dessa disciplina: ")))
          nota_2teste.append(float(input("Introduza a nota do 2º teste dessa disciplina: ")))
          nota_3teste.append(float(input("Introduza a nota do 3º teste dessa disciplina: ")))
          trabgrupo.append(float(input("Introduza a nota do trabalho de grupo dessa disciplina: ")))
          trabgrupo2.append(float(input("Introduza a nota do trabalho de 2º grupo dessa disciplina: ")))
          presenca.append(float(input("Introduza a nota da presença das aulas dessa disciplina: ")))
          print("As disciplinas são: {} e os seus respectivos docentes são: {}!".format(curso, professores))
          print("As disciplinas são: {} e as suas respectivas notas são: {} para o 1ºteste, {} para o 2º teste, {} para o 3º teste, {} para o 1º trab de grupo, {} para o 2º trab grupo e {} para a presença!".format(curso, nota_1teste, nota_2teste, nota_3teste, trabgrupo, trabgrupo2, presenca))
          try_again = (input('''Deseja continuar a adicionar disciplinas? [s/n]
          R:'''))
          if try_again != "s" and try_again !="S":
              break # Sair do while loop
    elif escolha=="6":
        print("\n 3 TESTES + 3 TRAB. GRUPO/MINI-TESTE")
        while True:
          curso.append(input("Introduza uma disciplina: "))
          professores.append(input("Introduza o docente dessa disciplina: "))
          nota_1teste.append(float(input("Introduza a nota do 1º teste dessa disciplina: ")))
          nota_2teste.append(float(input("Introduza a nota do 2º teste dessa disciplina: ")))
          nota_3teste.append(float(input("Introduza a nota do 3º teste dessa disciplina: ")))
          trabgrupo.append(float(input("Introduza a nota do trabalho de 1º grupo dessa disciplina: ")))
          trabgrupo2.append(float(input("Introduza a nota do trabalho de 2º grupo dessa disciplina: ")))
          trabgrupo3.append(float(input("Introduza a nota do trabalho de 3º grupo dessa disciplina: ")))
          presenca.append(float(input("Introduza a nota da presença das aulas dessa disciplina: ")))
          print("As disciplinas são: {} e os seus respectivos docentes são: {}!".format(curso, professores))
          print("As disciplinas são: {} e as suas respectivas notas são: {} para o 1ºteste, {} para o 2º teste, {} para o 3º teste, {} para o 1º trab de grupo, {} para o 2º trab grupo, {} para o 3º trab de grupo e {} para a presença!".format(curso, nota_1teste, nota_2teste, nota_3teste, trabgrupo, trabgrupo2, trabgrupo3, presenca))
          try_again = (input('''Deseja continuar a adicionar disciplinas? [s/n]
          R:'''))
          if try_again != "s" and try_again !="S":
              break # Sair do while loop
    elif escolha=="7":
        print("\n SAIR")
        break
    elif escolha !="":
      print("\n ESCOLHA NÃO É VALIDA!") 

print("---"*20) #ESCREVE INFORMAÇÕES INICIAIS

print("O aluno", aluno, "que possui o seguinte número de aluno", naluno, "frequenta o curso de", nomedocurso, "que tem as seguintes disciplinas:", [[i] for i in curso], "e os seguintes docentes:", [[i] for i in professores])

print("---"*20) #MÉDIA . Calculo da média final das disciplinas inseridas

if len(nota_3teste) == 0 and len(trabgrupo2) == 0 and len(trabgrupo3) == 0:
    print('Média de 2 TESTES + 1 TRAB. GRUPO/MINI-TESTE')
    media = list((np.array((nota_1teste) + np.array(nota_2teste))/2)*test+np.array(trabgrupo)*group+np.array(presenca)*presence)
    arredondado=[[i] for i in media]
    print ("As médias de:", [[i] for i in curso], "são:",np.round(arredondado,2))
elif len(nota_3teste) == 0 and len(trabgrupo3) == 0:
    print('Média de 2 TESTES + 2 TRAB. GRUPO/MINI-TESTE')
    media = list((np.array((nota_1teste) + np.array(nota_2teste))/2)*test+(np.array((trabgrupo) + np.array(trabgrupo2))/2)*group+np.array(presenca)*presence)
    arredondado=[[i] for i in media]
    print ("As médias de:", [[i] for i in curso], "são:",np.round(arredondado,2))
elif len(nota_3teste) == 0:
    print('Média de 2 TESTES + 3 TRAB. GRUPO/MINI-TESTE')
    media = list((np.array((nota_1teste) + np.array(nota_2teste))/2)*test+(np.array((trabgrupo) + np.array(trabgrupo2)) + np.array(trabgrupo3)/3)*group+np.array(presenca)*presence)
    arredondado=[[i] for i in media]
    print ("As médias de:", [[i] for i in curso], "são:",np.round(arredondado,2))
elif len(trabgrupo2) == 0 and len(trabgrupo3) == 0:
    print('Média de 3 TESTES + 1 TRAB. GRUPO/MINI-TESTE')
    media = list((np.array((nota_1teste) + np.array(nota_2teste) + np.array(nota_3teste))/3)*test+np.array(trabgrupo)*group+np.array(presenca)*presence)
    arredondado=[[i] for i in media]
    print ("As médias de:", [[i] for i in curso], "são:",np.round(arredondado,2))
elif len(trabgrupo3) == 0:
    print('Média de 3 TESTES + 2 TRAB. GRUPO/MINI-TESTE')
    media = list((np.array((nota_1teste) + np.array(nota_2teste) + np.array(nota_3teste))/3)*test+(np.array((trabgrupo) + np.array(trabgrupo2))/2)*group+np.array(presenca)*presence)
    arredondado=[[i] for i in media]
    print ("As médias de:", [[i] for i in curso], "são:",np.round(arredondado,2))
else:
    print('Média de 3 TESTES + 3 TRAB. GRUPO/MINI-TESTE')
    media = list((np.array((nota_1teste) + np.array(nota_2teste) + np.array(nota_3teste))/3)*test+(np.array((trabgrupo) + np.array(trabgrupo2)) + np.array(trabgrupo3)/3)*group+np.array(presenca)*presence)
    arredondado=[[i] for i in media]
    print ("As médias de:", [[i] for i in curso], "são:",np.round(arredondado,2))
    
print("---"*20) #TABELA

print('''
Nome: {}
Nº de aluno: {}
Curso: {}
'''.format(aluno, naluno, nomedocurso))
final=np.array(["Disciplinas" , "Docente", "Média"])

print(np.tile(final, 1))
print(np.dstack((curso, professores, media)))

print("---"*20) #GRÁFICO VERTICAL

time.sleep(1)

y_pos=np.arange(len(curso))

plt.bar(y_pos, media, align='center', alpha=0.5)
plt.xticks(y_pos, curso)
plt.ylabel('NOTA')
plt.xlabel('DISCIPLINA')
plt.title('GRÁFICO - MÉDIA')
 
plt.show()

print("---"*20) #GRÁFICO HORIZONTAL

elemento=[]
nota=[]

print("\n Gráfico da nota para uma disciplina")
elemento.append(input("Introduzir nome para o 1º teste: "))
elemento.append(input("Introduzir nome para o 2º teste: "))
elemento.append(input("Introduzir nome para o trab. grupo/mini-teste: "))
elemento.append(input("Introduzir nome para o presença: "))
nota.append(float(input("Introduzir a nota do 1º teste:")))
nota.append(float(input("Introduzir a nota do 2º teste:")))
nota.append(float(input("Introduzir a nota do trab. grupo/mini-teste:")))
nota.append(float(input("Introduzir a nota da presença:")))

print(elemento)
y_pos=np.arange(len(elemento))

plt.barh(y_pos, nota, align='center', alpha=0.5)
plt.yticks(y_pos, elemento)
plt.ylabel('ELEMENTOS DE AVALIAÇÃO')
plt.xlabel('VALOR DA NOTA')
plt.title('GRÁFICO - NOTA DA DISCIPLINA')
 
plt.show()

print("---"*20)

#Procedimento para Ler e Afixar o conteúdo do ficheiro texto nomeF
def lerAfixar(nomeF):
    fich1=open(nomeF,'r') # abre o ficheiro em modo 'r'-leitura
    texto=fich1.read() # lê do ficheiro
    print(texto) # afixa no ecran o conteudo do ficheiro texto
    fich1.close() # fecha o ficheiro texto

#Procedimento para gravar em ficheiro texto os elementos da matriz
def gravaMatrizFichTexto(matriz, nomeF):
    fich1=open(nomeF,'w')
    fich1.write('AVALIAÇÃO CONTÍNUA 1.º ANO/1.º SEM EI\n Ficheiro Texto') #escreve no ficheiro
    print(file=fich1)# introduz uma nova linha no ficheiro
    for i in range(0,len(matriz)): # ciclo i para as linhas da matriz
        print(file=fich1)#adiciona uma linha em branco no ficheiro
        for j in range(len(matriz[i])): # ciclo j para as colunas da matriz
            print('{0:6}'.format(matriz[i][j]),end=' | ',file=fich1)#print do elemento da matriz i,j 
        # em 6 digitos '{0:6}' 
        # na mesma linha separados com espaços e | (end=' | ')
        print(file=fich1) 
    print('_'*len(matriz[1])*9,file=fich1) #adiciona uma linha de '_'*len(matriz[1])*9
                                # 9 corresponde aos 9 espaços (6+3) para cada elemento
    fich1.close()

#Matriz:
matriz=[curso, professores, nota_1teste, nota_2teste, trabgrupo, presenca] #inicia a matriz
nomeF='AVALIAÇÃO CONTÍNUA' #nome do ficheiro em memória secundária

gravaMatrizFichTexto(matriz,nomeF) #chama o procedimento gravaMatrizFichTexto
lerAfixar(nomeF)#chama o procedimento lerAfixar o conteudo do ficheiro texto

print("---"*20)

# serializar a lista ap no ficheiro fich.pkl
with open('fich.pkl','wb') as f: 
    pickle.dump(matriz,f)
f.close()

# des-serializar a lista ap gravada em fich.pkl
with open('fich.pkl','rb') as f:
    matrizLida=pickle.load(f)
    print(matrizLida)
f.close()










