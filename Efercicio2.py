NS = [9, 5, 4, 8, 7, 6, 3, 2, 1, 9, 5, 7, 8, 5, 2, 1, 9]
vlr_a_contar = 9
cont = 0 
for N in NS: 
    if N == vlr_a_contar: 
        cont += 1 
        
print(f"El numero {vlr_a_contar} aparece {cont} veces en el arreglo.")