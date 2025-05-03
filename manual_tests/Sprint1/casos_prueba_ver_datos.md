# Casos de Prueba Funcionales – Historia de Usuario #18
**Historia de Usuario:** Ver datos recopilados  
**Descripción:** Yo como administrador quiero ver la información recopilada de la aplicación.

---

## Tabla Resumen de Casos de Prueba

| ID Caso | Nombre Caso de Prueba                | Tipo de Escenario        | Resultado Esperado                                      | Estado    |
|---------|---------------------------------------|---------------------------|----------------------------------------------------------|-----------|
| CP_05   | VerDatos_CasoExitoso                    | Flujo principal (exitoso)   | Se muestra correctamente la información recopilada       | Pendiente |
| CP_06   | VerDatos_SinPermisos                  | Error                     | Acceso denegado si el usuario no es administrador        | Pendiente |
| CP_07   | VerDatos_SinInformacion               | Flujo alternativo         | Mensaje indicando que no hay información disponible      | Pendiente |
| CP_08   | VerDatos_ReportesGenerales            | Flujo principal (existoso)   | Se generan y visualizan correctamente los reportes       | Pendiente |
| CP_09   | VerDatos_ErrorDeCarga                 | Error                     | Mensaje de error al fallar la carga de información       | Pendiente |

---

## CP_05 – VerDatos_CasoExitoso

**Descripción:** Se verifica que el administrador puede acceder y ver la información recopilada correctamente.

**Pasos y condiciones de ejecución:**
1. Iniciar sesión como administrador.
2. Ir a la sección "Datos recopilados".
3. Verificar que se cargue la información (listas, gráficos, etc.).

**Resultado esperado:**  
La información recopilada debe visualizarse en la interfaz correctamente y sin errores.

**Estado del caso:** Pendiente  
**Responsable diseño:** Marcela  
**Responsable ejecución:** Marcela  
**Comentarios:** Verificar que los datos coincidan con los almacenados en base de datos.

---

## CP_06 – VerDatos_SinPermisos

**Descripción:** Validar que los usuarios sin rol de administrador no puedan acceder a la vista de datos recopilados.

**Pasos:**
1. Iniciar sesión como usuario estándar o no autenticado.
2. Intentar acceder a la ruta del dashboard o de datos recopilados.

**Resultado esperado:**  
Debe mostrarse un mensaje de error o redirigir al login/página de acceso denegado.

**Comentarios:** Esto prueba la protección de rutas y control de acceso por rol.

---

## CP_07 – VerDatos_SinInformacion

**Descripción:** Verificar comportamiento si no hay datos recopilados aún.

**Pasos:**
1. Asegurarse que la base de datos esté vacía o sin registros de usuarios.
2. Acceder a la vista de datos recopilados.

**Resultado esperado:**  
El sistema debe mostrar un mensaje tipo: “Aún no hay datos para mostrar”.

**Comentarios:** Importante para una buena UX cuando la app es nueva o recién lanzada.

---

## CP_08 – VerDatos_ReportesGenerales

**Descripción:** Validar que los reportes se generen correctamente desde la información recopilada.

**Pasos:**
1. Iniciar sesión como administrador.
2. Acceder a la sección de reportes.
3. Seleccionar tipo de reporte.
4. Visualizar reporte generado (gráfico, tabla, etc.).

**Resultado esperado:**  
El sistema debe mostrar correctamente los reportes según los datos reales.

**Comentarios:** Verifica tanto precisión como diseño visual del reporte.

---

## CP_09 – VerDatos_ErrorDeCarga

**Descripción:** Simular un error en la carga de los datos desde el backend.

**Pasos:**
1. Detener o manipular el endpoint que devuelve los datos.
2. Ingresar al dashboard como administrador.

**Resultado esperado:**  
Debe mostrarse un mensaje como “Hubo un error al cargar los datos” y no romper la vista.

**Comentarios:** Ideal para verificar gestión de errores con `try-catch` o mensajes amigables.

---