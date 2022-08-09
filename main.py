diccionario = {"codigo": ["e-001", "e-002", "e-003", "e-004", "e-005", ],
                   "nombre": ["leche", "azucar", "arroz", "atun", "fideo", ],
                   "precio": ["6", "4", "5", "5", "3"]}
for key in diccionario:
    print(key, ":", diccionario[key])
continuar = "s"
contar =0
while continuar == "s":
    codigo = input("Ingrese el codigo: ")
    cantidad = int(input("Ingrese la cantidad: "))
    if codigo == "e-001":
        precio = 6
        producto = "leche"
        contar
    if codigo == "e-002":
        precio = 4
        producto = "azucar"
        contar
    if codigo == "e-003":
        precio = 5
        producto = "arroz"
        contar
    if codigo == "e-004":
        precio = 5
        producto = "atun"
        contar = ""
    if codigo == "e-005":
        precio = 3
        producto = "fideo"
        contar


    print("El producto es: ", producto)
    print("El precio es: ", precio)
    total = precio * cantidad
    print("El monto es: ", total)
    print("Desea continuar Si (s) No (n)")
    continuar = input()
    contar += total
    tupla = [str(codigo), " ", producto , " ", str(cantidad), " ", str(precio), " ", str(total)]
    cadena = "".join(tupla)
    f = open("demofile.txt", "a")
    f.write("\n" + cadena)
    f.close()
f = open("demofile.txt")
print(f.read())
f.close()
print("El precio total es: ", contar)


