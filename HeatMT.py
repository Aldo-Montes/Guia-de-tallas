# 28/03/2026
print("--- Asesor de Tallas: Montes Streetwear ---")
print("Descubre tu fit ideal para nuestra nueva colección.\n")

# 1. Función para calcular la talla de arriba (Playeras Oversize / Hoodies)
def calcular_talla_playera(pecho_cm):
    if pecho_cm < 95:
        return "Chica (S)"
    elif pecho_cm >= 95 and pecho_cm < 105:
        return "Mediana (M)"
    elif pecho_cm >= 105 and pecho_cm < 115:
        return "Grande (L)"
    else:
        return "Extra Grande (XL)"

# 2. Función para calcular la talla de abajo (Pantalones Cargo)
def calcular_talla_pantalon(cintura_cm):
    if cintura_cm < 76:
        return "Talla 28-30 (S)"
    elif cintura_cm >= 76 and cintura_cm < 86:
        return "Talla 32-34 (M)"
    elif cintura_cm >= 86 and cintura_cm < 96:
        return "Talla 36-38 (L)"
    else:
        return "Talla 40+ (XL)"

# 3. Pedimos los datos reales al cliente
pecho = float(input("Ingresa la circunferencia de tu pecho (en cm): "))
cintura = float(input("Ingresa la circunferencia de tu cintura (en cm): "))

# 4. Procesamos la información llamando a nuestras funciones
talla_arriba = calcular_talla_playera(pecho)
talla_abajo = calcular_talla_pantalon(cintura)

# 5. Entregamos el resultado final
print("\n--- Resultados de tu Fit ---")
print(f"👕 Playeras y Hoodies: Te recomendamos la talla {talla_arriba}")
print(f"👖 Pantalones Cargo: Te recomendamos la {talla_abajo}")
