def EstudaEscopo():
    Y = X * 2
    print("X global existe dentro função: valor ={0}".format(X))
    print("Y local existente dentro função: valor = {0}".format(Y))

print("Inicio do Programa")
X = 10
print("X globla existe fora da função: valor = {0}".format(X))
EstudaEscopo()
print("Fim do Programa")