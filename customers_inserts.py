from string import Template
from mimesis import Person
from mimesis import Address
from mimesis import Business
from mimesis import Internet
import random
from random import randrange
from datetime import timedelta
import datetime

template = Template(
    "Insert into CUSTOMERS (CUSTOMER_ID,NAME,ADDRESS,CREDIT_LIMIT,WEBSITE) "
    "values ($id,'$name','$address',$credit,'$website');")


def generate():
    inserts = []
    counter = 350

    business = Business('en')
    address = Address('en')
    internet = Internet('en')

    for index in range(counter, 15000, 1):
        inserts.append(template.substitute(id=index,
                                           name=business.company().replace("'", "''"),
                                           address=address.address().replace("'", "''"),
                                           credit=random.randint(300, 1000000),
                                           website=internet.home_page().replace("'", "''")
                                           ))

    inserts_file = open('result_scripts/customers.sql', 'w', encoding='utf-8')
    inserts_file.writelines('\n'.join(inserts))
    inserts_file.close()


generate()
