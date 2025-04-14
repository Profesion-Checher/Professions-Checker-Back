# Casos de Prueba Funcionales – Historia de Usuario #3
**Historia de Usuario:** Ver profesiones  
**Descripción:** Yo como usuario deseo ver las opciones de profesiones.

---

## Tabla Resumen de Casos de Prueba

| ID Caso | Nombre Caso de Prueba                | Tipo de Escenario        | Resultado Esperado                                           | Estado    |
|---------|---------------------------------------|---------------------------|---------------------------------------------------------------|-----------|
| CP_10   | VerProfesiones_CasoExitoso              | Flujo principal (exitoso)   | Se muestran correctamente las profesiones del sector tech     | Pendiente |
| CP_11   | VerProfesiones_SinConexion            | Error                     | Mensaje de error si no se puede acceder al backend            | Pendiente |
| CP_12   | VerProfesiones_ListaVacia             | Flujo alternativo         | Mostrar mensaje “No hay profesiones disponibles”              | Pendiente |
| CP_13   | VerProfesiones_FiltroSector           | Validación de contenido   | Todas las profesiones listadas deben pertenecer al sector TI  | Pendiente |

---

## CP_10 – VerProfesiones_CasoExitoso

**Descripción:** Validar que al seleccionar la opción de “ver profesiones” se despliegan correctamente las opciones.

**Pasos y condiciones de ejecución:**
1. Entrar a la aplicación como usuario autenticado o público.
2. Hacer clic en la opción “Ver profesiones”.
3. Visualizar la lista de profesiones disponibles.

**Resultado esperado:**  
Se despliega una lista de profesiones del sector de tecnologías como: Desarrollador, QA, Analista de datos, etc.

**Estado del caso:** Pendiente  
**Responsable diseño:** Marcela  
**Responsable ejecución:** Marcela 
**Comentarios:** Verificar que se vean todas y que estén correctamente escritas.

---

## CP_11 – VerProfesiones_SinConexion

**Descripción:** Simular error de conexión con el servidor al intentar cargar las profesiones.

**Pasos:**
1. Desconectar el backend o simular caída del servicio.
2. Intentar acceder a “Ver profesiones”.

**Resultado esperado:**  
El sistema debe mostrar un mensaje tipo: “No se pudo cargar la información. Intenta más tarde”.

**Comentarios:** Asegura buena gestión de errores y feedback al usuario.

---

## CP_12 – VerProfesiones_ListaVacia

**Descripción:** Verificar qué ocurre si la lista de profesiones está vacía.

**Pasos:**
1. Eliminar profesiones del backend o vaciar la base de datos.
2. Acceder a la opción “Ver profesiones”.

**Resultado esperado:**  
Mostrar mensaje como: “Actualmente no hay profesiones disponibles”.

**Comentarios:** Aporta a una mejor experiencia de usuario.

---

## CP_13 – VerProfesiones_FiltroSector

**Descripción:** Validar que todas las profesiones mostradas sean exclusivamente del sector tecnológico.

**Pasos:**
1. Ingresar a “Ver profesiones”.
2. Revisar manual o automáticamente que cada opción corresponda al sector TI.

**Resultado esperado:**  
Todas las profesiones deben estar relacionadas con el sector de tecnologías. Ej: DevOps, Ciberseguridad, etc.  
Ninguna profesión ajena (ej: Panadero, Médico) debe aparecer.

**Comentarios:** Esto verifica que se aplique correctamente un filtro por categoría.

---