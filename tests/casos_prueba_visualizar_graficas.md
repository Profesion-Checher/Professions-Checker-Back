# Casos de Prueba Funcionales – Historia de Usuario #26
**Historia de Usuario:** Visualizar gráficas  
**Descripción:** Yo como usuario quiero ver gráficas de los salarios de las profesiones proyectados en el futuro.

---

## ✅ Tabla Resumen de Casos de Prueba

| ID Caso | Nombre Caso de Prueba              | Tipo de Escenario        | Resultado Esperado                                                       | Estado    |
|---------|-------------------------------------|---------------------------|---------------------------------------------------------------------------|-----------|
| CP_14   | VerGraficas_CasoExitoso               | Flujo principal (exitoso)   | Se muestran gráficas con salarios proyectados de distintas profesiones   | Pendiente |
| CP_15   | VerGraficas_SinDatos                | Flujo alternativo         | Mostrar mensaje “No hay datos disponibles para proyectar”                | Pendiente |
| CP_16   | VerGraficas_DatosNoValidos          | Validación de datos       | Se muestra mensaje de error si los datos o predicciones están mal formados | Pendiente |
| CP_17   | VerGraficas_InteraccionUI           | Interacción usuario       | El usuario puede interactuar con la gráfica (hover, zoom, filtro, etc.)  | Pendiente |

---

## CP_14 – VerGraficas_CasoExitoso

**Descripción:** Verificar que al acceder a la opción de ver gráficas, se muestran proyecciones salariales correctamente.

**Pasos y condiciones de ejecución:**
1. Ingresar a la aplicación como usuario.
2. Ir a la sección de “Ver gráficas”.
3. Observar los gráficos generados de cada profesión con predicción salarial.

**Resultado esperado:**  
Se visualizan gráficos funcionales (línea, barra o área) con predicciones salariales para los próximos años, categorizados por profesión del sector TI.

**Estado del caso:** Pendiente  
**Responsable diseño:** Marcela  
**Responsable ejecución:** Marcela 
**Comentarios:** Se debe validar la precisión visual y comprensibilidad de las gráficas.

---

## CP_15 – VerGraficas_SinDatos

**Descripción:** Validar el comportamiento del sistema cuando no hay datos disponibles para graficar.

**Pasos:**
1. Simular ausencia de datos en la base de datos o respuesta vacía de la API.
2. Ingresar a la sección de gráficas.

**Resultado esperado:**  
Mostrar un mensaje del tipo: “No hay datos disponibles para generar gráficas”.

**Comentarios:** Importante mostrar feedback al usuario sin fallos visuales.

---

## CP_16 – VerGraficas_DatosNoValidos

**Descripción:** Verificar que el sistema maneje adecuadamente entradas erróneas o predicciones mal calculadas.

**Pasos:**
1. Introducir manualmente datos corruptos o inválidos en el backend.
2. Acceder a la sección de gráficas.

**Resultado esperado:**  
Mostrar un mensaje de error informativo: “Los datos no son válidos para graficar”.

**Comentarios:** Evita mostrar gráficas incoherentes o que generen errores en la interfaz.

---