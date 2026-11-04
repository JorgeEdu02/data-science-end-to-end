# Docker — soluciones

Ejercicio 1: copia `solucion/ejercicio1/Dockerfile` a `starter/ejercicio1/Dockerfile`, entra en `starter/ejercicio1` y ejecuta:

```bash
docker build -t procesar-ventas .
docker run --rm -v "$(pwd)/datos:/app/datos" procesar-ventas
```

Ejercicio 2: copia `solucion/ejercicio2/Dockerfile` a `starter/ejercicio2/Dockerfile`. Construye y corre:

```bash
docker build -t resumir-clientes .
docker run --rm -v "$(pwd)/datos:/app/datos" resumir-clientes
docker run --rm -v "$(pwd)/datos:/app/datos" resumir-clientes python contar_filas.py
bash comprobar.sh
```

`CMD` es el comando por defecto y puede reemplazarse al correr la imagen. Las dependencias se copian antes que el codigo para aprovechar la cache. Sin `-v`, la salida queda dentro del contenedor y no se puede recuperar automaticamente tras eliminarlo.

Ejercicio 3: el Dockerfile de `solucion/proyecto/` es una propuesta para un proyecto con `src/ingesta.py`: requiere ajustar rutas y dependencias reales. No se puede afirmar una verificacion Docker sin correrlo en tu Codespace.
