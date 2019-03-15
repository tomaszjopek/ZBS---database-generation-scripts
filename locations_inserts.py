import csv
from string import Template


def generate():
    template = Template(
        "Insert into LOCATIONS (LOCATION_ID,ADDRESS,POSTAL_CODE,CITY,STATE,COUNTRY_ID,LAT,LNG,POPULATION) values ($id,null,null,'$city',null,'$country_code',$lat,$lng,$population);")
    inserts = []
    counter = 1

    with open('csvs/worldcities.csv', newline='', encoding='utf-8') as csvfile:
        spamreader = csv.DictReader(csvfile)
        for row in spamreader:
            inserts.append(
                template.substitute(id=counter, city=str(row['city']).replace("'", "''"), country_code=row['iso2'],
                                    lat=row['lat'], lng=row['lng'], population=row['population']))
            counter = counter + 1

    distinct_inserts = list(set(inserts))

    inserts_file = open('result_scripts/locations.sql', 'w', encoding='utf-8')
    inserts_file.writelines('\n'.join(distinct_inserts))
    inserts_file.close()

generate()