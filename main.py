import pandas as pd 
import numpy as np

demanda_df_2019_1 = pd.read_excel("datos/Demanda_Comercial_Por_Comercializador_SEME1_2019.xlsx")
# print(len(demanda_df_2019_1.index))
# demanda_df_2019_2 = pd.read_excel("datos/Demanda_Comercial_Por_Comercializador_SEME2_2019.xlsx")
# demanda_df_2020_1 = pd.read_excel("datos/Demanda_Comercial_Por_Comercializador_SEME1_2020.xlsx")
# demanda_df_2020_2 = pd.read_excel("datos/Demanda_Comercial_Por_Comercializador_SEME2_2020.xlsx")

# demanda_df = pd.concat([demanda_df_2019_1, demanda_df_2019_2, demanda_df_2020_1, demanda_df_2020_2])
demanda_df = demanda_df_2019_1
# print(len(demanda_df.index))
# print(demanda_df.head())

demanda_df['demanda_dia'] = demanda_df.loc[:,'H0':'H23'].sum(axis=1)
# print(demanda_df.head())

#new_df = pd.pivot_table(demanda_df, values="demanda_dia", index=["Fecha", "tipo_mercado"], columns=["codigo_comercializador"], aggfunc=np.sum)
new_df = pd.pivot_table(demanda_df, values="demanda_dia", index=["Fecha", "tipo_mercado"], columns=["codigo_comercializador"]).reset_index()
# print(new_df.head())

new_df.to_excel("output/respuesta_punto1.xlsx")

#demanda_diaria_df = demanda_df.groupby(['Fecha', 'codigo_comercializador'])['demanda_dia'].agg('sum')
demanda_diaria_df = demanda_df.groupby(['Fecha', 'codigo_comercializador'])['demanda_dia'].agg(demanda_dia='sum').reset_index()
# print(demanda_diaria_df.head())

resumen_demanda_df = demanda_diaria_df.groupby(['codigo_comercializador'])['demanda_dia'].agg(promedio='mean', mediana='median', minimo='min', maximo='max', desviacion_estandar='std')
print(resumen_demanda_df.head())

resumen_demanda_df.to_excel("output/respuesta_punto2.xlsx")

#max_desviacion = resumen_demanda_df['desviacion_estandar'].idxmax()
max_desviacion = resumen_demanda_df.loc[resumen_demanda_df['desviacion_estandar'].idxmax()]
print(max_desviacion)