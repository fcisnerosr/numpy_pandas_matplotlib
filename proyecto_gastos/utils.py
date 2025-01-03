def aplicar_reemplazos(df, columna, replacements):
    """
    Aplica reemplazos en la columna especificada de un DataFrame.
    """
    for old, new in replacements.items():
        df[columna] = df[columna].str.replace(old, new, regex=True)
    return df

#  # Diccionario de reemplazos
#  replacements = {
#      'tdc|Tdc|Transferencia': 'debito',
#      'bebe|bebe_recién_nacido': 'bebe',
#      'formacion|jardín|cursos': 'educacion',
#      'limpieza|medicina|farmacia': 'salud',
#      'preparacion|comidas_fuera_del_hogar': 'alimentacion',
#      'membresia|suscripcion': 'otros',
#      'viajes|excursiones': 'viajes'
#  }
