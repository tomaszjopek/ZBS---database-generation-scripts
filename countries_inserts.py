import csv
from string import Template


def generate():
    template = Template(
        "INSERT INTO COUNTRIES (COUNTRY_ID,COUNTRY_NAME,REGION_ID) values ('$country_code','$country', $regionId);")
    inserts = []

    with open('csvs/GeoLite2-City-Locations-en.csv', newline='', encoding='utf-8') as csvfile:
        spamreader = csv.DictReader(csvfile)
        for row in spamreader:
            if str(row['continent_name']).__contains__('Europe'):
                inserts.append(
                    template.substitute(country_code=row['country_iso_code'], country=row['country_name'], regionId=1))
            elif str(row['continent_name']).__contains__('Asia'):
                inserts.append(
                    template.substitute(country_code=row['country_iso_code'], country=row['country_name'], regionId=3))
            elif str(row['continent_name']).__contains__('America'):
                inserts.append(
                    template.substitute(country_code=row['country_iso_code'], country=row['country_name'], regionId=2))
            else:
                inserts.append(
                    template.substitute(country_code=row['country_iso_code'], country=row['country_name'], regionId=4))

    distinct_inserts = list(set(inserts))

    inserts_file = open('result_scripts/countries.sql', 'w', encoding='utf-8')
    inserts_file.writelines('\n'.join(distinct_inserts))
    inserts_file.close()
