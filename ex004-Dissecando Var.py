# Dissecando uma variavel

msg = input("Digite algo: ")
print("O tipo primitivo desse valor é ", type(msg))
print("Só tem espaços? ", msg.isspace())
print("É um número? ", msg.isnumeric())
print("É alfabético? ", msg.isalpha())
print("É alfanumérico? ", msg.isalnum())
print("Esta em maiúsculas? ", msg.isupper())
print("Esta em minúsculas? ", msg.islower())
print("Esta capitalizada? ", msg.istitle())

