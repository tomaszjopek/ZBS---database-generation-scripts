import csv
from string import Template


def generate():
    cities = []
    counter = 1
    inserts = []
    tmp_counter = 1

    template = Template(
        "Insert into WAREHOUSES (WAREHOUSE_ID,WAREHOUSE_NAME,LOCATION_ID) values ($id,'$name',$loc_id);")

    with open('csvs/worldcities.csv', newline='', encoding='utf-8') as csvfile:
        spamreader = csv.DictReader(csvfile)
        for row in spamreader:
            cities.append([counter, str(row['city']).replace("'", "''")])
            counter = counter + 1

    for city in cities:
        inserts.append(template.substitute(id=tmp_counter, name=city[1], loc_id=city[0]))
        tmp_counter = tmp_counter + 1

    distinct_inserts = list(set(inserts))

    inserts_file = open('result_scripts/warehouses.sql', 'w', encoding='utf-8')
    inserts_file.writelines('\n'.join(distinct_inserts))
    inserts_file.close()


generate()
