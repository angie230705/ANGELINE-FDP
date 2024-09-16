# Crear una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades (3 ciudades)
# Segunda dimensión: Días de la semana (7 días)
# Tercera dimensión: Semanas (4 semanas)
temperaturas = [
    [   # Orellana
        [   # Semana 1
            {"day": "Lunes", "temp": 35},
            {"day": "Martes", "temp": 38},
            {"day": "Miércoles", "temp": 42},
            {"day": "Jueves", "temp": 41},
            {"day": "Viernes", "temp": 40},
            {"day": "Sábado", "temp": 32},
            {"day": "Domingo", "temp": 8}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 35},
            {"day": "Martes", "temp": 48},
            {"day": "Miércoles", "temp": 42},
            {"day": "Jueves", "temp": 35},
            {"day": "Viernes", "temp": 39},
            {"day": "Sábado", "temp": 42},
            {"day": "Domingo", "temp": 42}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 42},
            {"day": "Martes", "temp": 37},
            {"day": "Miércoles", "temp": 38},
            {"day": "Jueves", "temp": 38},
            {"day": "Viernes", "temp": 35},
            {"day": "Sábado", "temp": 33},
            {"day": "Domingo", "temp": 38}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 42},
            {"day": "Martes", "temp": 38},
            {"day": "Miércoles", "temp": 35},
            {"day": "Jueves", "temp": 32},
            {"day": "Viernes", "temp": 38},
            {"day": "Sábado", "temp": 40},
            {"day": "Domingo", "temp": 40}
        ]
    ],
    [   # Shushufindi
        [   # Semana 1
            {"day": "Lunes", "temp": 34},
            {"day": "Martes", "temp": 37},
            {"day": "Miércoles", "temp": 40},
            {"day": "Jueves", "temp": 38},
            {"day": "Viernes", "temp": 37},
            {"day": "Sábado", "temp": 38},
            {"day": "Domingo", "temp": 40}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 37},
            {"day": "Martes", "temp": 38},
            {"day": "Miércoles", "temp": 39},
            {"day": "Jueves", "temp": 40},
            {"day": "Viernes", "temp": 41},
            {"day": "Sábado", "temp": 42},
            {"day": "Domingo", "temp": 40}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 40},
            {"day": "Martes", "temp": 38},
            {"day": "Miércoles", "temp": 34},
            {"day": "Jueves", "temp": 32},
            {"day": "Viernes", "temp": 38},
            {"day": "Sábado", "temp": 38},
            {"day": "Domingo", "temp": 37}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 40},
            {"day": "Martes", "temp": 41},
            {"day": "Miércoles", "temp": 37},
            {"day": "Jueves", "temp": 38},
            {"day": "Viernes", "temp": 38},
            {"day": "Sábado", "temp": 40},
            {"day": "Domingo", "temp": 38}
        ]
    ],
    [   # Esmeralda
        [   # Semana 1
            {"day": "Lunes", "temp": 42},
            {"day": "Martes", "temp": 43},
            {"day": "Miércoles", "temp": 40},
            {"day": "Jueves", "temp": 38},
            {"day": "Viernes", "temp": 38},
            {"day": "Sábado", "temp": 39},
            {"day": "Domingo", "temp": 38}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 41},
            {"day": "Martes", "temp": 42},
            {"day": "Miércoles", "temp": 38},
            {"day": "Jueves", "temp": 38},
            {"day": "Viernes", "temp": 37},
            {"day": "Sábado", "temp": 38},
            {"day": "Domingo", "temp": 38}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 41},
            {"day": "Martes", "temp": 41},
            {"day": "Miércoles", "temp": 37},
            {"day": "Jueves", "temp": 39},
            {"day": "Viernes", "temp": 41},
            {"day": "Sábado", "temp": 40},
            {"day": "Domingo", "temp": 37}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 38},
            {"day": "Martes", "temp": 41},
            {"day": "Miércoles", "temp": 42},
            {"day": "Jueves", "temp": 38},
            {"day": "Viernes", "temp": 41},
            {"day": "Sábado", "temp": 40},
            {"day": "Domingo", "temp": 37}
        ]
    ]
]


# Calcular el promedio de temperaturas para cada ciudad y semana
ciudades = ["Ciudad 1", "Ciudad 2", "Ciudad 3"]
for ciudad_idx, ciudad in enumerate(temperaturas):
    for semana_idx, semana in enumerate(ciudad):
        suma_temperaturas = sum([dia["temp"] for dia in semana])
        promedio = suma_temperaturas / len(semana)
        print(f"Promedio de temperaturas en {ciudades[ciudad_idx]}, Semana {semana_idx + 1}: {promedio:.2f} grados")