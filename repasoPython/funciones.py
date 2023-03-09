# Entradas
base = float(input("Ingrese base: "))
altura = float(input("Ingrese altura: "))

# Proceso
def calcularAreaTriangulo(b,al):
    area = (b*al) / 2
    return area

# Salida
resultado = calcularAreaTriangulo(base,altura)
print("El area del triangulo es: ", resultado)

# Funcion con argumentos por defecto
def mostrarPais(pais = "Colombia"):
    print("Yo soy de: " + pais)

mostrarPais("Suiza")
mostrarPais("Ecuador")
mostrarPais()
mostrarPais("Brazil")