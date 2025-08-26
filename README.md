# Plan de gestión de configuración de software - Grupo 6 - 4K2 2025 

## Integrantes 
- Huenu Lihuel Capdevila Vicente - 94513 
- Arrigo Gaspar - 94365
- Alves Carneiro Rocío Mailen - 94215
- Garcia Amadey Juan Cruz - 90584
- Malnis Maria Sol - 99535
- Gragera Facundo Gabriel - 76547 
- Becerra Felipe - 91680
- Castro Walter Matías - 90557

## Estructura del Proyecto 
```
ISW_4K2_2025_G6_Repositorio
|--- Readme.md 
|--- InformacionGeneral
		|--- Planificacion_ISW_4K4_2025.<ext>
		|--- Programa_ICS_4K4_2025.<ext>
|--- Teórico
		|--- MaterialBibliográfico
				|--- <NombreLibro>.<ext>
		|--- PresentacionesDeClase
				|--- PresentacionUnidad<N>.<ext>
		|--- Resumenes
				|--- ResumenUnidad<N>.<ext>
		|--- LinksClasesGrabadasTeorico.<ext>
|--- Práctico 
		|--- TrabajosPracticos
				|--- TP<N>
					  |--- TP<N>Consignas.<ext>
					  |--- TP<N>Resolucion.<ext>
					  |--- TP<N>Correcciones.<ext>
		|--- ActividadesClase
					|--- Actividades<N>
					  |--- Actividad<N>Consignas.<ext>
					  |--- Actividad<N>Resolucion.<ext>
		|--- TrabajosResueltos
				|--- TPResueltos<N>
					  |--- TPResuelto<N>Consignas.<ext>
					  |--- TPResuelto<N>Resolucion.<ext>
		|--- LinksClasesGrabadasPractico.<ext>
```


## Ítems de configuración

**Esquema de nomenclatura de archivos**

```
<descripción>-<versión>.<extension>
```

| Items de Configuracion                       | Tipo               | Nombre                              | Ubicacion |
| -------------------------------------------- | ------------------ | ----------------------------------- | --------- |
| Plan de gestión de configuración de software | Proyecto           | `README.MD`                         | README.md |
| Planificación                                | InformacionGeneral | `Planificacion_ISC_4K4_2025.<ext>`  |           |
| Cronograma                                   | InformacionGeneral | `Programa_ICS_4K4_2025.<ext>`       |           |
| Libros                                       | Teorico            | `<NombreLibro>.<ext>`               |           |
| Presentación de clases                       | Teorico            | ` PresentacionUnidad<N>.<ext>`      |           |
| Resúmenes de Unidades                        | Teorico            | `ResumenUnidad<N>.<ext>`            |           |
| Links a clases grabadas Teórico              | Teórico            | `LinksClasesGrabadasTeorico.<ext>`  |           |
| Links a clases grabadas Práctico             | Práctico           | `LinksClasesGrabadasPractico.<ext>` |           |
| Trabajo Practico Consignas                   | Práctico           | `TP<N>Consignas.<ext>`              |           |
| Trabajo Practico Resolucion                  | Práctico           | `TP<N>Resolucion.<ext>`             |           |
| Trabajo Practico Correcciónes                | Práctico           | `TP<N>Correcciones.<ext>`           |           |
| Actividades Consignas                        | Práctico           | `Actividad<N>Consignas.<ext>`       |           |
| Actividades resolucion                       | Práctico           | `Actividad<N>Resolucion.<ext>`      |           |
| Trabajos Practicos Resuelto Consignas        | Práctico           | `TPResuelto<N>Consignas.<ext>`      |           |
| Trabajo Practico Resuelto Resolucion         | Práctico           | `TPResuelto<N>Resolucion.<ext>`     |           |
| Links Clases Grabadas Practico               | Práctico           | `LinksClasesGrabadasPractico`       |           |

---

## Glosario

| Palabra | Significado                                     | Ejemplos                         |
| ------- | ----------------------------------------------- | -------------------------------- |
| ISW     | Abreviacion de Ingeniería y calidad de software | `Planificacion_ISC_4K4_2025.pdf` |
|         |                                                 |                                  |


## Criterios de establecimiento de Linea base
Luego de cada entrega de una corrección de un trabajo practico, se procederá a establecer una versión de la Línea base



## Esquema de Nomenclaturas para trabajar 

### Archivos
**Esquema de nomenclatura de archivos**

```
<Descripción>_<Numero>.<extension>
```

### Commits
**Esquema de nomenclatura de commits**
```
<tipo>(alcance): mensaje breve
```

Tipos: `feat`, `fix`, `docs`, `style`, `refactor`

### Ramas 
**Git Flow**

```
main -> estable
feature/<nombre>  -> Nuevas Funcionalidades
fix/<nombre> -> Fixes 
```

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
