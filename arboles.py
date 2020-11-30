
import csv



def leer_arboles(nombre_archivo):
    arboleda = [] 


    with open(nombre_archivo, 'rt', encoding='utf8') as f:#encoding para que lea el archivo
        filas = csv.reader(f)
        encabezados=next(filas)
        for n_fila,filas in enumerate(filas, start=1):#n_filas no lo uso
            record = dict(zip(encabezados,filas))#armo un diccionario con encabezados y filas
            arboleda.append(record)

    # H=[(float(arbol['diametro']),float(arbol['altura_tot'])) for arbol in arboleda if arbol['nombre_com']=='Jacarandá' ]
    
    # print(H)

    return arboleda


def altos_jacarandas(nombre_archivo): 
    arboleda=leer_arboles(nombre_archivo)
   
    G=[float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com']=='Jacarandá' ]
    H=[(float(arbol['diametro']),float(arbol['altura_tot'])) for arbol in arboleda if arbol['nombre_com']=='Jacarandá' ]

    print(G)    



def altos_y_diametros(nombre_archivo): 

    arboleda=leer_arboles(nombre_archivo)
    H=[(float(arbol['diametro']),float(arbol['altura_tot'])) for arbol in arboleda if arbol['nombre_com']=='Jacarandá' ]

    print(H)    
   
