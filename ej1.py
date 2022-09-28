# Declaramos el método invertir que recibirá como parámetro una variable (palabra) de tipo string.
def invertir(palabra):
    # Declaramos una variable solución de tipo string
    solucion=""

    # Creamos un bucle que recorrerá letra por letra la palabra que demos como parámetro
    for letra in palabra:

        # Al string solución le iremos agregando en primer lugar la letra por la que vayamos y el resto de la palara que estará guardada en solución
        solucion=letra+solucion

    # Devolvemos la solucion
    return solucion

# Llamamos al método pasando como parámetro el texto
print(invertir("asddaad"))
