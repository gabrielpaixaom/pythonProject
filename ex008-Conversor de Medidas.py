# Conversor de medidas

n = float(input("Digite uma distancia em metros: "))
mm = n * 1000
cm = n * 100
dm = n * 10
dam = n / 10
hm = n / 100
km = n / 1000
print('A media  de  {}m corresponde a \n{}km \n{}hm \n{}dam \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm'.format(n, km, hm, dam, dm, cm, mm))
