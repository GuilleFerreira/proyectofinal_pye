import pandas as pd
import statistics
import numpy as np
import scipy.stats as stats
from matplotlib import pyplot as plt

columns = ["ID", "anio", "mes","Sexo","Edad","region","PEA","Desempleo","Salario"]
encuesta = pd.read_csv("ECH_2022-BDProyectoFinalPyE2023.csv", usecols=columns)

def calculardesempleo():
    desempleados = encuesta.loc[encuesta['Desempleo'] == 1]
    pea = encuesta.loc[encuesta['PEA'] == 1]
    cantdes = desempleados.ID.count()
    cantpea = pea.ID.count()
    tasadesempleo = cantdes/cantpea
    print("Tasa de desempleo:", tasadesempleo)
    return

def graficodesempleo():
    # 14 A 17
    personas1 = encuesta.loc[encuesta['Edad'] >= 14]
    personas2 = personas1.loc[personas1['Edad'] <= 17]
    desempleados = personas2.loc[personas2['Desempleo'] == 1]
    pea = personas2.loc[personas2['PEA'] == 1]
    cantdes = desempleados.ID.count()
    cantpea = pea.ID.count()
    tasadesempleo14_17 = cantdes/cantpea
    
    # 18 A 25
    personas1 = encuesta.loc[encuesta['Edad'] >= 18]
    personas2 = personas1.loc[personas1['Edad'] <= 25]
    desempleados = personas2.loc[personas2['Desempleo'] == 1]
    pea = personas2.loc[personas2['PEA'] == 1]
    cantdes = desempleados.ID.count()
    cantpea = pea.ID.count()
    tasadesempleo18_25 = cantdes/cantpea
    
    # 26 A 40
    personas1 = encuesta.loc[encuesta['Edad'] >= 26]
    personas2 = personas1.loc[personas1['Edad'] <= 40]
    desempleados = personas2.loc[personas2['Desempleo'] == 1]
    pea = personas2.loc[personas2['PEA'] == 1]
    cantdes = desempleados.ID.count()
    cantpea = pea.ID.count()
    tasadesempleo26_40 = cantdes/cantpea
    
    # MAS DE 40
    personas = encuesta.loc[encuesta['Edad'] > 40]
    desempleados = personas.loc[personas['Desempleo'] == 1]
    pea = personas.loc[personas['PEA'] == 1]
    cantdes = desempleados.ID.count()
    cantpea = pea.ID.count()
    tasadesempleo40 = cantdes/cantpea
    
    courses = ['14 a 17', '18 a 25', '26 a 40', 'Mas de 40']
    values = [tasadesempleo14_17, tasadesempleo18_25, tasadesempleo26_40, tasadesempleo40] 
    fig = plt.figure(figsize = (10, 5)) 

    plt.bar(courses, values, color ='blue', width = 0.6)
    plt.xlabel("Rango de edad")
    plt.ylabel("Tasa de desempleo")
    plt.title("Tasa de desempleo por edad")
    plt.show()
    
    #print("Tasa de desempleo 14 a 17:", tasadesempleo14_17)
    #print("Tasa de desempleo 18 a 25:", tasadesempleo18_25)
    #print("Tasa de desempleo 26 a 40:", tasadesempleo26_40)
    #print("Tasa de desempleo mas de 40:", tasadesempleo40)
    return


def histogramasalarios():
    tempList1 = encuesta.loc[encuesta['Desempleo'] == 0]
    tempList2 = tempList1.loc[tempList1['PEA'] == 1]
    tempList3 = tempList2.loc[tempList2['Salario'] > 0]
    salarios = tempList3.Salario
    
    salarios1 = salarios.loc[salarios < 300000]
    salarios2 = salarios.loc[salarios >= 300000]

    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.suptitle('Histograma de salarios')
    ax1.hist(salarios1)
    ax1.set_title(f"Menores a $300000")
    
    ax2.hist(salarios2)
    ax2.set_title(f"Mayores a $300000")
    plt.show()
    return

def boxplotsalarios():
    tempList1 = encuesta.loc[encuesta['Desempleo'] == 0]
    tempList2 = tempList1.loc[tempList1['PEA'] == 1]
    tempList3 = tempList2.loc[tempList2['Salario'] > 0]
    salarios = tempList3.Salario
    plt.boxplot(salarios, whis=20)
    plt.title(f"Boxplot de salarios")
    plt.show()
    return

def mediamedianamoda():
    tempList1 = encuesta.loc[encuesta['Desempleo'] == 0]
    tempList2 = tempList1.loc[tempList1['PEA'] == 1]
    tempList3 = tempList2.loc[tempList2['Salario'] > 0]
    salarios = tempList3.Salario
    
    media = salarios.mean()
    mediana = statistics.median(salarios)
    moda = statistics.mode(salarios)

    print(f"Media de salarios: {media}")
    print(f"Mediana de salarios: {mediana}")
    print(f"Moda de salarios: {moda}")
    return

def minimomaximocuartiles():
    tempList1 = encuesta.loc[encuesta['Desempleo'] == 0]
    tempList2 = tempList1.loc[tempList1['PEA'] == 1]
    tempList3 = tempList2.loc[tempList2['Salario'] > 0]
    salarios = tempList3.Salario
    minimo = np.min(salarios)
    maximo = np.max(salarios)
    q1 = np.percentile(salarios, 25)
    q2 = np.percentile(salarios, 50)
    q3 = np.percentile(salarios, 75) 
    
    print(f"Mínimo de salarios: {minimo}")
    print(f"Máximo de salarios: {maximo}")
    print(f"Q1 de salarios: {q1}")
    print(f"Q2 de salarios: {q2}")
    print(f"Q3 de salarios: {q3}")
    return


def boxplotporgenero():
    tempList1 = encuesta.loc[encuesta['Desempleo'] == 0]
    salariosTemp = tempList1.loc[tempList1['PEA'] == 1]
    salarios = salariosTemp.loc[salariosTemp['Salario'] > 0]
    mujeres = salarios.loc[salarios['Sexo'] == 2]
    hombres = salarios.loc[salarios['Sexo'] == 1]
    
    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.suptitle('Salarios diferenciados por género')
    ax1.boxplot(mujeres.Salario, whis=20)
    ax1.set_title(f"Salario mujeres")
    
    ax2.boxplot(hombres.Salario, whis=20)
    ax2.set_title(f"Salario hombres")
    plt.show()
    return

def boxplotporzona():
    tempList1 = encuesta.loc[encuesta['Desempleo'] == 0]
    salariosTemp = tempList1.loc[tempList1['PEA'] == 1]
    salarios = salariosTemp.loc[salariosTemp['Salario'] > 0]
    interior = salarios.loc[salarios['region'] != 1]
    montevideo = salarios.loc[salarios['region'] == 1]
    
    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.suptitle('Salarios diferenciados por zona geográfica')
    ax1.boxplot(interior.Salario, whis=20)
    ax1.set_title(f"Salario interior")
    
    ax2.boxplot(montevideo.Salario, whis=20)
    ax2.set_title(f"Salario montevideo")
    plt.show()
    return


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

# ===========================================================
#                        MAIN PROGRAM
# ===========================================================

calculardesempleo()
graficodesempleo()
histogramasalarios()
boxplotsalarios()
mediamedianamoda()
minimomaximocuartiles()
boxplotporgenero()
boxplotporzona()

pruebaHipotesis1()
pruebaHipotesis2()