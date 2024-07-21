# --- Cabeçalho do programa
print("##### Calculadora em Python ##### \n############# Lab02 #############")          #Descrição do cabeçalho

# --- Estrutura do primeiro menu
print("\nDeseja realizar um novo cálculo?")           #Pergunta ao usuário se deseja iniciar o programa
print("1 - Sim")                                      #Opção positiva
print("2 - Não")                                      #Opção negativa
iniciar = int(input("\nDigite uma opção: "))          #Variável que solicita e guarda a resposta do usuário
print("*********************************")
iniciar_validos = [1, 2]                              #Lista contendo as respostas aceitas como válidas

# --- Quando a opção digitada for inválida:
while iniciar not in iniciar_validos:                                                                     #Enquanto a opção digitada não estiver na lista de opções válidas:
  print("\nOpção inválida! \nTente novamente:")                                                           #Mensagem de alerta ao usuário
  iniciar = int(input("\nDeseja realizar um novo cálculo? \n1 - Sim \n2 - Não \nDigite uma opção: "))     #Pergunta se o usuário quer voltar ao 1º menu ou encerrar o programa e guarda a resposta

# --- Quando a opção digitada positiva
while iniciar == 1:                                                                                       #Enquanto a opção digitada for positiva:
  # --- Estrutura do segundo menu
  print("\nSelecione a operação matemática:")                                                             #Mensagem que solicita uma resposta ao usuário
  print("1 - Adição (+)")                                                                                 #Opção adição
  print("2 - Subtração (-)")                                                                              #Opção subtração
  print("3 - Multiplicação (*)")                                                                          #Opção subtração    
  print("4 - Divisão (/)")                                                                                #Opção divisão
  print("5 - Potenciação (**)")                                                                           #Opção potenciação
  operacao_matematica = int(input("\nDigite uma opção: "))                                                #Variável que solicita e guarda uma nova resposta ao usuário
  print("*********************************")
  operacoes_validas = [1, 2, 3, 4, 5]                                                                     #Lista contendo as respostas aceitas como válidas

  # --- Quando a opção digitada for inválida
  while operacao_matematica not in operacoes_validas:                                                     #Enquanto a opção digitada não estiver na lista de opções válidas:
    print("Operação inválida!")                                                                           #Mensagem de alerta ao usuário
    operacao_matematica = int(input("\nDigite uma opção válida: "))                                       #Variável que solicita e guarda uma nova resposta ao usuário
    print("*********************************")

  # --- Quando a opção digitada for válida  
  primeiro_numero = int(input("Digite o primeiro número: "))                                              #Solicita ao usuário que informe o primeiro número
  segundo_numero = int(input("Digite o segundo número: "))                                                #Solicita que o usuário informe o segundo número
  if operacao_matematica == 1:                                                                            #Se a operação metemática for adição:
    print("\nResultado: ", primeiro_numero, "+", segundo_numero, "=", primeiro_numero + segundo_numero)   #Efetua o cálculo e imprime a resposta
    print("*********************************")
  elif operacao_matematica == 2:                                                                          #Se a operação metemática for subtração:                                                                                                                                                 
    print("\nResultado: ", primeiro_numero, "-", segundo_numero, "=", primeiro_numero - segundo_numero)   #Efetua o cálculo e imprime a resposta
    print("*********************************")
  elif operacao_matematica == 3:                                                                          #Se a operação metemática for multiplicação:
    print("\nResultado: ", primeiro_numero, "*", segundo_numero, "=", primeiro_numero * segundo_numero)   #Efetua o cálculo e imprime a resposta
    print("*********************************")
  elif operacao_matematica == 4:                                                                          #Se a operação metemática for divisão:
    if segundo_numero == 0:                                                                               #Se o segundo número informado pelo usuário for 0:
      print("\nNão é possível dividir por 0!")                                                            #Mensagem de alerta ao usuário
      print("*********************************")
    else:                                                                                                 #Se o segundo número informado pelo usuário não for 0:
      print("\nResultado: ", primeiro_numero, "/", segundo_numero, "=", primeiro_numero / segundo_numero) #Efetua o cálculo e imprime a resposta
      print("*********************************")
  elif operacao_matematica == 5:                                                                          #Se a operação matemática for potenciação:
    print("\nResultado: ", primeiro_numero, "**", segundo_numero, "=", primeiro_numero ** segundo_numero) #Efetua o cálculo e imprime a resposta
    print("*********************************")
  iniciar = int(input("\nDeseja realizar um novo cálculo? \n1 - Sim \n2 - Não \nDigite uma opção: "))     #Pergunta ao usuário se ele deseja reiniciar a aplicação
  print("*********************************")
  while iniciar not in iniciar_validos:                                                                   #Enquanto a opção digitada não estiver na lista de opções válidas:
    print("\nOpção inválida! \nTente novamente:")                                                         #Mensagem de alerta ao usuário
    iniciar = int(input("\nDeseja realizar um novo cálculo? \n1 - Sim \n2 - Não \nDigite uma opção: "))   #Variável que solicita e guarda uma nova resposta ao usuário

# --- Quando a opção digitada for negativa  
if iniciar == 2:                                                  #Se a resposta for negativa:
  print("\n##################################################")   
  print("############# Obrigado por utilizar! #############")     #Mensagem de agradecimento ao usuário
  print("Para realizar um novo cálculo reinicie o programa.")     #Mensagem com instruções de como usar o programa novamente
  print("######################## -Fim- ###################")     #Mensagem de encerramento do programa