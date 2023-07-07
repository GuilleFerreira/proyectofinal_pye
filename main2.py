import pandas as pd
import statistics
import numpy as np
import scipy.stats as stats
from matplotlib import pyplot as plt

columns = ["ID", "anio", "mes","Sexo","Edad","region","PEA","Desempleo","Salario"]
encuesta = pd.read_csv("ECH_2022-BDProyectoFinalPyE2023.csv", usecols=columns)


def pruebaHipotesis1():
    desempleados = encuesta.loc[encuesta['Desempleo'] == 1]
    pea = encuesta.loc[encuesta['PEA'] == 1]
    cantdes = desempleados.ID.count()
    cantpea = pea.ID.count()
    tasadesempleo2022 = cantdes / cantpea

    # Prueba de hipótesis de una muestra
    tasaDesempleo2021 = 0.07  # Tasa de desempleo en 2021 (hipótesis nula)

    if tasadesempleo2022 < tasaDesempleo2021:
        print("Se rechaza la hipótesis nula.")
    else:
        print("No se rechaza la hipótesis nula.")

    return




def pruebaHipotesis2():
    tempList1 = encuesta.loc[encuesta['Desempleo'] == 0]
    salariosTemp = tempList1.loc[tempList1['PEA'] == 1]
    salarios = salariosTemp.loc[salariosTemp['Salario'] > 0]
    mujeres = salarios.loc[salarios['Sexo'] == 2]
    hombres = salarios.loc[salarios['Sexo'] == 1]
    
    # Realizar la prueba estadística (t-test) para muestras independientes (dos colas)
    t_statistic, p_value = stats.ttest_ind(hombres.Salario, mujeres.Salario)

    # Definir el nivel de significancia
    nivel_significancia = 0.01

    # Comparar el valor p con el nivel de significancia
    if p_value < nivel_significancia:
        print("Se rechaza la hipótesis nula, hay diferencias significativas en el salario promedio entre los grupos según el género.")
    else:
        print("No se rechaza la hipótesis nula, no hay diferencias significativas en el salario promedio entre los grupos según el género.")

    return


pruebaHipotesis1()