import random
from string import Template
from random import randrange
from datetime import timedelta
import datetime
import calendar


def generate():
    template = Template(
        "Insert into ORDERS (ORDER_ID,CUSTOMER_ID,STATUS,SALESMAN_ID,ORDER_DATE) values ($order_id, $customer_id, '$status', $salesman_id, $order_date);")
    inserts = []
    counter = 105
    status = ['Shipped', 'Pending', 'Canceled']

    def random_date(start, end):
        delta = end - start
        int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
        random_second = randrange(int_delta)
        return start + timedelta(seconds=random_second)

    startDate = datetime.datetime(1995, 1, 1)
    endDate = datetime.datetime.now()

    for warehouse in range(0, 5000):
        tmp_date = random_date(startDate, endDate)
        # tmp_month = calendar.month_abbr[tmp_date.month]
        # tmp_month = tmp_month.__str__()[:3]
        tmp_month = tmp_date.month.__str__()
        tmp_day = tmp_date.day.__str__()
        tmp_year = tmp_date.year.__str__()

        dates = "to_date('" + tmp_year + '-' + tmp_month + '-' + tmp_day + "', 'YYYY-MM-DD' )"

        inserts.append(template.substitute(order_id=counter, customer_id=random.randint(0, 319),
                                           status=status[random.randint(0, 2)], salesman_id=random.randint(0, 4907),
                                           order_date=dates))
        counter = counter + 1

    distinct_inserts = list(set(inserts))

    inserts_file = open('result_scripts/orders_inserts.sql', 'w', encoding='utf-8')
    inserts_file.writelines('\n'.join(distinct_inserts))
    inserts_file.close()


generate()