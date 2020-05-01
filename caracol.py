a = [[1,2,3],
     [4,5,6],
     [7,8,9]]

r, c = 0, - 1 # posición renglón -> r; posición columna -> c
sig = 3 # Indica el borde de la matriz
x = 3 
y = 2 
deltaR, deltaC = 0, 1 # cambio en la posición por renglón y columna
giro = 0 # número de giro

for i in range(9): # rango de 0 hasta el número de elementos en la matriz
    c = c + deltaC
    r = r + deltaR
    print(a[r][c])

    if i == sig - 1: # Si llega al borde la matriz
        giro = giro + 1
        
        if giro % 2 == 0:   # Si giro es par, suma las columnas recorridas
            sig = sig + x
            y = y - 1
        else:               # Si giro es impar, suma los renglones recorridos
            sig = sig + y
            x = x - 1
        deltaC, deltaR = -deltaR, deltaC # intercambia el cambio por el opuesto aditivo