from random import choice         # Importando os comandos necessarios de bibliotecas externa
from sys import exit
from time import sleep
from emoji import emojize

opcoes = ["PEDRA", "PAPEL", "TESOURA"]                                      #definindo as opções do computador, as regras em formato de dados na matriz vitoria, as variaveis importantes para o placar final
vitoria = [["PEDRA","TESOURA"], ["PAPEL" , "PEDRA"], ["TESOURA","PAPEL"]]
vitoria_jogador = 0
vitoria_computador = 0
empate = 0

pergunta = input("\nVocê deseja começar o JOKENPÔ? (Sim ou Não) ").strip().lower()       #variavel para iniciar o while 

if pergunta not in ("sim", "s"):                           #validção da entrada do usuário
    print("\033[31mO jogo NÃO SERÁ iniciado!!!\033[m")
    exit()

while pergunta in ("sim", "s"):
    print("\n\033[36m-=-=-=-=-=-=-=-=-=-=-=-=-JOKENPÔ-=-=-=-=-=-=-=-=-=-=-=-=-\033[m\n")

    computador = choice(opcoes)                                                                                                           #computador e
    jogador = input(emojize("\033[7;30;47mEscolha PEDRA:rock:, PAPEL:roll_of_paper: ou TESOURA:scissors: : \033[m")).strip().upper()      #usuário escolhendo
    
    print(emojize("\nPEDRA:rock:"))
    sleep(0.8)
    print(emojize("PAPEL:roll_of_paper:"))    #animação
    sleep(0.95)
    print(emojize("TESOURA:scissors:\n"))
    sleep(0.90)

    if jogador not in ["PEDRA", "PAPEL", "TESOURA"]:      #validção da entrada do usuário
        print("\033[31mSUA ESCOLHA É INVÁLIDA!!!\033[m")
        exit()
    
    print(f"\033[1;33mO jogador jogou {jogador}!!!\033[m")        #mostrando o que o jogador e o computador escolheram
    print(f"\033[1;34mO computador jogou {computador}!!!\033[m")
    sleep(1)
    
    if jogador == computador:
        print(f"\033[7;37;40mDeu EMPATE, pois ambas as partes escolheram {computador}!!!\033[m")   #todas as possibilidades de empate
        empate += 1
    elif [jogador,computador] in vitoria:
        print(f"\033[1;37;42mO jogador VENCEU, pois {jogador} ganha de {computador}!!!\033[m")     #todas as possibilidades de vitória do jogador, usando a matriz vitoria que representa as regras
        vitoria_jogador += 1
    else:
        print(f"\033[1;30;41mO computador VENCEU, pois {computador} ganha de {jogador}!!!\033[m")  #todas as possibilidades de vitoria do computador,
        vitoria_computador += 1                                                                    # vito que, se não foi empate ou vitoria do jogador só sobra vitoria do computador
   
    print("\n\033[36m-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\033[m\n")

    pergunta = input("\nVocê deseja CONTINUAR JOGANDO O jogo de JOKENPÔ? ").strip().lower()       #atualização da variavel do while 
                                                                                                  #final do jogo:
print(f"""\n\033[36m-=-=-=-=-=-=-=-=-=-=-=-FIM DE JOGO-=-=-=-=-=-=-=-=-=-=-=-\033[m\n 
ESTASTÍSTICAS FINAIS:
\033[1;30;42mVitórias do JOGADOR: {vitoria_jogador} \033[m
\033[1;30;41mVitórias do COMPUTADOR: {vitoria_computador} \033[m                              
\033[7;37;40mEMPATES: {empate} \033[m""")
print("\n\033[36m-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\033[m\n")