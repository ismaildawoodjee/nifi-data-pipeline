# for scheduling the Airflow DAG
from datetime import datetime, timedelta

# for building the DAG and using operators
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator

# import Python modules (my own modules) from `sourcefiles` folder
from sourcefiles import csv_to_json as c2j

# DAG arguments
default_args = {
    "owner": "airflow",
    "depends_on_past": True,
    "wait_for_downstream": True,
    "start_date": datetime.now(),
    "email": ["airflow@airflow.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 0,
    "retry_delay": timedelta(minutes=1),
}

with DAG(
    dag_id="csv_to_json_pipeline",
    default_args=default_args,
    schedule_interval=timedelta(minutes=10),
) as dag:

    print_starting = BashOperator(
        task_id="starting",
        bash_command='echo "Generating fake data in CSV and dumping to JSON"',
    )

    generate_data = PythonOperator(
        task_id="generate_fake_data",
        python_callable=c2j.generate_fake_data,
    )

    csv_to_json_task = PythonOperator(
        task_id="convert_csv_to_json",
        python_callable=c2j.convert_csv_to_json,
    )

    end_of_pipeline = DummyOperator(task_id="end_of_pipeline")

    generate_data >> print_starting >> csv_to_json_task >> end_of_pipeline
