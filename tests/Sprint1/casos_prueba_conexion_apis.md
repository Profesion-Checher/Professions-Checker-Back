# Casos de Prueba Funcionales – Historia de Usuario #6
**Historia de Usuario:** Conectar las APIs (Frontend/Backend-DB)  
**Objetivo:** Validar la conexión funcional entre el Frontend y el Backend mediante API REST

---

## Tabla Resumen de Casos de Prueba

| ID Caso | Nombre Caso de Prueba                  | Tipo de Escenario       | Resultado Esperado                           | Estado  |
|---------|-----------------------------------------|--------------------------|-----------------------------------------------|---------|
| CP_01   | ConectarAPIs_CasoExitoso                  | Flujo principal (exitoso)  | Frontend consume y muestra datos del backend  | Exitoso |
| CP_02   | ConectarAPIs_BackendFueraDeServicio     | Error                    | Mensaje de error al no recibir respuesta      | Exitoso |
| CP_03   | ConectarAPIs_RespuestaVaciaDelBackend   | Flujo alternativo        | Frontend maneja sin romperse la respuesta vacía | Exitoso |
| CP_04   | ConectarAPIs_DatosMalformateados        | Error                    | Frontend muestra mensaje de error o ignora campo inválido | Exitoso |

---

## CP_01 – ConectarAPIs_CasoExitoso

**Descripción:** Se probará la conexión completa y funcional entre el frontend y el backend, cuando el backend responde correctamente.

**Pasos y condiciones de ejecución:**
1. Iniciar la aplicación (Frontend).
2. Asegurarse de que el Backend esté activo en el puerto correcto.
3. Realizar una acción en el frontend que haga una petición a la API (pedir lista de profesiones).
4. Verificar que los datos se muestran correctamente en la UI.

**Resultado esperado:**  
El frontend debe mostrar los datos devueltos por el backend correctamente (lista de profesiones).

**Estado del caso:** Exitoso

**Resultado obtenido:** El frontend muestra correctamente los datos obtenidos del backend. 

**Errores asociados:** Ninguno 

**Responsable diseño:** Marcela 

**Responsable ejecución:** Marcela 

**Comentarios:** Asegúrese de que el `.env` de frontend tenga la URL del backend correcta.

---

## CP_02 – ConectarAPIs_BackendFueraDeServicio

**Descripción:** Se probará la respuesta del sistema cuando el backend está caído o fuera de servicio.

**Pasos:**
1. Apagar el servidor backend (simular caída).
2. Iniciar el frontend.
3. Intentar hacer una petición al backend desde el frontend.

**Resultado esperado:**  
El frontend debe mostrar un mensaje de error tipo: “No se pudo obtener la información. Intente más tarde”.

**Estado del caso:** Exitoso  

**Resultado obtenido:** El frontend muestra un mensaje: "Load failed" 

**Errores asociados:** No se pudo establecer conexión con el backend. Frontend capturó correctamente el error. 

**Responsable diseño:** Marcela

**Responsable ejecución:** Marcela

**Comentarios:** Esto prueba la resiliencia del frontend frente a fallos del backend.

---

## CP_03 – ConectarAPIs_RespuestaVaciaDelBackend

**Descripción:** Validar comportamiento del frontend cuando el backend responde correctamente pero sin datos.

**Pasos:**
1. Asegurar que el backend responda con `200 OK` pero un array vacío (`[]`).
2. Realizar la petición desde el frontend.

**Resultado esperado:**  
El frontend debe mostrar un mensaje como: “No hay resultados disponibles” y no debe mostrar errores en consola.

**Estado:** Exitoso 

**Resultado obtenido:** El frontend no muestra ningún mensaje, ni error visible.

**Errores asociados:** Falta manejo adecuado para datos vacíos.

**Responsable diseño:** Marcela  

**Responsable ejecución:** Marcela

**Comentarios:** Ideal para validar UX cuando no hay contenido.

---

## CP_04 – ConectarAPIs_DatosMalformateados

**Descripción:** Validar qué ocurre si el backend devuelve datos mal estructurados (por ejemplo, falta un campo obligatorio).

**Pasos:**
1. Modificar temporalmente la respuesta del backend para omitir un campo esperado.
2. Cargar los datos desde el frontend.

**Resultado esperado:**  
El frontend debería evitar romperse. Puede mostrar un mensaje como “Dato no disponible” o ignorar ese campo.

**Estado:** Exitoso 

**Resultado obtenido:** El frontend no muestra ningún mensaje, ni error visible.

**Errores asociados:** Falta manejo adecuado para datos incompletos o mal formateados.

**Responsable diseño:** Marcela 

**Responsable ejecución:** Marcela

**Comentarios:** Importante validar que el frontend tenga validaciones para casos inesperados.

---