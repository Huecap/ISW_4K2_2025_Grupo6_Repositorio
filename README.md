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
|--- Práctico 
		|--- TrabajosPracticos
				|--- TP<N>
```


## Ítems de configuración

| Items de Configuracion                       | Tipo               | Esquema de Nombrado                              | Ubicacion                                                                                 |
| -------------------------------------------- | ------------------ | ------------------------------------------------ | ----------------------------------------------------------------------------------------- |
| Plan de gestión de configuración de software | InformacionGeneral | `README.MD`                                      | `ICS_4K2_2025_G6_Repositorio`                                                             |
| Programa                                     | InformacionGeneral | `Programa.<ext>`                                 | `ICS_4K2_2025_G6_Repositorio/InformacionGeneral`                                          |
| Cronograma                                   | InformacionGeneral | `Cronograma_Clases.<ext>`                        | `ICS_4K2_2025_G6_Repositorio/InformacionGeneral`                                          |
| Presentación de clase                        | Teorico            | `Presentacion_<N>_<Tema>.<ext>`                  | `ICS_4K2_2025_G6_Repositorio/Teórico`                                                     |
| Trabajo Practico Consignas                   | Práctico           | `TP_<N>_Consigna.<ext>`                          | `ICS_4K2_2025_G6_Repositorio/Práctico/TrabajosPracticos/TP<N>`                            |
| Trabajo Practico Resuelto                    | Práctico           | `TP_<N>_Resolucion.<ext>`                        | `ICS_4K2_2025_G6_Repositorio/Práctico/TrabajosPracticos/TP<N>`                            |
| Guia Ejercicios Resueltos                    | Practico           | `Ejercicios ResueltosConsignasYResoluciones.pdf` | `ISW_4K2_Repositorio_Grupo6_2025/Práctico/Ejercicios ResueltosConsignasYResoluciones.pdf` |
| Tp Consignas                                 | Práctico           | `TP_Consignas.<ext>`                             | `ICS_4K2_2025_G6_Repositorio/Práctico/TrabajosPracticos/`                                 |

---

## Glosario

| Palabra             | Significado                                                                    | Ejemplos                         |
| ------------------- | ------------------------------------------------------------------------------ | -------------------------------- |
| ICS                 | Abreviatura de Ingeniería y calidad de software                                | `ICS_4K2_2025_G6_Repositorio`    |
| 4K2                 | Comisión de Cursado de la asignatura                                           |                                  |
| 2025                | Año de desarrollo del proyecto                                                 |                                  |
| G6                  | Numero Grupo en el que se desarrollo el proyecto                               |                                  |
| TP                  | Abreviatura de Trabajo Practico                                                | `TP_Consignas.<ext>`             |
| ER                  | Abreviatura de Ejericio Resuelto                                               | `ER_Consignas_y_Resoluciones.<ext>` |
| `<N>`               | Numero de trabajo / clase / actividad                                          | `TP_<1>_Resolucion.<ext>`        |
| `<ext>`             | Extensión del archivo en cuestion (.pdf, .txt, .md, etc)                       | `Programa.<pdf>`                 |


## Criterios de establecimiento de Linea base

>Luego de cada entrega con correcciones de un trabajo práctico, se establecerá una nueva versión de la Línea Base. Esto se debe a que, con cada corrección, se obtiene una versión completa y actualizada del trabajo, la cual será asignada como Línea Base.


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
**Commits merge**
```
Merge pull request #<N> from <branch> to <branch/main>
```

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
