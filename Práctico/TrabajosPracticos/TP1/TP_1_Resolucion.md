## TP1 - Aplicacion Mis Gastos Familiares

**Roles identificados como usuarios:**  
- Gestor de gastos (familiar que administrará la aplicacion)

**User Stories identificadas para cada rol**  
- Registrar responsable de gasto 
    > Registro del campo "familiar", quien realizó el gasto. 
No necesariamente usuario Gestor es el familiar que generó el gasto
- Iniciar sesión
- Registrar gasto
- Visualizar planilla de gastos
    > Este US si incluira la opcion de ordenar gastos segun un criterio determinado. Pero NO el filtro de datos.
- Modificar gasto
- Registrar tipo de gasto
    > Alta de un nuevo campo "tipo de gasto": descripción general del gasto realizado. Ejemplo: vacaciones/compras/educacion...
- Registrar usuario
    > Registro del Gestor de gastos
- Filtrar gastos
    > Funcionalidad extra en la planilla de gastos, que filtrar gastos segun distintos criterios: familiar, tipo gasto, monto mayor a ... 
- Cerrar sesión

**Descripcion de US**
 
> **Registrar gasto**  
> Como Gestor de datos quiero registrar un gasto familiar para tener seguimiento de cuánto se gastó  
>
> Criterios de aceptacion:  
>\- El gestor debe estar logueado  
>\- Debe mostrarse el nombre y apellido del usuario logueado  
>\- El gestor debe seleccionar al familiar que realizo el gasto. Por defecto se muestra al propio gestor   
>\- Debe mostrarse como fecha del gasto la fecha actual del sistema  
>\- El gestor puede modificar la fecha por una fecha anterior  
>\- El gestor puede seleccionar un tipo de gasto  
>\- El gestor debe cargar el monto del gasto, siendo este monto un numero positivo  
>
> Pruebas de usuario:  
>\- Probar registrar gasto con nombre y apellido de gestor, fecha actual, tipo de gasto y monto positivo [PASA]  
>\- Probar registrar gasto con nombre y apellido de gestor, fecha actual y monto positivo [PASA]
>\- Probar registrar un gasto sin estar logueado [FALLA]  
>\- Probar registrar un gasto sin indicar familiar [FALLA]
>\- Probar registrar un gasto indicando como monto un valor negativo [FALLA]  
  
> **Visualizar planilla de gastos**  
> Como Gestor de datos quiero visualizar la planilla de gastor para acceder a la información de mis gastos cargados  
>
> Criterios de aceptacion:  
>\- Se debe visualizar columnas monto, tipo de gasto, fecha de gasto, responsable de gasto    
>\- Se puede modificar el modo de ordenamiento de datos: por fecha, por monto, de modo ascendente/descendente. Por defecto, se ordena por fecha-descendente  
>\- Se puede modificar el periodo de fecha de los gastos que se muestran. Por defecto, se muestran gastos del ultimo mes  
>\- Se debe visualizar el monto total de los gastos en el periodo seleccionado
>
> Pruebas de usuario:  
>\- Probar visualizar planilla con monto, tipo de gasto, fecha de gasto y responsable de gasto, ordenado por fecha descendente [PASA]  
>\- Probar ordenar gastos por monto ascendente [PASA]  
>\- Probar cambiar periodo a ultimos dos meses de gastos [PASA]  
>\- Probar cambiar periodo a uno posterior al actual [FALLA]  

- No quedo claro si el filtro de periodo se incluye... Pero si a nuestro criterio lo incluimos, recordar que tiene que haber concordancia entre lo que anotamos como Criterios y luego lo que validamos en las Pruebas