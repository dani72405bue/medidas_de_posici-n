"""
Programa interactivo para medidas de posición: cuartiles, deciles y percentiles.

Características:
- Pide al usuario cuántos datos quiere introducir (mínimo 20).
- Calcula la posición p = k*(n+1)/m (m = 4, 10, 100 según cuartil/decil/percentil).
- Muestra la posición y el valor correspondiente. Regla especial:
- Si la posición p es un entero y ese índice (1-based) es par, se promedia
	el dato en esa posición con el siguiente (tal como pediste).
- Si la posición no es entera, se interpola linealmente entre piso y techo.

Uso: ejecutar el script y seguir las indicaciones.
"""

from math import floor, ceil


def leer_numero(prompt):
	while True:
		s = input(prompt).strip()
		try:
			return float(s)
		except ValueError:
			print("Entrada no válida. Introduce un número válido.")


def solicitar_datos():
	print("Programa de medidas de posición (cuartiles, deciles, percentiles)")
	while True:
		try:
			n = int(input("¿Cuántos datos vas a introducir? (mínimo 20): ").strip())
			if n < 20:
				print("Debes introducir al menos 20 datos.")
				continue
			break
		except ValueError:
			print("Introduce un entero válido.")

	datos = []
	print("Introduce los datos numéricos uno por uno (puedes usar decimales).")
	i = 1
	while len(datos) < n:
		try:
			v = input(f"Dato {i}: ").strip()
			num = float(v)
			datos.append(num)
			i += 1
		except ValueError:
			print("Entrada no válida. Intenta de nuevo.")

	datos.sort()
	return datos


def posicion(k, m, n):
	"""Calcula la posición p = k*(n+1)/m (1-based)."""
	return (k * (n + 1)) / m


def valor_en_posicion(datos, p):
	"""
	Devuelve el valor correspondiente a la posición p (1-based) en lista ordenada `datos`.

	Reglas:
	- Si p es entero y el índice es par, devuelve el promedio del elemento en p y el siguiente.
	- Si p es entero y el índice es impar, devuelve el elemento en p.
	- Si p no es entero, hace interpolación lineal entre floor(p) y ceil(p).
	"""
	n = len(datos)
	if p <= 1:
		return datos[0]
	if p >= n:
		return datos[-1]

	if abs(p - round(p)) < 1e-12:  # p entero
		idx = int(round(p))  # 1-based
		if idx < n and idx % 2 == 0:
			# índice par -> promedio con siguiente (regla del usuario)
			a = datos[idx - 1]
			b = datos[idx]
			return (a + b) / 2.0
		else:
			return datos[idx - 1]
	else:
		f = floor(p)
		c = ceil(p)
		# manejar límites
		if f < 1:
			return datos[0]
		if c > n:
			return datos[-1]
		frac = p - f
		a = datos[f - 1]
		b = datos[c - 1]
		return a + frac * (b - a)


def mostrar_resultado(tipo, k, datos):
	n = len(datos)
	m = {'C': 4, 'D': 10, 'P': 100}[tipo]
	p = posicion(k, m, n)
	val = valor_en_posicion(datos, p)
	print(f"\nResultado para {'Cuartil' if tipo=='C' else 'Decil' if tipo=='D' else 'Percentil'} {k}:")
	print(f"- Posición p = {p:.4f} (fórmula k*(n+1)/m, con n={n} y m={m})")
	if abs(p - round(p)) < 1e-12 and int(round(p)) % 2 == 0 and int(round(p)) < n:
		print("- Observación: p es entero y par -> se promedia con el siguiente valor (regla aplicada).")
	elif abs(p - round(p)) < 1e-12:
		print("- Observación: p es entero -> se toma el valor en esa posición.")
	else:
		print("- Observación: p no es entero -> se interpola entre los valores vecinos.")
	print(f"- Valor obtenido: {val}")


def menu_interactivo(datos):
	while True:
		print("\nSelecciona una opción:")
		print("  1) Calcular un Cuartil (Q)")
		print("  2) Calcular un Decil (D)")
		print("  3) Calcular un Percentil (P)")
		print("  4) Mostrar todos los Cuartiles (Q1,Q2,Q3)")
		print("  5) Salir")
		opc = input("Opción: ").strip()
		if opc == '1':
			k = int(input("¿Qué cuartil? (1..3): ").strip())
			if k < 1 or k > 3:
				print("Cuartil inválido.")
				continue
			mostrar_resultado('C', k, datos)
		elif opc == '2':
			k = int(input("¿Qué decil? (1..9): ").strip())
			if k < 1 or k > 9:
				print("Decil inválido.")
				continue
			mostrar_resultado('D', k, datos)
		elif opc == '3':
			k = int(input("¿Qué percentil? (1..99): ").strip())
			if k < 1 or k > 99:
				print("Percentil inválido.")
				continue
			mostrar_resultado('P', k, datos)
		elif opc == '4':
			for k in (1, 2, 3):
				mostrar_resultado('C', k, datos)
		elif opc == '5':
			print("Saliendo.")
			break
		else:
			print("Opción no válida. Intenta de nuevo.")


def main():
	datos = solicitar_datos()
	print(f"\nHas introducido {len(datos)} datos. Lista ordenada:")
	print(datos)
	menu_interactivo(datos)


if __name__ == '__main__':
	main()

