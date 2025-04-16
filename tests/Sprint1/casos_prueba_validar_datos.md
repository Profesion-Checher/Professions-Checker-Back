# Casos de Prueba Funcionales – Historia de Usuario #30  
**Historia de Usuario:** Validación de la calidad de los datos  
**Descripción:** Como científico de datos quiero validar la calidad y consistencia del dataset antes de entrenar el modelo para asegurar que los resultados del regresor no se vean afectados por datos erróneos o faltantes.

---

## Tabla Resumen de Casos de Prueba

| ID Caso | Nombre Caso de Prueba                  | Tipo de Escenario         | Resultado Esperado                                                                     | Estado    |
|---------|-----------------------------------------|----------------------------|-----------------------------------------------------------------------------------------|-----------|
| CP_26   | Validacion_Nulos                       | Validación de datos        | Se identifican y reportan los valores nulos por columna                                 | Pendiente |
| CP_27   | Validacion_ImputacionEliminacion       | Transformación de datos    | Se aplican técnicas de imputación o eliminación correctamente                           | Pendiente |
| CP_28   | Validacion_DuplicadosTipos             | Limpieza de datos          | Se eliminan duplicados y se verifica que los tipos de datos sean correctos              | Pendiente |
| CP_29   | Validacion_ErrorInesperado             | Flujo alternativo          | Si ocurre error inesperado, se lanza mensaje de advertencia y se cancela el preprocesado | Pendiente |

---

## CP_26 – Validacion_Nulos

**Descripción:** Verificar que se identifiquen correctamente los valores nulos por columna y se genere un reporte claro.

**Pasos y condiciones de ejecución:**
1. Cargar el dataset preprocesado.
2. Ejecutar análisis de valores nulos.
3. Generar reporte indicando cuántos nulos hay por columna.

**Resultado esperado:**  
Se muestra una tabla o log con el conteo de nulos por columna, sin errores de ejecución.

**Estado del caso:** Pendiente  
**Responsable diseño:** [Tu Nombre]  
**Responsable ejecución:** [Tester]  
**Comentarios:** Este paso es clave antes de decidir imputar o eliminar datos.

---

## CP_27 – Validacion_ImputacionEliminacion

**Descripción:** Validar que, al encontrar valores nulos, se apliquen correctamente las técnicas de imputación o eliminación según el caso.

**Pasos:**
1. Detectar columnas con valores nulos.
2. Aplicar imputación (media, mediana, moda) o eliminación de filas/columnas.
3. Validar que el dataset resultante no contenga nulos.

**Resultado esperado:**  
Se procesan los valores nulos y se obtiene un dataset limpio sin pérdidas innecesarias de información.

**Comentarios:** Documentar qué estrategia de imputación se usó en cada caso.

---

## CP_28 – Validacion_DuplicadosTipos

**Descripción:** Asegurar que los datos no tengan duplicados y los tipos de cada columna sean consistentes con su propósito.

**Pasos:**
1. Verificar existencia de registros duplicados y eliminarlos.
2. Revisar tipos de datos (por ejemplo, fechas como `datetime`, números como `float` o `int`).
3. Corregir cualquier inconsistencia.

**Resultado esperado:**  
No hay registros duplicados y los tipos de datos son adecuados para cada variable.

**Comentarios:** Añadir test automático para validar consistencia de tipos en futuros datasets.

---

## CP_29 – Validacion_ErrorInesperado

**Descripción:** Evaluar qué ocurre si se introduce un dataset con errores estructurales graves (faltan columnas clave, tipos incompatibles).

**Pasos:**
1. Introducir archivo corrupto o mal formado.
2. Ejecutar rutina de validación.

**Resultado esperado:**  
El sistema lanza advertencia del tipo: “Error en la validación: el dataset no cumple con el formato esperado”.

**Comentarios:** Fundamental para evitar entrenamientos con datos de baja calidad.

---