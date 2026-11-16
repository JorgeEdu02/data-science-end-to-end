FROM python:3.11-slim
WORKDIR /app
COPY psets/proyecto/servicio/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt
COPY psets/proyecto/modelado/pipeline_proyecto.py /app/modelado/pipeline_proyecto.py
COPY psets/proyecto/servicio/api.py /app/servicio/api.py
COPY psets/proyecto/servicio/modelo.joblib /app/servicio/modelo.joblib
COPY psets/proyecto/servicio/modelo_version.txt /app/servicio/modelo_version.txt
RUN mkdir -p /app/monitoreo
ENV RUTA_REGISTRO=/app/monitoreo/predicciones.jsonl
EXPOSE 8000
CMD ["uvicorn", "servicio.api:app", "--host", "0.0.0.0", "--port", "8000"]
