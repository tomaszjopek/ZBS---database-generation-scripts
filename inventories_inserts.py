import random
from string import Template


def generate():
    template = Template(
        "Insert into INVENTORIES (PRODUCT_ID,WAREHOUSE_ID,QUANTITY) values ($id, $warehouse_id, '$quantity');")
    inserts = []

    for warehouse in range(0, 15000):
        inserts.append(template.substitute(id=random.randint(0, 5000), warehouse_id=random.randint(0, 12902),
                                           quantity=random.randint(0, 250)))

    distinct_inserts = list(set(inserts))

    inserts_file = open('result_scripts/inventories_inserts.sql', 'w', encoding='utf-8')
    inserts_file.writelines('\n'.join(distinct_inserts))
    inserts_file.close()


generate()
