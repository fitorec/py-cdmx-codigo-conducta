# Código de Conducta — Comunidad Python CDMX

```
 --..,_                     _,.--.
    `'.'.  CÓDIGO  DE    .'`__ o  `;__.
       '.'.            .'.'`  '---'`  `
         '.`'--....--'`.'
           `'--....--'`    CONDUCTA
````

Este repositorio contiene el **Código de Conducta** de la comunidad **Python Ciudad de México** en formato **SVG editable**.

El propósito de este repositorio es:

- Promover una cultura de respeto e inclusión en los espacios de la comunidad.
- Proveer una versión editable y visual del código en formato SVG.
- Facilitar la exportación del SVG a PNG mediante un script Python.

## Archivos

- `codigo_de_conducta.svg`: Imagen vectorial del código de conducta (editable).
- `svg2png.py`: Script para convertir el SVG en un archivo PNG.
- `requirements.txt`: Lista de dependencias para ejecutar el script.
- `GNUmakefile`: Permite generar la imagen y borrarla desde objetivos del make.
- `LICENSE`: Licencia del repositorio (Creative Commons).
- `README.md`: Este archivo.

## Requisitos

Este proyecto requiere **Python 3.7+** y la biblioteca [CairoSVG](https://cairosvg.org/).

### Instalación

```bash
pip install -r requirements.txt
```

> ⚠️ En Linux podrías necesitar paquetes del sistema:
>
> ```bash
> sudo apt install libcairo2 libpango-1.0-0 libgdk-pixbuf2.0-0 libffi-dev
> ```

### 🛠 Uso con Makefile

Este repositorio incluye un `Makefile` que automatiza la creación del entorno virtual, instalación de dependencias y generación de la imagen PNG.

#### Comandos disponibles:

```bash
make         # Ejecuta el objetivo 'build': crea entorno virtual, instala dependencias y genera codigo_de_conducta.png
make build   # Igual que 'make'
make clean   # Elimina el archivo generado codigo_de_conducta.png
```

## Uso del script

Para convertir el archivo SVG a PNG:

```bash
python svg2png.py -i codigo_de_conducta.svg -o salida.png
```

Parámetros:

* `-i`, `--input`: Ruta al archivo SVG de entrada.
* `-o`, `--output`: Ruta del archivo PNG de salida.

## Contribuciones

Este repositorio está abierto a mejoras visuales, traducciones o adaptaciones del
código de conducta para otras comunidades.

¡Tu contribución es bienvenida!
