# Imagen base optimizada para Python 3.12 (Sección 1.9)
FROM python:3.12-slim

# Instalación de dependencias de sistema mínimas para Poetry y compilación si es necesario
RUN apt-get update && apt-get install -y \
    curl \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Instalación de Poetry (Sección 1.11)
ENV POETRY_VERSION=1.7.1
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"

WORKDIR /app

# Copia de archivos de configuración de Poetry
COPY pyproject.toml poetry.lock* ./

# Instalación de dependencias sin crear entorno virtual (optimización para contenedor)
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --no-root

# Copia de la lógica del microservicio
COPY . .

# Exposición del puerto estándar para Cloud Run (Sección 1.13)
EXPOSE 8080

# Usuario no raíz por seguridad (Sección 1.14 / Mejores Prácticas)
RUN useradd -m appuser && chown -R appuser /app
USER appuser

# Comando de arranque (Sección 1.10)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
