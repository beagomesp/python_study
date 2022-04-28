def hello(nome):
  print("hello {}".format(nome))



lista = ["florzinha", "docinho", "lindinha"]

for meninas in lista:
  print(meninas)

print("------")
print("------")

for index in range(len(lista)):

  if lista[index].startswith("l"):
    break
  hello(lista[index])