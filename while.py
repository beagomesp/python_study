print("Adivinhe o numero!")
comando = 1

while(comando!= 0):
  comando = int(input("Digite um numero:"))

  if (comando == 2):
    print ("Descobriu!")
    break
  else :
    print ("Errou tente novamente!")