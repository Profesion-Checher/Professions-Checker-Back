# Casos de Prueba Funcionales – Historia de Usuario #19

**Historia de Usuario:** Desplegar el sitio web  
**Descripción:** Yo como desarrollador quiero desplegar el sitio web.

---

## Tabla Resumen de Casos de Prueba

| ID Caso | Nombre Caso de Prueba     | Tipo de Escenario       | Resultado Esperado                                                  | Estado    |
|---------|----------------------------|--------------------------|------------------------------------------------------------------------|-----------|
| CP_01   | Despliegue_HostingCorrecto | Flujo principal (exitoso)| El sitio está disponible públicamente en un servicio de hosting       | Pendiente |
| CP_02   | Acceso_DesdeOtroEquipo     | Validación externa       | El sitio es accesible desde otro computador o red diferente           | Pendiente |

---

## CP_01 – Despliegue_HostingCorrecto

**Descripción:** Verifica que el sitio web esté correctamente desplegado en un servicio de hosting.

**Pasos y condiciones de ejecución:**
1. Obtener la URL generada por el servicio de hosting (ej. Vercel, Netlify, AWS, etc.).
2. Abrir un navegador web.
3. Ingresar la URL y presionar Enter.

**Resultado esperado:**  
El sitio se carga correctamente sin errores y muestra la interfaz esperada.

**Estado del caso:** Pendiente  
**Resultado obtenido:** –  
**Errores asociados:** –  
**Responsable diseño:** Marcela  
**Responsable ejecución:** Marcela  
**Comentarios:** Verificar también que los recursos (imágenes, estilos, scripts) se cargan correctamente.

---

## CP_02 – Acceso_DesdeOtroEquipo

**Descripción:** Verifica que el sitio desplegado sea accesible desde un equipo diferente al del desarrollador.

**Pasos:**
1. Compartir la URL del sitio desplegado con otro miembro del equipo o usar otro dispositivo.
2. Acceder al enlace desde una red diferente.
3. Verificar si el sitio carga correctamente.

**Resultado esperado:**  
El sitio se muestra de forma completa y funcional en otro computador.

**Estado del caso:** Pendiente  
**Resultado obtenido:** –  
**Errores asociados:** –  
**Responsable diseño:** Marcela  
**Responsable ejecución:** Marcela  
**Comentarios:** Se recomienda usar navegación en modo incógnito y diferentes navegadores para asegurar compatibilidad.

---
