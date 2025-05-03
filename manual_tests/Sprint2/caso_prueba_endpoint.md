# Casos de Prueba Funcionales – Historia de Usuario #27

**Historia de Usuario:** Crear Endpoint entre el backend y la AI-API  
**Descripción:** Yo como desarrollador debo implementar un endpoint en el backend que permita la comunicación con la AI-API para obtener la predicción de salarios a futuro según la profesión, experiencia y salario actual.

---

## Tabla Resumen de Casos de Prueba

| ID Caso | Nombre Caso de Prueba           | Tipo de Escenario        | Resultado Esperado                                                    | Estado    |
|---------|----------------------------------|---------------------------|------------------------------------------------------------------------|-----------|
| CP_01   | Solicitud_Exitosa                | Flujo principal (exitoso)  | El backend envía los datos correctamente a la AI-API y recibe predicción| Pendiente |
| CP_02   | Validacion_DatosInvalidos         | Validación de entrada     | Se devuelve error 400 por datos incompletos o inválidos                | Pendiente |
| CP_03   | Manejo_Error_AIAPI_NoDisponible   | Flujo alternativo         | Se registra error en logs y se devuelve mensaje de error controlado    | Pendiente |
| CP_04   | Respuesta_Consistente_Formato     | Validación de formato     | El backend entrega respuesta en formato JSON consistente               | Pendiente |
| CP_05   | TiempoRespuesta_Razonable         | Validación de rendimiento | La respuesta se recibe en menos de 5 segundos                          | Pendiente |

---

## CP_01 – Solicitud_Exitosa

**Descripción:** Verifica que el backend procese correctamente solicitudes válidas y obtenga respuesta de la AI-API.

**Pasos y condiciones de ejecución:**
1. Enviar solicitud POST al endpoint con datos válidos: profesión, experiencia, salario_actual.
2. El backend debe validar la información.
3. El backend debe enviar la solicitud a la AI-API.
4. Recibir respuesta exitosa.

**Resultado esperado:**  
Se recibe una respuesta JSON con la predicción de salario futuro.

**Estado del caso:** Pendiente  
**Resultado obtenido:** –  
**Errores asociados:** –  
**Responsable diseño:** [Tu Nombre]  
**Responsable ejecución:** [Tu Nombre]  
**Comentarios:** Asegurarse que la AI-API esté disponible.

---

## CP_02 – Validacion_DatosInvalidos

**Descripción:** Verifica que el backend detecte datos de entrada inválidos y no realice la solicitud a la AI-API.

**Pasos:**
1. Enviar solicitud con datos faltantes o mal formateados (por ejemplo, experiencia negativa o salario como texto).
2. Backend debe validar la entrada antes de llamar a la AI-API.

**Resultado esperado:**  
Se recibe error 400 indicando “Datos inválidos”.

**Estado del caso:** Pendiente  
**Resultado obtenido:** –  
**Errores asociados:** –  
**Responsable diseño:** [Tu Nombre]  
**Responsable ejecución:** [Tu Nombre]  
**Comentarios:** Probar diferentes combinaciones de errores.

---

## CP_03 – Manejo_Error_AIAPI_NoDisponible

**Descripción:** Verifica que, en caso de que la AI-API no esté disponible, el backend maneje correctamente el error.

**Pasos:**
1. Apagar o simular caída de la AI-API.
2. Enviar solicitud válida al backend.

**Resultado esperado:**  
El backend responde con un error controlado (por ejemplo, error 503) y registra el error en los logs del servidor.

**Estado del caso:** Pendiente  
**Resultado obtenido:** –  
**Errores asociados:** –  
**Responsable diseño:** [Tu Nombre]  
**Responsable ejecución:** [Tu Nombre]  
**Comentarios:** Revisar archivo/log de errores tras la prueba.

---

## CP_04 – Respuesta_Consistente_Formato

**Descripción:** Verifica que el formato de la respuesta al frontend sea siempre el mismo, independientemente de la predicción.

**Pasos:**
1. Enviar múltiples solicitudes válidas.
2. Comparar estructura del objeto JSON de respuesta.

**Resultado esperado:**  
Siempre se recibe un JSON estructurado con los mismos campos (por ejemplo: `{ "profesion": "Ingeniero", "salario_actual": 40000, "prediccion": [...] }`).

**Estado del caso:** Pendiente  
**Resultado obtenido:** –  
**Errores asociados:** –  
**Responsable diseño:** [Tu Nombre]  
**Responsable ejecución:** [Tu Nombre]  
**Comentarios:** Muy importante para integración con frontend.

---

## CP_05 – TiempoRespuesta_Razonable

**Descripción:** Verifica que la respuesta del backend ocurra en un tiempo aceptable.

**Pasos:**
1. Enviar solicitud válida.
2. Medir tiempo de respuesta.

**Resultado esperado:**  
La respuesta debe recibirse en un tiempo menor a 5 segundos.

**Estado del caso:** Pendiente  
**Resultado obtenido:** –  
**Errores asociados:** –  
**Responsable diseño:** [Tu Nombre]  
**Responsable ejecución:** [Tu Nombre]  
**Comentarios:** Probar bajo diferentes condiciones de red si es posible.

---
