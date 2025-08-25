from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import table_insertion

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="daily_dag",
    default_args=default_args,
    description="Daily DAG running custom script",
    schedule_interval="@daily",
    start_date=datetime(2025, 8, 20),
    catchup=False,
    tags=["example"],
) as dag:

    task1 = PythonOperator(
        task_id="data_fetch",
        python_callable=table_insertion.insert_stock,
    )
