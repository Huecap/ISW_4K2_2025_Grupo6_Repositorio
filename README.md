# Plan de gestión de configuración de software - Grupo 6 - 4K2 2025 

## Integrantes 

| Nombre completo                | Legajo |
| ------------------------------ | ------ |
| Arrigo Gaspar                  | 94365  |
| Alves Carneiro Rocío Mailen    | 94215  |
| Capdevila Vicente Huenu Lihuel | 94513  |
| Garcia Amadey Juan Cruz        | 90584  |
| Malnis Maria Sol               | 99535  |
| Gragera Facundo Gabriel        | 76547  |
| Becerra Felipe                 | 91680  |
| Castro Walter Matías           | 90557  |
| Rocca Valentino Gabriel        | 94774  |
| Villegas Angel Nahuel          | 94837  |


## Estructura del Proyecto 
```
ICS_4K2_2025_G6_Repositorio
|--- InformacionGeneral
|--- Teórico
		|--- MaterialBibliográfico
                |--- Tema
		|--- PresentacionesDeClase
		|--- Resumenes
|--- Práctico 
		|--- TrabajosPracticos
				|--- TP<N>
		|--- ActividadesClase
					|--- Actividades<N>
		|--- TrabajosResueltos
				|--- TPResueltos<N>
```


## Ítems de configuración

**Esquema de nomenclatura de archivos**

```
<Descripcion>_<CaracteristicaA>_<CaracteristicaB>_...<CaracteristicaN>_<N>.<ext>
```

| Items de Configuracion                       | Tipo               | Esquema de Nombrado                    | Ubicacion                                                               |
| -------------------------------------------- | ------------------ | -------------------------------------- | ----------------------------------------------------------------------- |
| Plan de gestión de configuración de software | Proyecto           | `README.MD`                            | `ICS_4K2_2025_G6_Repositorio`                                           |
| Planificación                                | InformacionGeneral | `Planificacion_ISC_4K2_2025.<ext>`     | `ICS_4K2_2025_G6_Repositorio/InformacionGeneral`                        |
| Cronograma                                   | InformacionGeneral | `Programa_ICS_4K2_2025.<ext>`          | `ICS_4K2_2025_G6_Repositorio/InformacionGeneral`                        |
| Libros                                       | Teorico            | `<NombreLibro>.<ext>`                  | `ICS_4K2_2025_G6_Repositorio/Teórico/MaterialBibliográfico`             |
| Presentación de clases                       | Teorico            | `Presentacion_Tema_<N>.<ext>`        | `ICS_4K2_2025_G6_Repositorio/Teórico/PresentacionesDeClase`             |
| Resúmenes de Unidades                        | Teorico            | `Resumen_Unidad_<N>.<ext>`             | `ICS_4K2_2025_G6_Repositorio/Teórico/Resumenes`                         |
| Links a clases grabadas Teórico              | Teórico            | `Links_Clases_Grabadas_Teorico.<ext>`  | `ICS_4K2_2025_G6_Repositorio/Teórico`                                   |
| Links a clases grabadas Práctico             | Práctico           | `Links_Clases_Grabadas_Practico.<ext>` | `ICS_4K2_2025_G6_Repositorio/Práctico`                                  |
| Trabajo Practico Consignas                   | Práctico           | `TP_<N>_Consignas.<ext>`                 | `ICS_4K2_2025_G6_Repositorio/Práctico/TrabajosPracticos/TP<N>`          |
| Trabajo Practico Resolucion                  | Práctico           | `TP_<N>_Resolucion.<ext>`              | `ICS_4K2_2025_G6_Repositorio/Práctico/TrabajosPracticos/TP<N>`          |
| Trabajo Practico Correcciónes                | Práctico           | `TP_<N>_Correcciones.<ext>`            | `ICS_4K2_2025_G6_Repositorio/Práctico/TrabajosPracticos/TP<N>`          |
| Actividades Consignas                        | Práctico           | `Actividad_<N>_Consignas.<ext>`        | `ICS_4K2_2025_G6_Repositorio/Práctico/ActividadesClase/Actividades<N>`  |
| Actividades resolucion                       | Práctico           | `Actividad_<N>_Resolucion.<ext>`       | `ICS_4K2_2025_G6_Repositorio/Práctico/ActividadesClase/Actividades<N>`  |
| Trabajos Practicos Resuelto Consignas        | Práctico           | `TPResuelto_<N>_Consignas.<ext>`       | `ICS_4K2_2025_G6_Repositorio/Práctico/TrabajosResueltos/TPResueltos<N>` |
| Trabajo Practico Resuelto Resolucion         | Práctico           | `TPResuelto_<N>_Resolucion.<ext>`      | `ICS_4K2_2025_G6_Repositorio/Práctico/TrabajosResueltos/TPResueltos<N>` |
| Links Clases Grabadas Practico               | Práctico           | `Links_Clases_Grabadas_Practico`       | `ICS_4K2_2025_G6_Repositorio/Práctico`                                  |

