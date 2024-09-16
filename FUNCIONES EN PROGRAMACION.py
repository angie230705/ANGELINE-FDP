import numpy as np


def calcular_temperatura_promedio(datos_temperatura):
    """
    Calcula la temperatura promedio de cada ciudad durante el período dado.

    :param datos_temperatura: Lista de listas de listas que contiene las temperaturas
                              por ciudad, semana y día, en formato numpy array.
    :return: Lista de promedios de temperatura para cada ciudad.
    """
    promedios_ciudades = []

    # Iterar sobre cada ciudad en los datos
    for ciudad in datos_temperatura:
        # Convertir la lista de semanas en un array de NumPy
        ciudad_array = np.array(ciudad)

        # Calcular la temperatura promedio para la ciudad
        promedio_ciudad = np.mean(ciudad_array)

        # Añadir el resultado a la lista de promedios
        promedios_ciudades.append(promedio_ciudad)

    return promedios_ciudades


# Ejemplo de uso
# Definir los datos de ejemplo (utilizando datos ficticios)
horas_por_día = 24
temperaturas_dia = {
    "lunes": 20,
    "martes": 21,
    "miércoles": 19,
    "jueves": 22,
    "viernes": 20,
    "sábado": 18,
    "domingo": 17
}

# Crear datos de temperatura para varias ciudades
datos_temperatura = [
    # Ciudad A
    [
        # Semana 1
        [
            np.full(horas_por_día, temperaturas_dia["lunes"]),
            np.full(horas_por_día, temperaturas_dia["martes"]),
            np.full(horas_por_día, temperaturas_dia["miércoles"]),
            np.full(horas_por_día, temperaturas_dia["jueves"]),
            np.full(horas_por_día, temperaturas_dia["viernes"]),
            np.full(horas_por_día, temperaturas_dia["sábado"]),
            np.full(horas_por_día, temperaturas_dia["domingo"])
        ],
        # Semana 2
        [
            np.full(horas_por_día, temperaturas_dia["lunes"]),
            np.full(horas_por_día, temperaturas_dia["martes"]),
            np.full(horas_por_día, temperaturas_dia["miércoles"]),
            np.full(horas_por_día, temperaturas_dia["jueves"]),
            np.full(horas_por_día, temperaturas_dia["viernes"]),
            np.full(horas_por_día, temperaturas_dia["sábado"]),
            np.full(horas_por_día, temperaturas_dia["domingo"])
        ]
    ],
    # Ciudad B
    [
        # Semana 1
        [
            np.full(horas_por_día, temperaturas_dia["lunes"]),
            np.full(horas_por_día, temperaturas_dia["martes"]),
            np.full(horas_por_día, temperaturas_dia["miércoles"]),
            np.full(horas_por_día, temperaturas_dia["jueves"]),
            np.full(horas_por_día, temperaturas_dia["viernes"]),
            np.full(horas_por_día, temperaturas_dia["sábado"]),
            np.full(horas_por_día, temperaturas_dia["domingo"])
        ],
        # Semana 2
        [
            np.full(horas_por_día, temperaturas_dia["lunes"]),
            np.full(horas_por_día, temperaturas_dia["martes"]),
            np.full(horas_por_día, temperaturas_dia["miércoles"]),
            np.full(horas_por_día, temperaturas_dia["jueves"]),
            np.full(horas_por_día, temperaturas_dia["viernes"]),
            np.full(horas_por_día, temperaturas_dia["sábado"]),
            np.full(horas_por_día, temperaturas_dia["domingo"])
        ]
    ],
    # Ciudad C
    [
        # Semana 1
        [
            np.full(horas_por_día, temperaturas_dia["lunes"]),
            np.full(horas_por_día, temperaturas_dia["martes"]),
            np.full(horas_por_día, temperaturas_dia["miércoles"]),
            np.full(horas_por_día, temperaturas_dia["jueves"]),
            np.full(horas_por_día, temperaturas_dia["viernes"]),
            np.full(horas_por_día, temperaturas_dia["sábado"]),
            np.full(horas_por_día, temperaturas_dia["domingo"])
        ],
        # Semana 2
        [
            np.full(horas_por_día, temperaturas_dia["lunes"]),
            np.full(horas_por_día, temperaturas_dia["martes"]),
            np.full(horas_por_día, temperaturas_dia["miércoles"]),
            np.full(horas_por_día, temperaturas_dia["jueves"]),
            np.full(horas_por_día, temperaturas_dia["viernes"]),
            np.full(horas_por_día, temperaturas_dia["sábado"]),
            np.full(horas_por_día, temperaturas_dia["domingo"])
        ]
    ]
]

# Calcular y mostrar los promedios de temperatura
promedios = calcular_temperatura_promedio(datos_temperatura)
print("Temperatura promedio por ciudad:", promedios)