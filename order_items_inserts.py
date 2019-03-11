import random
from string import Template


def generate():
    template = Template(
        "Insert into ORDER_ITEMS (ORDER_ID,ITEM_ID,PRODUCT_ID,QUANTITY,UNIT_PRICE) values ($order_id, $item_id, $product_id, $quantity, $unit_price);")
    inserts = []
    counter = 666

    for warehouse in range(0, 5000):
        inserts.append(
            template.substitute(order_id=random.randint(0, 5001), item_id=counter, product_id=random.randint(0, 3694),
                                quantity=random.randint(0, 200), unit_price=round(random.uniform(150.20, 3694.22), 2)))
        counter = counter + 1

    distinct_inserts = list(set(inserts))

    inserts_file = open('result_scripts/order_items_inserts.sql', 'w', encoding='utf-8')
    inserts_file.writelines('\n'.join(distinct_inserts))
    inserts_file.close()
