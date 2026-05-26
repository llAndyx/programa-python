# ---------------------------
# MATRIZ DE TÍTULOS
# ---------------------------

videoteca = [
    ["Inception", 2010, 9, "Ciencia Ficción"],
    ["Avengers: Endgame", 2019, 8, "Acción"],
    ["Interstellar", 2014, 10, "Ciencia Ficción"],
    ["Batman", 2022, 8, "Acción"],
    ["Coco", 2017, 9, "Animación"],
    ["Joker", 2019, 8, "Drama"],
    ["Dune", 2021, 9, "Ciencia Ficción"]
]


# -------------------------------------------------
# FUNCIÓN PARA CONTAR LOS TÍTULOS QUE CUMPLEN
# LOS CRITERIOS
# -------------------------------------------------
def contar_titulos(matriz, calificacion_minima, anio_limite):

    # Variable contador
    contador = 0

    # Recorremos toda la matriz
    for titulo in matriz:

        # Guardamos los datos importantes de cada fila
        nombre = titulo[0]
        anio = titulo[1]
        calificacion = titulo[2]

        # Verificamos si cumple ambos criterios
        if calificacion >= calificacion_minima and anio >= anio_limite:

            # Si cumple, aumentamos el contador
            contador += 1

            # Mostramos el título encontrado
            print("Título que cumple:", nombre)

    # Retornamos el total
    return contador


# ------------------------------------
# DATOS QUE INGRESA EL USUARIO
# ------------------------------------

calificacion_busqueda = int(input("Ingrese la calificación mínima: "))
anio_busqueda = int(input("Ingrese desde qué año buscar: "))


# ------------------------------------
# LLAMADO DE LA FUNCIÓN
# ------------------------------------
total = contar_titulos(
    videoteca,
    calificacion_busqueda,
    anio_busqueda
)


# ------------------------------------
# RESULTADO FINAL
# ------------------------------------
print("\nCantidad total de títulos encontrados:", total)