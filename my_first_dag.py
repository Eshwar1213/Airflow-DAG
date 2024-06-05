from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator


default_args = {
    'owner': 'Eshwar',
    'retries' : 5,
    'retry_delay' : timedelta(minutes=2)
}


with DAG(
    dag_id= "my_first_dag",
    default_args = default_args,
    description="This is my first day",
    start_date= datetime(2024,6,5,2),
    schedule_interval='@daily',
) as dag:
    task1 = BashOperator(
        task_id='first_task',
        bash_command = 'echo hello word, this is my first dag!'
    )

task1