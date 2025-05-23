# Casos de Prueba Funcionales – Historia de Usuario #1

**Historia de Usuario:** Login/Register  
**Descripción:** Yo como usuario quiero iniciar sesión o registrarme si no tengo una cuenta.

---

## Tabla Resumen de Casos de Prueba

| ID Caso | Nombre Caso de Prueba        | Tipo de Escenario       | Resultado Esperado                                                       | Estado    |
|---------|-------------------------------|--------------------------|---------------------------------------------------------------------------|-----------|
| CP_04   | Login_Correcto                | Flujo principal (exitoso)| El usuario inicia sesión exitosamente con correo y contraseña válidos    | Exitoso |
| CP_05   | Login_CamposVacios            | Validación de formulario | Se muestran errores por campos obligatorios no llenados                   | Exitoso |
| CP_06   | Login_CredencialesInvalidas   | Flujo alternativo        | Se muestra error por correo o contraseña incorrectos                      | Exitoso |
| CP_07   | Registro_Correcto             | Flujo principal (exitoso)| El usuario se registra correctamente con todos los campos completados     | Exitoso |
| CP_08   | Registro_CamposVacios         | Validación de formulario | Se muestran errores por campos no llenados                                | Exitoso |

---

## CP_04 – Login_Correcto

**Descripción:** Verifica que el usuario pueda iniciar sesión correctamente con credenciales válidas.

**Pasos y condiciones de ejecución:**
1. Ir a la página de login.
2. Ingresar un correo y contraseña válidos.
3. Hacer clic en “Iniciar sesión”.

**Resultado esperado:**  
El usuario es redirigido a la página de su perfil tras autenticarse exitosamente.

**Estado del caso:** Exitoso
**Resultado obtenido:** El usuario es redirigifo a su página de perfil cuando se autentifica exitosamente.
**Errores asociados:** Ninguno 
**Responsable diseño:** Marcela  
**Responsable ejecución:** Marcela  
**Comentarios:** Asegurar conexión con backend activo.

---

## CP_05 – Login_CamposVacios

**Descripción:** Verifica el comportamiento cuando se dejan campos vacíos en el formulario de login.

**Pasos:**
1. Acceder a la página de login.
2. Dejar en blanco el campo de correo o contraseña.
3. Presionar “Iniciar sesión”.

**Resultado esperado:**  
Se muestran mensajes como “Llena este campo”.

**Estado del caso:** Exitoso  
**Resultado obtenido:** Se muestra el mensaje "Llena este campo" arriba del campo vacío. 
**Errores asociados:** Ninguno 
**Responsable diseño:** Marcela  
**Responsable ejecución:** Marcela  
**Comentarios:** Ideal para probar validación frontend.

---

## CP_06 – Login_CredencialesInvalidas

**Descripción:** Verifica que se muestre error si el usuario ingresa credenciales incorrectas.

**Pasos:**
1. Ingresar un correo registrado con una contraseña incorrecta.
2. Hacer clic en “Iniciar sesión”.

**Resultado esperado:**  
Se muestra mensaje: “Correo o contraseña incorrectos”.

**Estado del caso:** Pendiente  
**Resultado obtenido:** Se muestra el mensaje "Correo o contraseña incorrectos". 
**Errores asociados:** Ninguno 
**Responsable diseño:** Marcela  
**Responsable ejecución:** Marcela  
**Comentarios:** Backend debe validar correctamente la autenticación.

---

## CP_07 – Registro_Correcto

**Descripción:** Verifica que el registro funcione con todos los campos requeridos llenos.

**Pasos:**
1. Acceder a la página de registro.
2. Llenar nombre, apellido, correo y contraseña.
3. Enviar formulario.

**Resultado esperado:**  
El usuario se registra correctamente mostrando un mensaje "usuario registrado".

**Estado del caso:** Exitoso  
**Resultado obtenido:** El usuario se registra correctamente y se muestra el mensaje "usuario registrado con éxito".
**Errores asociados:** Ninguno
**Responsable diseño:** Marcela  
**Responsable ejecución:** Marcela  
**Comentarios:** Probar también que no se repita un correo existente.

---

## CP_08 – Registro_CamposVacios

**Descripción:** Verifica que el formulario de registro valide campos obligatorios.

**Pasos:**
1. Acceder a la página de registro.
2. Dejar en blanco uno o varios campos obligatorios.
3. Enviar formulario.

**Resultado esperado:**  
Se muestran mensajes como “Llena este campo” junto a cada campo vacío.

**Estado del caso:** Exitoso
**Resultado obtenido:** Muestra un mensaje "Llena este campo" arriba del campo vacío.
**Errores asociados:** Ninguno 
**Responsable diseño:** Marcela  
**Responsable ejecución:** Marcela  
**Comentarios:** Verificar si los errores se muestran dinámicamente.

---