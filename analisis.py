import pandas as pd
from classes.estadisticos import *
from classes.graficos import *
import matplotlib.pyplot as plt

print("2 Por tipo de conversión (CALL o FORM), ¿Cuántas hay de cada una?")

conversiones= pd.read_csv("conversiones (4).csv")
navegacion = pd.read_csv("navegacion (4).csv")

#FILTRAMOS EL DATASET 

#SEPARAMOS LOS DATOS EN COLUMNAS

ts = navegacion["ts"]
uuid = navegacion["uuid"]
id_user = navegacion["id_user"]
user_recurrent = navegacion["user_recurrent"]
gclid = navegacion["gclid"]
url_landing = navegacion["url_landing"]

#EJERCICIO 2

tipodeconversiones = list(conversiones["lead_type"])

def contarCALL(lista):
    count = 0
    for elemento in lista:
        if elemento == "CALL":
            count += 1
    return count

print("El número de CALL: ", contarCALL(tipodeconversiones))
print("El numero de FORM: ", (len(tipodeconversiones)- contarCALL(tipodeconversiones)))

#conversiones.apply(conversiones["lead_type"]=="CALL")
