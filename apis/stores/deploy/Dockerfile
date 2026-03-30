FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PORT 8080

WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc \
    && pip install --no-cache-dir poetry \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy poetry files
COPY pyproject.toml poetry.lock ./

# Install dependencies (no virtual environment needed inside container)
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --only main --no-root

# Copy project files
COPY . .

# Expose port
EXPOSE 8080

# Command to run the FastMCP / FastAPI server. Assuming standard Uvicorn run mapping.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
