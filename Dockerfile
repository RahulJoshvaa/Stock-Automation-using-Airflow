FROM apache/airflow:2.9.0

#extending the predefined image to install required dependencies 
#we will be building this in yml file
USER airflow

RUN pip install --no-cache-dir requests psycopg2-binary python-dotenv
