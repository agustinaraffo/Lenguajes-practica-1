import csv 
import json
from datetime import datetime
import os

dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
dias_mas_entrenamiento = {} #3
lista_fechas = [] #4
campeon_entrenamientos = {} #diccionario para el 5(campeon que más entrenó)
entrenamientos_finde = {} #7 para el campeon que mas entrena los fines de semana
total_registros = 0
entrenamientos_por_dia = {} #diccionario para el json

#1 LEER EL ARCHIVO:
with open(r"C:\Users\agusr\Practica2 lenguajes\actividad_2.csv.csv", "r", encoding="utf-8") as f:   

    reader = csv.DictReader(f)

    #2 IDENTIFICAR EL DIA DE LA SEMANA DE CADA ENTRENAMIENTO
    for fila in reader:
        fecha = datetime.strptime(fila["timestamp"], "%Y-%m-%d %H:%M")
        dia = dias[fecha.weekday()]
        total_registros += 1
        print(f"El entrenamiento del {fila['timestamp']} fue un {dia}.")


        #3 CALCULAR DIA CON MAS ENTRENAMIENTOS
        if dia in dias_mas_entrenamiento:
            dias_mas_entrenamiento[dia] += 1
        else:
            dias_mas_entrenamiento[dia] = 1
    
        #4 CUANTOS DIAS PASARON DEL PRIMER AL ULTIMO ENTRENAMIENTO
        lista_fechas.append(fecha.date())

        #5 MOSTRAR EL CAMPEON QUE MAS ENTRENO
        campeon = fila["campeon"]
        if campeon in campeon_entrenamientos:
            campeon_entrenamientos[campeon] += 1
        else:
            campeon_entrenamientos[campeon] = 1
 
        #7 CAMPEON QUE MAS ENTRENA LOS FINES DE SEMANA
        campeon = fila["campeon"]

        if dia == "Sabado" or dia == "Domingo":
            if campeon in entrenamientos_finde:
                entrenamientos_finde[campeon] += 1
            else:
                entrenamientos_finde[campeon] = 1

        #8 JSON 
        if dia not in entrenamientos_por_dia:
            entrenamientos_por_dia[dia] = {}
        if campeon in entrenamientos_por_dia[dia]:
            entrenamientos_por_dia[dia][campeon] += 1
        else:
            entrenamientos_por_dia[dia][campeon] = 1

#Continuacion3 convierto a lista y ordeno de mayor a menor
lista_dias = list(dias_mas_entrenamiento.items())
ordenado = sorted(lista_dias, key=lambda x: x[1], reverse=True)

dia_mas = ordenado[0]

print (f"El dia con mas entrenamientos es {dia_mas}")


#Continuacion4 
#Ordeno la lista de fechas
lista_fechas.sort()

#Tomo la primera posicion y la ultima (primer y ultimo dia)
primer_dia = lista_fechas[0]
ultimo_dia = lista_fechas[-1]

#Calculo la cantidad de dias entre ambos
contador_dias = (ultimo_dia - primer_dia).days
print (f"Pasaron {contador_dias} dias entre el primer y ultimo dia de entrenamiento, el primer dia fue: {primer_dia} y el ultimo fue {ultimo_dia}")

#Continuacion5
#ordeno de mayor a menor por cantidad de dias de entrenamiento
ranking_campeones = sorted(campeon_entrenamientos.items(), key=lambda x: x[1], reverse=True)
campeon_mas_entreno = ranking_campeones[0]

print (f"El campeon que mas entrenó fue: {campeon_mas_entreno}")

#6PROMEDIO DE ENTRENAMIENTOS POR CADA DIA DE LA SEMANA

# calculo la cantidad total de dias del rango
dias_totales = (ultimo_dia - primer_dia).days  

# cantidad de semanas aproximada
cantidad_semanas = dias_totales / 7

print("El promedio de entrenamientos cada dia de la semana es:")

for dia, cantidad in dias_mas_entrenamiento.items():
    promedio = cantidad / cantidad_semanas
    print(f"Para el dia {dia}: {promedio:.2f} entrenamientos por semana")


#Continuacion7
#ordeno de mayor a menor 
mayor_findes = sorted(entrenamientos_finde.items(), key=lambda x: x[1], reverse=True)

# el primero es el que más entrenó
campeon_mayor_findes = mayor_findes[0]
print(f"El que más entreno los fines de semana es {campeon_mayor_findes}")


#8 CREAR ARCHIVO CSV CON CANTIDAD DE ENTRENAMIENTOS POR CAMPEON

# creo la carpeta salida si no existe
os.makedirs("salida", exist_ok=True)

# creo el archivo en esa carpeta
with open("salida/entrenamientos_por_campeon.csv", "w", newline="", encoding="utf-8") as salida_csv:
    writer = csv.writer(salida_csv)
        
    # se escribe el campeon con cantidad de entrenamientos
    for campeon, cantidad in campeon_entrenamientos.items(): 
        writer.writerow([campeon, cantidad])


#9 CREAR JSON CON TOTAL DE REGISTROS Y PARA CADA DIA LOS CAMPEONES Y CUANTAS VECES ENTRENARON
datos_json = {
    "total_registros": total_registros,
    "por_dia": entrenamientos_por_dia
}

with open("salida/resumen_entrenamientos.json", "w", encoding="utf-8") as jf:
    json.dump(datos_json, jf)

