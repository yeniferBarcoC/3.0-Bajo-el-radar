""" Modulo Multas
    Funciones para el cálculo de multas
    de tránsito 
    Yenifer Barco Castrillón
    Mayo 10-2021 """
# Definición de Funciones
#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================
def multar_velocidad(distancia_uno, distancia_dos,tiempo):
    """ 
    Parameters
    ----------
    distancia_uno:float
        distacia uno para calcular la velocidad en metros
    distancia_dos:float
        segunda distancia para calcular la velocidad en metros
    tiempo:float
        tiempo dado por el ususario en segundos
    Returns
    -------
    texto_multa:string
        enunciado de la multa de velocidad
    """ 
    # conversion de metros a Kilometros
    dist_km_uno = distancia_uno/100
    dist_km_dos = distancia_dos/100

    #Conversion de segundos a horas
    tiempo_horas = tiempo/3600

    #Calcular espacio
    espacio = dist_km_dos - dist_km_uno

    #Calcular velocidad
    velocidad = espacio/tiempo_horas
    print("\nVelocidad actal: ",velocidad)
    if velocidad>=1 and velocidad<=20:
        texto_multa="Llamada de atención por baja velocidad"
    elif velocidad>=21 and velocidad<=60:
        texto_multa="Normal"
    elif velocidad>=61 and velocidad<=80:
        texto_multa="Llamado de atención por alta velocidad"
    elif velocidad>=81 and velocidad<=120:
        texto_multa="Multa tipo I"
    elif velocidad>120:
        texto_multa="Multa tipo II e inmovilización de vehículo"
    else:
        texto_multa="Por favor ingrese un valor valido"

    return texto_multa

def multar_alcoholemia(grado_alcohol):
    """ 
    Parameters
    ----------
    grado_alcohol:float
        grados de alcohol para verificar si esta en estado de embriagues en miligramos
    Returns
    -------
    texto_multa:string
        enunciado de la multa de alcoholemia
    """ 
    if grado_alcohol>0:
        if grado_alcohol>=20 and grado_alcohol<=39:
            texto_multa="Además de las sanciones previstas en la presente ley, se decretará la suspensión de la licencia de conducción entre seis (6) y doce (12) meses."
        elif grado_alcohol>=40 and grado_alcohol<=99:
            texto_multa="Primer grado de embriaguez: se decretará la suspensión de la Licencia de Conducción entre uno (1) y tres (3) años."
        elif grado_alcohol>=100 and grado_alcohol<=149:
            texto_multa="Segundo grado de embriaguez: se decretará la suspensión de la Licencia de Conducción entre tres (3) y cinco (5) años, y la obligación de realizar curso de sensibilización, conocimientos y consecuencias de la alcoholemia y drogadicción en centros de rehabilitación debidamente autorizados, por un mínimo de cuarenta (40) horas."
        elif grado_alcohol>=150:
            texto_multa="Tercer grado de embriaguez: se decretará la suspensión entre cinco (5) y diez (10) años de la Licencia de Conducción, y la obligación de realizar curso de sensibilización, conocimientos y consecuencias de la alcoholemia y drogadicción en centros de rehabilitación debidamente autorizados, por un mínimo de ochenta (80) horas."
        else:
            texto_multa="Su nivel de alcoholemia esta dentro de los niveles permitidos la cual no le acarrea una multa."
    else:
        texto_multa="Ingrese un valor mayor a cero para los grados de alcoholemia"

    return texto_multa


