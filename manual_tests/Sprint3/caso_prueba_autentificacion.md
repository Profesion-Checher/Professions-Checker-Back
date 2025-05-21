# Casos de Prueba Funcionales – Historia de Usuario #14

**Historia de Usuario:** Autenticación  
**Descripción:** La aplicación debe ser capaz de permitir el acceso a las personas autorizadas, además de prohibir las personas sin autorización.

---

## Tabla Resumen de Casos de Prueba

| ID Caso | Nombre Caso de Prueba      | Tipo de Escenario       | Resultado Esperado                                                     | Estado    |
|---------|-----------------------------|--------------------------|-------------------------------------------------------------------------|-----------|
| CP_03   | Acceso_UsuarioAutorizado    | Flujo principal (exitoso)| El usuario autorizado accede correctamente a las funciones privadas     | Pendiente |
| CP_04   | Acceso_UsuarioNoAutorizado  | Flujo alternativo        | El usuario sin autorización es redirigido a la página de inicio         | Pendiente |

---

## CP_01 – Acceso_UsuarioAutorizado

**Descripción:** Verifica que un usuario autorizado pueda acceder correctamente a las funcionalidades protegidas de la aplicación.

**Pasos y condiciones de ejecución:**
1. Iniciar sesión con una cuenta válida y autorizada.
2. Intentar acceder a una ruta protegida (por ejemplo: `/dashboard`, `/consultas`).
3. Observar el contenido cargado.

**Resultado esperado:**  
El usuario accede sin problemas a las funcionalidades protegidas de la aplicación.

**Estado del caso:** Pendiente  
**Resultado obtenido:** –  
**Errores asociados:** –  
**Responsable diseño:** Marcela  
**Responsable ejecución:** Marcela  
**Comentarios:** Asegurar que el sistema reconozca el rol/permisos del usuario correctamente.

---

## CP_02 – Acceso_UsuarioNoAutorizado

**Descripción:** Verifica que un usuario sin autorización no pueda acceder a contenido protegido.

**Pasos:**
1. Acceder a la aplicación sin iniciar sesión o con una cuenta no autorizada.
2. Intentar acceder a una ruta protegida.
3. Observar la respuesta del sistema.

**Resultado esperado:**  
El usuario es redirigido automáticamente a la página de inicio o login.

**Estado del caso:** Pendiente  
**Resultado obtenido:** –  
**Errores asociados:** –  
**Responsable diseño:** Marcela  
**Responsable ejecución:** Marcela  
**Comentarios:** Validar también que no se permita acceso directo vía URL si no hay sesión activa.

---
