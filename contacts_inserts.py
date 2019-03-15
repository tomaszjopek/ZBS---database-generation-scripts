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
    "Insert into CONTACTS (CONTACT_ID,FIRST_NAME,LAST_NAME,EMAIL,PHONE,CUSTOMER_ID)"
    "values ($id,'$name','$surname','$email','$phone',$customer_id);")


def generate():
    inserts = []
    counter = 330

    person = Person('en')
    business = Business('en')
    address = Address('en')
    internet = Internet('en')

    for index in range(counter, 15000, 1):
        inserts.append(template.substitute(id=index,
                                           name=person.name().replace("'", "''"),
                                           surname=person.surname().replace("'", "''"),
                                           email=person.email().replace("'", "''"),
                                           phone=person.telephone(),
                                           customer_id=random.randint(330, 14999)
                                           ))

    inserts_file = open('result_scripts/contacts.sql', 'w', encoding='utf-8')
    inserts_file.writelines('\n'.join(inserts))
    inserts_file.close()


generate()
