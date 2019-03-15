import csv
import random
from string import Template


def generate():
    counter = 3698
    inserts = []

    template = Template(
        "Insert into PRODUCTS (PRODUCT_ID,PRODUCT_NAME,DESCRIPTION,STANDARD_COST,LIST_PRICE,CATEGORY_ID) values ($id,'$product_name','$description', '$standard_cost', '$list_price', '$category_id');")

    with open('csvs/Intel_CPUs.csv', newline='', encoding='utf-8') as csvfile:
        spamreader = csv.DictReader(csvfile)
        for row in spamreader:
            name = f"{row['Product_Collection']} {row['Vertical_Segment']} {row['Processor_Number']}"
            name = name.replace("'", '')
            desc = row['Status'] + row['Launch_Date'] + row['Lithography'] + row['Recommended_Customer_Price'] + row[
                'nb_of_Cores'] + row['nb_of_Threads'] + row['Processor_Base_Frequency'] + row['Max_Turbo_Frequency'] + row[
                       'Cache'] + row['Bus_Speed'] + row['TDP'] + row['Embedded_Options_Available'] + row[
                       'Conflict_Free'] + row['Max_Memory_Size'] + row['Memory_Types']
            desc = desc.replace(',', '')
            desc = desc.replace('(', '')
            desc = desc.replace(')', '')
            desc = desc.replace("'", '')
            inserts.append(template.substitute(id=counter, product_name=name, description=desc,
                                               standard_cost=random.randint(300, 3000),
                                               list_price=random.randint(400, 4000), category_id=1))
            counter = counter + 1

    distinct_inserts = list(set(inserts))

    inserts_file = open('result_scripts/cpu_products.sql', 'w', encoding='utf-8')
    inserts_file.writelines('\n'.join(distinct_inserts))
    inserts_file.close()


generate()
