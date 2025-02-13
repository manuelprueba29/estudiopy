
matriz=[ 
        [1,1,0,1,0],
        [1,1,1,0,0,],
        [0,0,0,1,1,],
        [1,0,0,0,0],
        [1,1,0,0,0]
        ]

def recorrido(matriz, i, j):
    # Verificar si la posición está dentro de los límites y es un 1
    if i < 0 or i >= len(matriz) or j < 0 or j >= len(matriz[0]) or matriz[i][j] == 0:
        return

    # Marcar el nodo como visitado
    matriz[i][j] = 0

    # Visitar los 4 vecinos (arriba, abajo, izquierda, derecha)
    recorrido(matriz, i+1, j)  # Abajo
    recorrido(matriz, i-1, j)  # Arriba
    recorrido(matriz, i, j+1)  # Derecha
    recorrido(matriz, i, j-1)  # Izquierda

def contar_redes(matriz):
    conteo = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == 1:
                recorrido(matriz, i, j)
                conteo += 1  # Nueva red encontrada
    
    print(conteo)            
    return conteo

contar_redes(matriz)
    
