from string import Template
from mimesis import Person
import random
from random import randrange
from datetime import timedelta
import datetime


def generate():
    def random_date(start, end):
        delta = end - start
        int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
        random_second = randrange(int_delta)
        return start + timedelta(seconds=random_second)

    startDate = datetime.datetime(1995, 1, 1)
    endDate = datetime.datetime.now()

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

        inserts.append(template.substitute(EMPLOYEE_ID=index,
                                           FIRST_NAME=person.name().replace("'", "''"),
                                           LAST_NAME=person.last_name().replace("'", "''"),
                                           EMAIL=person.email().replace("'", "''"),
                                           PHONE=person.telephone(),
                                           HIRE_DATE=tmp_date.__str__(),
                                           MANAGER_ID=random.choice(initial_managers),
                                           JOB_TITLE=random.choice(job_titles)
                                           ))

    inserts_file = open('result_scripts/employees.sql', 'w', encoding='utf-8')
    inserts_file.writelines('\n'.join(inserts))
    inserts_file.close()
