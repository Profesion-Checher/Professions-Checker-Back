# Casos de Prueba Funcionales – Historia de Usuario #29  
**Historia de Usuario:** Selección de variables predictoras  
**Descripción:** Yo como científico de datos quiero identificar las variables con mayor correlación con la variable objetivo para optimizar el rendimiento del modelo y reducir el overfitting.

---

## Tabla Resumen de Casos de Prueba

| ID Caso | Nombre Caso de Prueba                  | Tipo de Escenario         | Resultado Esperado                                                                       | Estado    |
|---------|-----------------------------------------|----------------------------|-------------------------------------------------------------------------------------------|-----------|
| CP_29   | SeleccionVars_GenerarHeatmap           | Análisis exploratorio      | Se genera y visualiza un heatmap con las correlaciones entre variables                   | Pendiente |
| CP_30   | SeleccionVars_TestMultiplesComb        | Evaluación comparativa     | Se documentan al menos dos combinaciones diferentes de variables con sus métricas        | Pendiente |
| CP_31   | SeleccionVars_ElegirFinal              | Validación cruzada         | Se selecciona la combinación con mejor performance basada en validación cruzada          | Pendiente |
| CP_32   | SeleccionVars_CasoError                | Flujo alternativo          | Si hay error en el análisis (faltan columnas, tipo incorrecto), se lanza mensaje claro   | Pendiente |

---

## CP_29 – SeleccionVars_GenerarHeatmap

**Descripción:** Verificar que se genere un mapa de calor visualizando las correlaciones entre todas las variables del dataset.

**Pasos y condiciones de ejecución:**
1. Cargar el dataset preprocesado.
2. Calcular la matriz de correlación (ej. Pearson).
3. Generar y guardar el heatmap.

**Resultado esperado:**  
El sistema genera una visualización clara en forma de heatmap que muestra la fuerza de correlación entre variables, destacando las más relevantes frente a la variable objetivo.

**Estado del caso:** Pendiente  
**Responsable diseño:** [Tu Nombre]  
**Responsable ejecución:** [Tester]  
**Comentarios:** El heatmap debe ser fácil de interpretar (colores bien definidos, etiquetas legibles).

---

## CP_30 – SeleccionVars_TestMultiplesComb

**Descripción:** Validar que se prueben al menos dos combinaciones diferentes de variables predictoras con sus respectivas métricas.

**Pasos:**
1. Definir dos o más subconjuntos de variables basadas en el análisis de correlación.
2. Entrenar modelos con cada subconjunto.
3. Registrar y comparar las métricas de validación.

**Resultado esperado:**  
Se documentan los resultados (RMSE, R², MAE, etc.) por cada conjunto probado y se justifican los cambios en rendimiento.

**Comentarios:** Puede automatizarse con validación cruzada y generación de logs.

---

## CP_31 – SeleccionVars_ElegirFinal

**Descripción:** Verificar que se elige la combinación óptima de variables según el mejor rendimiento medido en validación cruzada.

**Pasos:**
1. Comparar los resultados de las combinaciones anteriores.
2. Escoger la de mejor desempeño.
3. Guardar esta combinación como configuración base para entrenamiento.

**Resultado esperado:**  
Se selecciona un conjunto de variables óptimo con resultados consistentes y bajo riesgo de overfitting.

**Comentarios:** Incluir visualización de resultados en validación cruzada (boxplots, histogramas, etc.).

---

## CP_32 – SeleccionVars_CasoError

**Descripción:** Probar el comportamiento del sistema si el análisis no puede realizarse (datos faltantes, nombres incorrectos, etc.).

**Pasos:**
1. Introducir un dataset con columnas faltantes o mal nombradas.
2. Ejecutar análisis de correlación.

**Resultado esperado:**  
Mostrar mensaje: “Error al generar correlaciones: verifique las columnas y el formato del dataset”.

**Comentarios:** Importante evitar que el pipeline se rompa sin aviso útil.

---