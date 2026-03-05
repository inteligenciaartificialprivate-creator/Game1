"""Juego de química básica en consola.

Reglas:
- Se juegan 5 rondas.
- En cada ronda se elige un elemento químico al azar.
- El jugador debe indicar protones, electrones y neutrones.
- Se obtiene +1 punto si las tres respuestas de la ronda son correctas.
"""

from __future__ import annotations

import random


# Lista interna de elementos químicos (nombre, número atómico Z, número de masa A).
ELEMENTOS = [
    {"nombre": "Hidrógeno", "Z": 1, "A": 1},
    {"nombre": "Helio", "Z": 2, "A": 4},
    {"nombre": "Litio", "Z": 3, "A": 7},
    {"nombre": "Berilio", "Z": 4, "A": 9},
    {"nombre": "Boro", "Z": 5, "A": 11},
    {"nombre": "Carbono", "Z": 6, "A": 12},
    {"nombre": "Nitrógeno", "Z": 7, "A": 14},
    {"nombre": "Oxígeno", "Z": 8, "A": 16},
    {"nombre": "Flúor", "Z": 9, "A": 19},
    {"nombre": "Neón", "Z": 10, "A": 20},
    {"nombre": "Sodio", "Z": 11, "A": 23},
    {"nombre": "Magnesio", "Z": 12, "A": 24},
    {"nombre": "Aluminio", "Z": 13, "A": 27},
    {"nombre": "Silicio", "Z": 14, "A": 28},
    {"nombre": "Fósforo", "Z": 15, "A": 31},
]


def pedir_entero(mensaje: str) -> int:
    """Solicita un número entero al usuario y valida la entrada."""
    while True:
        entrada = input(mensaje).strip()
        try:
            return int(entrada)
        except ValueError:
            print("Entrada inválida. Debes ingresar un número entero.")


def jugar_ronda(numero_ronda: int) -> bool:
    """Ejecuta una ronda y devuelve True si todo fue correcto, en caso contrario False."""
    elemento = random.choice(ELEMENTOS)

    nombre = elemento["nombre"]
    z = elemento["Z"]
    a = elemento["A"]

    print(f"\n--- Ronda {numero_ronda} ---")
    print(f"Elemento: {nombre}")
    print(f"Número atómico (Z): {z}")
    print(f"Número de masa (A): {a}")

    protones_usuario = pedir_entero("Ingresa la cantidad de protones: ")
    electrones_usuario = pedir_entero("Ingresa la cantidad de electrones: ")
    neutrones_usuario = pedir_entero("Ingresa la cantidad de neutrones: ")

    protones_correctos = z
    electrones_correctos = z
    neutrones_correctos = a - z

    acierto_total = (
        protones_usuario == protones_correctos
        and electrones_usuario == electrones_correctos
        and neutrones_usuario == neutrones_correctos
    )

    if acierto_total:
        print("✅ ¡Correcto! Ganaste 1 punto en esta ronda.")
    else:
        print("❌ Respuesta incorrecta.")
        print("Respuestas correctas:")
        print(f"- Protones: {protones_correctos}")
        print(f"- Electrones: {electrones_correctos}")
        print(f"- Neutrones: {neutrones_correctos}")

    return acierto_total


def main() -> None:
    """Función principal del juego."""
    print("=== Juego de Química Básica ===")
    print("Debes responder protones, electrones y neutrones de cada elemento.")
    print("Reglas: Protones = Z, Electrones = Z, Neutrones = A - Z")

    puntaje = 0
    total_rondas = 5

    for ronda in range(1, total_rondas + 1):
        if jugar_ronda(ronda):
            puntaje += 1

    print("\n=== Fin del juego ===")
    print(f"Puntaje final: {puntaje}/{total_rondas}")


if __name__ == "__main__":
    main()
