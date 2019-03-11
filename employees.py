import csv
from string import Template
from mimesis.providers import Person
import random
from random import randrange
from datetime import timedelta
import datetime
import calendar


def generate():
    def random_date(start, end):
        delta = end - start
        int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
        random_second = randrange(int_delta)
        return start + timedelta(seconds=random_second)

    startDate = datetime.datetime(1995, 1, 1)
    endDate = datetime.datetime.now()

    # to_date('07-JUN-16','DD-MON-RR')

    template = Template(
        "Insert into EMPLOYEES (EMPLOYEE_ID,FIRST_NAME,LAST_NAME,EMAIL,PHONE,HIRE_DATE,MANAGER_ID,JOB_TITLE)"
        " values ($EMPLOYEE_ID,'$FIRST_NAME','$LAST_NAME','$EMAIL','$PHONE','$HIRE_DATE',$MANAGER_ID,'$JOB_TITLE');")
    inserts = []
    counter = 200
    job_titles = ['Stock Clerk', 'Accountant', 'Sales Manager', 'Sales Representative', 'Shipping Clerk']
    initial_managers = [48]

    person = Person('en')

    for index in range(counter, 5000, 1):
        tmp_job_title = random.choice(job_titles)
        if str(tmp_job_title).__contains__('Manager'):
            initial_managers.append(index)

        tmp_date = random_date(startDate, endDate)
        tmp_month = calendar.month_abbr[tmp_date.month]
        tmp_month = tmp_month.__str__()[:3]
        tmp_day = tmp_date.day.__str__()
        tmp_year = tmp_date.year.__str__()[-2:]

        dates = tmp_day + '-' + tmp_month + '-' + tmp_year

        inserts.append(template.substitute(EMPLOYEE_ID=index,
                                           FIRST_NAME=person.name().replace("'", "''"),
                                           LAST_NAME=person.last_name().replace("'", "''"),
                                           EMAIL=person.email().replace("'", "''"),
                                           PHONE=person.telephone(),
                                           HIRE_DATE=dates,
                                           MANAGER_ID=random.choice(initial_managers),
                                           JOB_TITLE=random.choice(job_titles)
                                           ))

    inserts_file = open('result_scripts/employees.sql', 'w', encoding='utf-8')
    inserts_file.writelines('\n'.join(inserts))
    inserts_file.close()
