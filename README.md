# PARCIAL_EDA

el link al repositio es el siguiente : https://github.com/Germiprogramer/PARCIAL_EDA.git

# Cuántas visitas recibe en el día el cliente y de estas,   cuántas de ellas convierten y cuántas no (en %)

Para responder a esta pregunta, se ha calculado el numero de navegaciones y el numero de conversiones. Diviendo el numero de conversiones entre el de navegaciones, podemos hallar el porcentaje de conversiones.

# Por tipo de conversión (CALL o FORM), ¿Cuántas hay de cada una?

Se ha realizado una lista con los elementos de la columna del dataframe "lead_type". A partir de ahí, se ha realizado una función para ver cuales cumplen la condición CALL. Si restamos al total el número de CALL, obtenemos el número de FORM.

# Porcentaje de usuarios recurrentes sobre el total de usuarios

Utilizando la funcion drop de pandas, se ha creado un nuevo dataset incluyendo tan solo los usuarios recurrentes. Comparando las longitudes del dataset original con el nuevo, hemos podido hallar el porcentaje.

# Coche más visitado. ¿Es el que más convierte?
