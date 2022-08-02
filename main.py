diccionario = {"codigo":["e-001", "e-002", "e-003", "e-004", "e-005",], "nombre":["leche", "azucar", "arroz", "atun", "fideo",], "precio":["6", "4", "5", "5", "3"]}
print(diccionario)
for key in diccionario:
    print(key, ":", diccionario[key])

continuar = True
while continuar:
    codigo = (input("Introducir el codigo del producto: "))
    cantidad = int(input("Ingresar la cantidad de productos: "))
    continuar = input("¿Desea añadir mas articulos a la lista (Si/No)? ") == "Si"
coste = 0
print("Lista de compra")
for nombre, precio, in diccionario.items():
    print(codigo, '\t', nombre, '\t', precio, '\t', cantidad)