---

## Glosario

| Palabra             | Significado                                                                    | Ejemplos                         |
| ------------------- | ------------------------------------------------------------------------------ | -------------------------------- |
| ICS                 | Abreviacion de Ingeniería y calidad de software                                | `Planificacion_ISC_4K2_2025.pdf` |
| 4K2                 | Comisión de Cursado de la asignatura                                           | `Resumen_Unidad_4.md`            |
| 2025                | Año de desarrollo del proyecto                                                 | `Resumen_Unidad_3.md`            |
| G6                  | Numero Grupo en el que se desarrollo el proyecto                               | `Resumen_Unidad_1.md`            |
| `<N>`               | Numero de trabajo / clase / actividad                                          | `Actividad_12_Consignas.pdf`     |
| `<ext>`             | Extensión del archivo en cuestion (.pdf, .txt, .md, etc)                       | `Actividad_12_Consignas.pdf`     |
| `<CaracteristicaN>` | Hace referencia a alguna caracteristica significativa para el Item en cuestion | `Resumen_Unidad_3.md`            |


## Criterios de establecimiento de Linea base

>Luego de cada entrega de una corrección de un trabajo practico, se procederá a establecer una versión de la Línea base


## Esquema de Nomenclaturas para trabajar 

### Archivos
**Esquema de nomenclatura de archivos**

```
<Descripción>_<Numero>.<extension>
```

---
### Commits
**Esquema de nomenclatura de commits**
```
<tipo>(alcance): mensaje breve
```

Tipos: `feat`, `fix`, `docs`, `style`, `refactor`

|Tipo|Significado breve|Ejemplo commit|
|---|---|---|
|**feat**|Nueva funcionalidad|`feat(auth): agregar login con JWT`|
|**fix**|Corrección de bug|`fix(api): resolver error 500 en /users`|
|**docs**|Documentación|`docs(readme): actualizar pasos de instalación`|
|**style**|Formato/estilo (no lógica)|`style(css): reordenar clases del botón`|
|**refactor**|Reorganizar/mejorar código (sin cambiar comportamiento)|`refactor(user): simplificar lógica de registro`|
|**test**|Pruebas automáticas|`test(cart): agregar test para eliminar producto`|
|**chore**|Tareas varias / dependencias|`chore(deps): actualizar versión de express`|

---
### Ramas 
**Git Flow**

```
main -> estable
feature/<nombre>  -> Nuevas Funcionalidades
fix/<nombre> -> Fixes 
```
- **`main` → estable**
    - Rama principal que siempre contiene el código en **estado estable**.
    - Solo recibe merges de ramas ya probadas (features terminadas o fixes validados).
    - Representa el seguimiento de la **línea base de producción**.
- **`feature/<nombre>` → nuevas funcionalidades**
    - Ramas creadas a partir de `main`.
    - Se usan para desarrollar **nuevas características** sin afectar la rama estable.
    - Una vez finalizadas y probadas, se integran nuevamente a `main`.
    - Ejemplo: `feature/login`, `feature/reportes`.
- **`fix/<nombre>` → fixes**
    - Ramas específicas para realizar **correcciones puntuales de errores**.
    - Se crean desde `main` para atender problemas detectados en la versión estable.
    - Se fusionan de vuelta en `main` una vez validada la solución.
    - Ejemplo: `fix/error-login`, `fix/ui-navbar`.

---
### Lineas Base
**SemVer (Semantic Versioning)** -> ``MAJOR.MINOR.PATCH``
```
v1.0.0 → primera línea base.
v1.1.0 → nueva funcionalidad agregada.
v1.1.1 → solo bugfix.
```

- **MAJOR** → cambios que rompen compatibilidad (cambios grandes).
    - Ej: `1.x.x → 2.0.0`
    - Significa que la línea base marca una nueva etapa del producto.
- **MINOR** → nuevas funcionalidades, pero **compatibles** con lo anterior.
    - Ej: `1.2.0 → 1.3.0`
    - Línea base con funcionalidades extra, pero no rompe lo existente.
- **PATCH** → solo correcciones de errores (bugfixes), sin nuevas funcionalidades.
    - Ej: `1.3.0 → 1.3.1`
    - Línea base estable que corrige fallos.

---
**Anotaciones**
> Linea base: esperar hasta un cierto punto. momento claro. podría ser después de una entrega corregida, después de un tp... un momento definido
linea base la hace git 

glosario: hacer un txt que explique la nomenclatura abreviada 
