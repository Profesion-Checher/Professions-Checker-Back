# Casos de Prueba Funcionales – Historia de Usuario #28  
**Historia de Usuario:** Entrenamiento base del regresor  
**Descripción:** Yo como científico de datos quiero entrenar un modelo de regresión lineal con los datos preprocesados para obtener una primera versión funcional que permita evaluar su rendimiento inicial.

---

## Tabla Resumen de Casos de Prueba

| ID Caso | Nombre Caso de Prueba              | Tipo de Escenario        | Resultado Esperado                                                               | Estado    |
|---------|-------------------------------------|---------------------------|-----------------------------------------------------------------------------------|-----------|
| CP_22   | Regresor_EntrenamientoCorrecto      | Flujo principal (exitoso)   | El modelo OLS es entrenado con el 70% de los datos sin errores                   | Pendiente |
| CP_23   | Regresor_EvaluacionCorrecta         | Flujo principal (exitoso)   | El 30% de los datos se usa para evaluar el modelo, obteniendo métricas válidas   | Pendiente |
| CP_24   | Regresor_GuardadoModelo             | Guardado persistente      | El modelo entrenado se guarda correctamente como archivo `.pkl`                  | Pendiente |
| CP_25   | Regresor_ErrorEntrenamiento         | Flujo alternativo         | Si ocurre un error durante el entrenamiento, se captura y se muestra mensaje     | Pendiente |

---

## CP_22 – Regresor_EntrenamientoCorrecto

**Descripción:** Verificar que el modelo de regresión lineal OLS se entrene con al menos el 70% de los datos.

**Pasos y condiciones de ejecución:**
1. Preprocesar y dividir el dataset en 70% entrenamiento y 30% prueba.
2. Entrenar modelo OLS con el conjunto de entrenamiento.
3. Comprobar si el modelo se entrena sin errores.

**Resultado esperado:**  
Modelo entrenado con éxito sobre los datos de entrenamiento.

**Estado del caso:** Pendiente  
**Responsable diseño:** Marcela 
**Responsable ejecución:** [Tester]  
**Comentarios:** Validar que el conjunto de entrenamiento esté balanceado y limpio.

---

## CP_23 – Regresor_EvaluacionCorrecta

**Descripción:** Evaluar el rendimiento del modelo usando el 30% restante del dataset.

**Pasos:**
1. Usar el modelo entrenado para predecir sobre el conjunto de prueba.
2. Calcular métricas como RMSE, R², MAE.
3. Verificar que las métricas sean coherentes y útiles.

**Resultado esperado:**  
Se obtienen métricas que permiten evaluar si el modelo es funcional en una primera versión.

**Comentarios:** Guardar métricas en log o consola para seguimiento.

---

## CP_24 – Regresor_GuardadoModelo

**Descripción:** Comprobar que el modelo entrenado se guarda correctamente en un archivo `.pkl`.

**Pasos:**
1. Entrenar modelo.
2. Guardar modelo usando `joblib` o `pickle`.
3. Verificar existencia del archivo `.pkl`.

**Resultado esperado:**  
El archivo `modelo_regresor.pkl` (o similar) es creado y almacena el modelo entrenado correctamente.

**Comentarios:** Verificar que el archivo sea reutilizable en etapas posteriores.

---

## CP_25 – Regresor_ErrorEntrenamiento

**Descripción:** Validar que si ocurre un error durante el entrenamiento, el sistema lo detecta y muestra mensaje adecuado.

**Pasos:**
1. Provocar error (ej. datos faltantes, tipos incorrectos).
2. Ejecutar entrenamiento del modelo.

**Resultado esperado:**  
Mostrar mensaje: “Error durante el entrenamiento del modelo. Verifique los datos.”

**Comentarios:** Es fundamental tener manejo de excepciones para evitar caídas silenciosas del sistema.

---