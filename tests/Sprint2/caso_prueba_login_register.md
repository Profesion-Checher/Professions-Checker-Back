# 🔐 Casos de Prueba Funcionales – Historia de Usuario #1

**Historia de Usuario:** Login/Register  
**Descripción:** Yo como usuario quiero iniciar sesión o registrarme si no tengo una cuenta.

---

## ✅ Tabla Resumen de Casos de Prueba

| ID Caso | Nombre Caso de Prueba        | Tipo de Escenario       | Resultado Esperado                                                       | Estado    |
|---------|-------------------------------|--------------------------|---------------------------------------------------------------------------|-----------|
| CP_01   | Login_Correcto                | Flujo principal (exitoso)| El usuario inicia sesión exitosamente con correo y contraseña válidos    | Pendiente |
| CP_02   | Login_CamposVacios            | Validación de formulario | Se muestran errores por campos obligatorios no llenados                   | Pendiente |
| CP_03   | Login_CredencialesInvalidas   | Flujo alternativo        | Se muestra error por correo o contraseña incorrectos                      | Pendiente |
| CP_04   | Registro_Correcto             | Flujo principal (exitoso)| El usuario se registra correctamente con todos los campos completados     | Pendiente |
| CP_05   | Registro_CamposVacios         | Validación de formulario | Se muestran errores por campos no llenados                                | Pendiente |
| CP_06   | Registro_AutenticadorExterno  | Integración externa      | El usuario puede autenticarse mediante servicio externo (OAuth)           | Pendiente |

---

## CP_01 – Login_Correcto

**Descripción:** Verifica que el usuario pueda iniciar sesión correctamente con credenciales válidas.

**Pasos y condiciones de ejecución:**
1. Ir a la página de login.
2. Ingresar un correo y contraseña válidos.
3. Hacer clic en “Iniciar sesión”.

**Resultado esperado:**  
El usuario es redirigido a la página principal tras autenticarse exitosamente.

**Estado del caso:** Pendiente  
**Resultado obtenido:** –  
**Errores asociados:** –  
**Responsable diseño:** Marcela  
**Responsable ejecución:** Marcela  
**Comentarios:** Asegurar conexión con backend activo.

---

## CP_02 – Login_CamposVacios

**Descripción:** Verifica el comportamiento cuando se dejan campos vacíos en el formulario de login.

**Pasos:**
1. Acceder a la página de login.
2. Dejar en blanco el campo de correo o contraseña.
3. Presionar “Iniciar sesión”.

**Resultado esperado:**  
Se muestran mensajes como “Este campo es obligatorio”.

**Estado del caso:** Pendiente  
**Resultado obtenido:** –  
**Errores asociados:** –  
**Responsable diseño:** Marcela  
**Responsable ejecución:** Marcela  
**Comentarios:** Ideal para probar validación frontend.

---

## CP_03 – Login_CredencialesInvalidas

**Descripción:** Verifica que se muestre error si el usuario ingresa credenciales incorrectas.

**Pasos:**
1. Ingresar un correo registrado con una contraseña incorrecta.
2. Hacer clic en “Iniciar sesión”.

**Resultado esperado:**  
Se muestra mensaje: “Correo o contraseña incorrectos”.

**Estado del caso:** Pendiente  
**Resultado obtenido:** –  
**Errores asociados:** –  
**Responsable diseño:** Marcela  
**Responsable ejecución:** Marcela  
**Comentarios:** Backend debe validar correctamente la autenticación.

---

## CP_04 – Registro_Correcto

**Descripción:** Verifica que el registro funcione con todos los campos requeridos llenos.

**Pasos:**
1. Acceder a la página de registro.
2. Llenar nombre, apellido, tipo de usuario, correo y contraseña.
3. Enviar formulario.

**Resultado esperado:**  
El usuario se registra correctamente y se le redirige al login o dashboard.

**Estado del caso:** Pendiente  
**Resultado obtenido:** –  
**Errores asociados:** –  
**Responsable diseño:** Marcela  
**Responsable ejecución:** Marcela  
**Comentarios:** Probar también que no se repita un correo existente.

---

## CP_05 – Registro_CamposVacios

**Descripción:** Verifica que el formulario de registro valide campos obligatorios.

**Pasos:**
1. Acceder a la página de registro.
2. Dejar en blanco uno o varios campos obligatorios.
3. Enviar formulario.

**Resultado esperado:**  
Se muestran mensajes como “Este campo es obligatorio” junto a cada campo vacío.

**Estado del caso:** Pendiente  
**Resultado obtenido:** –  
**Errores asociados:** –  
**Responsable diseño:** Marcela  
**Responsable ejecución:** Marcela  
**Comentarios:** Verificar si los errores se muestran dinámicamente.

---

## CP_06 – Registro_AutenticadorExterno

**Descripción:** Verifica que se pueda registrar o iniciar sesión con autenticadores externos como Google o GitHub.

**Pasos:**
1. Ir a login o registro.
2. Hacer clic en botón “Continuar con Google/GitHub”.
3. Completar el flujo de autenticación externo.

**Resultado esperado:**  
El usuario se autentica exitosamente y accede a la aplicación.

**Estado del caso:** Pendiente  
**Resultado obtenido:** –  
**Errores asociados:** –  
**Responsable diseño:** Marcela  
**Responsable ejecución:** Marcela  
**Comentarios:** Validar correcto funcionamiento de OAuth2.

---
