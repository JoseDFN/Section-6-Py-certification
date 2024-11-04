colores = ["Rojo", "Verde", "Azul", "Amarillo"]

print(colores[0])
print(colores[-1])
print(len(colores))

colores.append('Negro')
print(colores)
colores.remove('Negro')
print(colores)
colores[0] = "rojo"
print (colores)
"rojo" in colores

L2 = ["yay", "idk", "LOL"]

Lnueva = colores + L2

print(Lnueva)

frutas = ["manzana", "pera", "banano"]

Lnueva.extend(frutas)

print(Lnueva)

vegetales = ["brocoli", "zanahoria"]

Lnueva.insert(2, vegetales)

print(Lnueva)

Lnueva.remove("yay")

Lnueva.pop(2)

tupla = ()

print(type(tupla))