"""
time e pyplot
crie um programa para ajudar o usuario a escrever rapido. de a ele uma palavra e
peça para ele escreve-la cinco vezes. verifique quantos segundo isso levou.

no final, diga ao usuario quantos erros foram cometidos e mostre um grafico com a 
evolução da velocidade durante 5 rounds
"""
import time as t
import matplotlib.pyplot as plt 

def Grafico(y, x, erros):
    plt.plot(x, y)
    plt.title("Sua evolução")
    plt.xlabel("Vezes")
    plt.ylabel("Tempo")
    plt.show()

print("escreva a palavra 'Principal' 5 vezes seguidas o mais rapido possivel: ")
tentou = ["1","2","3","4","5"]  
tentativas = []
tempo = []
erros = 0

input("Aperte enter para começar")

while len(tentativas) <5:
    Hora_Começo = t.time()
    novo = input("agora: ")
    Hora_Fim = t.time()

    if novo.lower()!= "principal":
        erros += 1
        tentativas.append(novo)
    else:
        tentativas.append(novo)

    Delta_tempo = Hora_Fim - Hora_Começo
    tempo.append(round(Delta_tempo,2))

print("voce cometou: ", erros, " erro(s)")
print("grafico da sua evolução a seguir: ")
t.sleep(3)

Grafico(tempo, tentou, erros) #cria o grafico.

