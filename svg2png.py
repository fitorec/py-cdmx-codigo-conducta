#!/usr/bin/env python3

import argparse
import os
import sys
import cairosvg

def convertir_svg_a_png(archivo_entrada, archivo_salida):
    try:
        cairosvg.svg2png(url=archivo_entrada, write_to=archivo_salida)
        print(f"[✓] Imagen generada: {archivo_salida}")
    except Exception as e:
        print(f"[✗] Error al convertir SVG a PNG: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(
        description="Convierte un archivo SVG en PNG usando CairoSVG."
    )
    parser.add_argument(
        "-i", "--input", required=True, help="Ruta del archivo SVG de entrada."
    )
    parser.add_argument(
        "-o", "--output", required=True, help="Ruta del archivo PNG de salida."
    )

    args = parser.parse_args()

    if not os.path.isfile(args.input):
        print(f"[✗] El archivo de entrada no existe: {args.input}")
        sys.exit(1)

    convertir_svg_a_png(args.input, args.output)

if __name__ == "__main__":
    main()
