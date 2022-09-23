import datetime as dt

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
#from airflow.operators.python_operator import PythonOperator

default_args = {
    'owner': 'admin',
    'start_date': dt.datetime(2022, 8, 25),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=5),
}


with DAG('attendancedetails',
         default_args=default_args,
         schedule_interval='00 10 * * *',
         ) as dag:

    attendancedetails = BashOperator(task_id='attendancedetails',
                               bash_command='java -jar /usr/local/jarfiles/AttendanceDetails.jar >>/home/trscadmin/javaattendance.log')


attendancedetails

