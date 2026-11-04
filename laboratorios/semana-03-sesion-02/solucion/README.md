# Semana 3, sesión 2 — Infraestructura como código

**Pregunta previa 1:** definir servicios en archivos versionados permite solicitar/aplicar cambios mediante revisión de código y automatización, en vez de aprovisionamiento manual sin reproducibilidad.

**Pregunta previa 2:** Compose ya es una forma declarativa de infraestructura local, pero Terraform añade archivo de estado de recursos, separación explícita entre plan y apply, y proveedores para recursos más allá de contenedores.

**Volúmenes:** sin un volumen persistente, los datos guardados dentro de un contenedor eliminado se pierden (simplemente detener y volver a arrancar el mismo contenedor no los borra).

**Host dentro de pgAdmin:** `pg-database`, nombre del servicio en la red Docker, no `localhost`.

**depends_on:** organiza el arranque, no garantiza que Postgres esté listo para conexiones; se necesita comprobación de salud o reintentos de la ingesta.

**Terraform:** si un contenedor creado bajo Terraform cambia fuera de Terraform, `terraform plan` detecta drift según el recurso y proveedor y puede proponer cambios; no corrige por sí solo hasta `apply`.

## Archivos solucionados
- `docker-compose.yml`: Postgres, pgAdmin y script de ingesta.
- `terraform/main.tf`: los mismos tres contenedores, red y volumen.

## Para ejecutar
Los archivos `Dockerfile`, `ingest_data.py` y `requirements.txt` del starter se copian al lado del compose; están igualmente incluidos en esta solución.

```bash
cd laboratorios/semana-03-sesion-02/solucion
docker compose up --build
# revisar en pgAdmin puerto 8085 y ejecutar SELECT mes_origen, COUNT(*) FROM viajes_taxi GROUP BY mes_origen ORDER BY mes_origen;
docker compose down -v
cd terraform
terraform init
terraform plan
terraform apply
```

El script ingiere tres meses de datos externos de taxis de Nueva York; **no se ha ejecutado** la descarga de 2023 ni se han verificado conteos de Postgres aquí. El enunciado describe una meta de 300.000 viajes por mes; esa cantidad no puede reportarse como resultado observado sin ejecutar la ingesta.

**Importante:** `docker compose down -v` destruye el volumen y sus datos; no debe usarse sobre un entorno con datos valiosos.
