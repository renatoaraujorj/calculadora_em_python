print("##### Calculadora em Python ##### \n############# Lab02 #############")
print("\nDeseja realizar um novo cálculo?")
print("1 - Sim")
print("2 - Não")
iniciar = int(input("\nDigite uma opção: "))
print("*********************************")
iniciar_validos = [1, 2]
while iniciar not in iniciar_validos:
  print("\nOpção inválida! \nTente novamente:")
  iniciar = int(input("\nDeseja realizar um novo cálculo? \n1 - Sim \n2 - Não \nDigite uma opção: "))
while iniciar == 1:
  print("\nSelecione a operação matemática:")
  print("1 - Adição (+)")
  print("2 - Subtração (-)")
  print("3 - Multiplicação (*)")
  print("4 - Divisão (/)")
  print("5 - Potenciação (**)")
  operacao_matematica = int(input("\nDigite uma opção: "))
  print("*********************************")
  operacoes_validas = [1, 2, 3, 4, 5]
  while operacao_matematica not in operacoes_validas:
    print("Operação inválida!")
    operacao_matematica = int(input("\nDigite uma opção válida: "))
    print("*********************************")
  primeiro_numero = int(input("Digite o primeiro número: "))
  segundo_numero = int(input("Digite o segundo número: "))
  if operacao_matematica == 1:
    print("\nResultado: ", primeiro_numero, "+", segundo_numero, "=", primeiro_numero + segundo_numero)
    print("*********************************")
  elif operacao_matematica == 2:
    print("\nResultado: ", primeiro_numero, "-", segundo_numero, "=", primeiro_numero - segundo_numero)
    print("*********************************")
  elif operacao_matematica == 3:
    print("\nResultado: ", primeiro_numero, "*", segundo_numero, "=", primeiro_numero * segundo_numero)
    print("*********************************")
  elif operacao_matematica == 4:
    if segundo_numero == 0:
      print("\nNão é possível dividir por 0!")
      print("*********************************")
    else:
      print("\nResultado: ", primeiro_numero, "/", segundo_numero, "=", primeiro_numero / segundo_numero)
      print("*********************************")
  elif operacao_matematica == 5:
    print("\nResultado: ", primeiro_numero, "**", segundo_numero, "=", primeiro_numero ** segundo_numero)
    print("*********************************")
  iniciar = int(input("\nDeseja realizar um novo cálculo? \n1 - Sim \n2 - Não \nDigite uma opção: "))
  print("*********************************")
  while iniciar not in iniciar_validos:
    print("\nOpção inválida! \nTente novamente:")
    iniciar = int(input("\nDeseja realizar um novo cálculo? \n1 - Sim \n2 - Não \nDigite uma opção: "))
if iniciar == 2:
  print("\n##### Obrigado por utilizar! #####")
  print("############## Fim ###############")