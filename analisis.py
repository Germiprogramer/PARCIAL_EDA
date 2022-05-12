import pandas as pd
from classes.estadisticos import *
from classes.graficos import *
import matplotlib.pyplot as plt


conversiones= pd.read_csv("conversiones.csv")
navegacion = pd.read_csv("navegacion.csv")


#FILTRAMOS EL DATASET 

#SEPARAMOS LOS DATOS EN COLUMNAS

ts = navegacion["ts"]
uuid = navegacion["uuid"]
id_user = navegacion["id_user"]
user_recurrent = navegacion["user_recurrent"]
gclid = navegacion["gclid"]
url_landing = navegacion["url_landing"]

#SEPARACION URL

list = list(navegacion["url_landing"])

for i in range(len(list)): 
    list[i].split("gclid")

    #no me ha dado tiempo a acabarla

#EJERCICIO 1

print("Conversiones que recibe al día el cliente: ")

filas_conv = Filas(conversiones)
filas_conv.calculo()

filas_nav = Filas(navegacion)
filas_nav.calculo()

print(conversiones.shape(0)/navegacion.shape(0))



#EJERCICIO 2


print("2 Por tipo de conversión (CALL o FORM), ¿Cuántas hay de cada una?")
tipodeconversiones = list(conversiones["lead_type"])

def contarCALL(lista):
    
    for i in range(len(lista)):
        if lista[i] == "CALL":
            count += 1
    return count

print("El número de CALL: ", contarCALL(tipodeconversiones))
print("El numero de FORM: ", (len(tipodeconversiones)- contarCALL(tipodeconversiones)))

grafico(conversiones["lead_type"], "pie", "conversiones", "tipoconversiones")

#EJERCICIO 3

print("Porcentaje de usuarios recurrentes sobre el total de usuarios: ")

recurrentes = navegacion.drop(navegacion[navegacion['user_recurrent']=="true"].index)

porcentaje_recurrentes = recurrentes.shape[0]/navegacion.shape[0]

print("el pocentaje de usuarios recurrentes es: {}".format(porcentaje_recurrentes))

#EJERCICIO 4