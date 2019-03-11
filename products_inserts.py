import csv
import random
from string import Template


def generate():
    counter = 289
    inserts = []

    template = Template(
        "Insert into PRODUCTS (PRODUCT_ID,PRODUCT_NAME,DESCRIPTION,STANDARD_COST,LIST_PRICE,CATEGORY_ID) values ($id,'$product_name','$description', '$standard_cost', '$list_price', '$category_id');")

    with open('csvs/All_GPUs.csv', newline='', encoding='utf-8') as csvfile:
        spamreader = csv.DictReader(csvfile)
        for row in spamreader:
            name = row['Name']
            name = name.replace("'", '')
            desc = row['Architecture'] + row['Best_Resolution'] + row['Boost_Clock'] + row['Core_Speed'] + row[
                'DVI_Connection'] + row['Dedicated'] + row['Direct_X'] + row['DisplayPort_Connection'] + row[
                       'HDMI_Connection'] + row['Integrated'] + row['L2_Cache'] + row['Manufacturer'] + row[
                       'Max_Power'] + row['Memory'] + row['Memory_Bandwidth'] + row['Memory_Bus'] + row[
                       'Memory_Speed'] + row['Memory_Type'] + row['Notebook_GPU'] + row['Open_GL'] + row['PSU'] + row[
                       'Pixel_Rate'] + row['Power_Connector'] + row['Process'] + row['ROPs'] + row['Release_Date'] + \
                   row['Resolution_WxH'] + row['SLI_Crossfire'] + row['Shader'] + row['Texture_Rate'] + row[
                       'VGA_Connection']
            desc = desc.replace(',', '')
            desc = desc.replace('(', '')
            desc = desc.replace(')', '')
            desc = desc.replace("'", '')
            inserts.append(template.substitute(id=counter, product_name=name, description=desc,
                                               standard_cost=random.randint(300, 3000),
                                               list_price=random.randint(400, 4000), category_id=2))
            counter = counter + 1

    distinct_inserts = list(set(inserts))

    inserts_file = open('result_scripts/gpu_products.sql', 'w', encoding='utf-8')
    inserts_file.writelines('\n'.join(distinct_inserts))
    inserts_file.close()
