""" Programa Apoyo multas#
    incorpora al modulo multas.py
    Oscar Franco-Bedoya
    Mayo 3-2021 """

#---------------- Zona librerias------------
import multas as mult

#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================


#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación (Conquistar)
# =====================================================================
distancia_uno=float(input("Ingrese la primera distancia en metros:"))
distancia_dos=float(input("Ingrese la distacia dos en metros:"))
tiempo=float(input("Ingrese el tiempo en segundos:"))

multa_velocidad = mult.multar_velocidad(distancia_uno,distancia_dos,tiempo)
print("Multa de velocidad: ", multa_velocidad)

if multa_velocidad.find("Multa")>=0:
    grados_alcohol=float(input("\nIngrese los grados de alcohol en mg:"))
    multa_alcohol = mult.multar_alcoholemia(grados_alcohol)
    print("\nMulta de alcoholemia: ",multa_alcohol)
else:
    print("\nUsted no posee una multa de velocidad, por lo cual no se calcula su nivel de alcohol") 


