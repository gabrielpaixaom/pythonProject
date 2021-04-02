# Dobro, triplo e raiz quadrada de um número

n = int(input("Digite um número: "))
d = n * 2
t = n * 3
r = pow(n, 0.5)

print("O Dobro de {} é: {}.".format(n, d))
print("O Triplo de {} é: {}.".format(n, t))
print("A Raiz Quadrada de {} é: {:.2f}.".format(n, r))

