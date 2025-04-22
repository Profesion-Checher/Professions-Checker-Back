# Casos de Prueba Funcionales – Historia de Usuario #7  
**Historia de Usuario:** Barra de menú para el buscador y los filtros  
**Descripción:** Yo como usuario deseo buscar información más precisa y aplicar filtros para buscar la información más fácil.

---

## Tabla Resumen de Casos de Prueba

| ID Caso | Nombre Caso de Prueba              | Tipo de Escenario        | Resultado Esperado                                                                 | Estado    |
|---------|-------------------------------------|---------------------------|-------------------------------------------------------------------------------------|-----------|
| CP_17   | BuscarPorNombre_CasoExitoso           | Flujo principal (exitoso)   | Se muestran resultados que coinciden con el nombre ingresado                       | Pendiente |
| CP_18   | BuscarPorNombre_SinCoincidencias    | Flujo alternativo         | Mostrar mensaje “No se encontraron resultados para tu búsqueda”                    | Pendiente |
| CP_19   | FiltrarPorSalario_CasoExitoso         | Flujo principal (exitoso)   | Se muestran profesiones dentro del rango salarial especificado                     | Pendiente |
| CP_20   | FiltrarPorSalario_SinCoincidencias  | Flujo alternativo         | Mostrar mensaje “No se encontraron profesiones en ese rango salarial”              | Pendiente |

---

## CP_17 – BuscarPorNombre_CasoExitoso

**Descripción:** Verificar que al buscar una profesión por nombre, se muestren los resultados correctos.

**Pasos y condiciones de ejecución:**
1. Ingresar al sitio web.
2. Escribir un nombre válido de profesión en la barra de búsqueda (ej: “Desarrollador”).
3. Pulsar el botón de buscar.

**Resultado esperado:**  
Se muestran resultados que coinciden exactamente o parcialmente con el texto ingresado.

**Estado del caso:** Pendiente  
**Responsable diseño:** Marcela 
**Responsable ejecución:** Marcela
**Comentarios:** Validar tanto coincidencias exactas como parciales.

---

## CP_18 – BuscarPorNombre_SinCoincidencias

**Descripción:** Verificar el comportamiento cuando no hay coincidencias con la búsqueda.

**Pasos:**
1. Ingresar un nombre no registrado o poco común (ej: “Astronauta de Marte”).
2. Ejecutar la búsqueda.

**Resultado esperado:**  
Mostrar un mensaje claro: “No se encontraron resultados para tu búsqueda”.

**Comentarios:** Importante dar feedback visual sin errores de carga ni páginas vacías.

---

## CP_19 – FiltrarPorSalario_CasoExitoso

**Descripción:** Verificar que el sistema muestre correctamente las profesiones que se encuentran en el rango salarial seleccionado.

**Pasos:**
1. Ingresar al sitio.
2. Seleccionar un rango de salarios (ej: $3M – $7M).
3. Aplicar filtro.

**Resultado esperado:**  
Mostrar únicamente las profesiones cuyo salario esté dentro del rango seleccionado.

**Comentarios:** Se debe validar que el backend reciba los valores correctos del filtro.

---

## CP_20 – FiltrarPorSalario_SinCoincidencias

**Descripción:** Comprobar el comportamiento cuando el rango seleccionado no contiene ninguna profesión.

**Pasos:**
1. Seleccionar un rango salarial muy alto (ej: $50M – $100M).
2. Aplicar filtro.

**Resultado esperado:**  
Mensaje del tipo: “No se encontraron profesiones en ese rango salarial”.

**Comentarios:** Asegurar que el mensaje sea claro y visualmente accesible.

---