import pandas as pd 
import numpy as np
from scipy import stats
import time

#Ejercicio 1
demanda_df_2019_1 = pd.read_excel("datos/Demanda_Comercial_Por_Comercializador_SEME1_2019.xlsx")
demanda_df_2019_2 = pd.read_excel("datos/Demanda_Comercial_Por_Comercializador_SEME2_2019.xlsx")
demanda_df_2020_1 = pd.read_excel("datos/Demanda_Comercial_Por_Comercializador_SEME1_2020.xlsx")
demanda_df_2020_2 = pd.read_excel("datos/Demanda_Comercial_Por_Comercializador_SEME2_2020.xlsx")

demanda_df = pd.concat([demanda_df_2019_1, demanda_df_2019_2, demanda_df_2020_1, demanda_df_2020_2])
#demanda_df = demanda_df_2019_1
# print(len(demanda_df.index))
# print(demanda_df.head())

demanda_df['demanda_dia'] = demanda_df.loc[:,'H0':'H23'].sum(axis=1)
# print(demanda_df.head())

new_df = pd.pivot_table(demanda_df, values="demanda_dia", index=["Fecha", "tipo_mercado"], columns=["codigo_comercializador"]).reset_index()
# print(new_df.head())

new_df.to_excel("output/respuesta_punto1.xlsx")


#Ejercicio 2
demanda_diaria_df = demanda_df.groupby(['Fecha', 'codigo_comercializador'])['demanda_dia'].agg(demanda_dia='sum').reset_index()
# print(demanda_diaria_df.head())

resumen_demanda_df = demanda_diaria_df.groupby(['codigo_comercializador'])['demanda_dia'].agg(promedio='mean', mediana='median', minimo='min', maximo='max', desviacion_estandar='std')
#print(resumen_demanda_df.head())

resumen_demanda_df.to_excel("output/respuesta_punto2.xlsx")

max_desviacion = resumen_demanda_df.loc[resumen_demanda_df['desviacion_estandar'].idxmax()]
#print(max_desviacion)
#Respuesta: El que presenta la mayor dispersión es EPMC, debido a que tiene la desviación estándar más alta.

#Ejercicio 3
precios_df_2019 = pd.read_excel("datos/Precio_Bolsa_Nacional_2019.xlsx")
precios_df_2020 = pd.read_excel("datos/Precio_Bolsa_Nacional_2020.xlsx")

precios_df = pd.concat([precios_df_2019, precios_df_2020])
#print(precios_df.head())

#Ejercicio 4
#H0: La demanda diaria de los miércoles es mayor que la de los domingos

def get_day_name(date):
    DIAS = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
    now = time.localtime()
    weekday_index = now.tm_wday
    print(DIAS[weekday_index])    


# t,p = stats.ttest_ind(df.Turnover[df.Type.eq('A')], df.Turnover[df.Type.eq('B')], 
#                       equal_var=False, alternative='less')

if p < 0.05:
    print('La demanda diaria de los miércoles es mayor que la de los domingos, con 95% de confianza')
else:
    print('La hipótesis (medias iguales) no puede ser rechazada.')

#Ejercicio 5
