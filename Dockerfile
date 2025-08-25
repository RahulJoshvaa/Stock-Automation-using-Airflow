FROM apache/airflow:2.9.0

# Switch to airflow user to install packages (recommended)
USER airflow

# Install Python dependencies
RUN pip install --no-cache-dir requests psycopg2-binary python-dotenv
