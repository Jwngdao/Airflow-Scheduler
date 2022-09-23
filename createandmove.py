import datetime as dt

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
#from airflow.operators.python_operator import PythonOperator

default_args = {
    'owner': 'admin',
    'start_date': dt.datetime(2022, 8, 30),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=5),
}


with DAG('createtextfileandmove',
         default_args=default_args,
         schedule_interval='*/10 * * * *',
         ) as dag:

    create_text_file = BashOperator(task_id='create_text_file',
                               bash_command='touch /usr/Example1/hello.txt')
    move_text_file= BashOperator(task_id='move_text_file',
                               bash_command='mv /usr/Example1/hello.txt ~/Example2/')



create_text_file >> move_text_file

