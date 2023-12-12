import turtle
class dibujar_estrella:
    def __init__(self, puntas, Lado):
        self.puntas = puntas
        self.Lado = Lado

    def Estrella(puntas, lado):
        ''' Función que dibuja una estrella regular de un número de puntas dado haciendo uso del módulo Turtle.

        Parámetros:
        puntas: Es un entero con el número de puntas de la estrella.
        lado: Es un entero con el tamaño de los lados de la estrella.
        '''

        # Función para calcular el máximo común divisor de dos números enteros por el algoritmo de euclides. Se necesita para calcular el ángulo de rotación.
        def MCD(a, b):
        
            while b != 0:
                a, b = b, a % b
            return a

        if puntas <= 4:
        # Condicional para avisar de que el número de puntas debe ser mayor que 4. Si no no es posible dibujar la estrella.

            print('El número de puntas es demasiado pequeño. Prueba de nuevo con un número de puntas mayor.')
            return 
        # El ángulo de rotación en los vértices de la estrella se calcula en fución del primer número entero coprimo con el número de puntas
        # Bucle iterarivo para buscar el mayor coprimo con el número de puntas
        for i in range(puntas // 2, 1, -1):
            # Condicional para ver si i y el número de puntas son números coprimos(tienen solo 2,1,-2 en comun)
            if MCD(puntas, i) == 1:
                angle = 360.0 / puntas * i
                break
        # Bucle iterativo para dibujar los trazos de cada punta.
        for _ in range(puntas):
            # Dibujamos el lado
            turtle.forward(lado)
            # Rotamos el cursor
            turtle.left(angle)

        return
    puntas = int(input("¿de cuantas puntas quieres la estrella?"))

    Estrella(puntas,200)