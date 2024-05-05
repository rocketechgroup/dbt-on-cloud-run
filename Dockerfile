# Use Python 3.11 as the base image
FROM python:3.11

# Install Poetry
RUN pip install poetry

# Create a new user and switch to that user
RUN useradd -m dbtuser
USER dbtuser

# Set the working directory in the Docker container
WORKDIR /app

# Copy the project files into the Docker container
COPY --chown=dbtuser:dbtuser . /app

# Install the project dependencies
RUN poetry install --only main --no-root

WORKDIR /app/dbt

# Set the command to run when the Docker container starts
CMD ["poetry", "run", "dbt", "run"]