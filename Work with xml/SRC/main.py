from asyncore import read
from cgitb import reset
import base64
from traceback import print_tb
from unittest import result
import zlib
from base64 import encode
from multiprocessing.sharedctypes import Value
from xml.dom import minidom
import os
import pandas as pd
import xml.etree.ElementTree as ET
from lxml import etree as et
from datetime import datetime
date_time = datetime.now().date()




#---------------------------Parse XML --------------------------------------------------#

tree = ET.parse('C:\\Users\\a.cuko\\Desktop\\DOOR\\XML\\.xml')
root = tree.getroot()
DEST_FILE_NAME = "C:\\Users\\a.cuko\\Desktop\\DOOR\\XMLparser\\decompresed.xml"




for child in root.iter('Order'):                                  # Get elemet`s from .XML that will be used to create our output.xml
    _ = child.attrib
    customer_name = (_.get('FromContactID'))

for child in root.iter('Order'):                                  # Get elemet`s from .XML that will be used to create our output.xml
    _ = child.attrib
    ship_order = (_.get('MfgShipToAddressID'))


def translate_to_file():                                          # Decode base64 to XML
   for child in root.iter('OrderDetail'):
       child.get('ParentLineID')
       result = zlib.decompress(base64.b64decode(child.text), 16 + zlib.MAX_WBITS).decode('utf-8') 
       with open(DEST_FILE_NAME, "w") as file:
         file.write(result)


def read_file():
    with open(DEST_FILE_NAME) as file:
        return file.readlines()


def clean_file(lines):
    with open(DEST_FILE_NAME, 'w') as file:
        lines = filter(lambda x: x.strip(), lines)
        file.writelines(lines)

#---------------------------------- Buil Ouptut.xml---------------------------------------#

def create_xml(): 

    count = 1
    data = open(DEST_FILE_NAME, 'r')
    count = 1

    lines = ''
    
    while True:
         line = data.readline()
         if not line:
             break   
         lines += line
    #     # if count == 5180:
    #     #     print(line)
         count += 1
        
    
    options = []
    tree2 = ET.ElementTree(ET.fromstring(lines))
    root2 = tree2.getroot()

    # tree2 = ET.parse(DEST_FILE_NAME)
    # root2 = tree2.getroot()
    for child in root2.iter('Detail'):
            all_element = child.attrib 
            value = (all_element.get('DetailValue'))
            subvalue = ':'                 
            if subvalue in value:                                                                 
                value = (all_element.get('DetailValue')) .partition(': ')[2]  
            else:
                value = (all_element.get('DetailValue')) 
            name = all_element.get('Description')                                                
            subname = '+'
            if subname in name:                                                                   
                name = all_element.get('Description').partition('+ ')[2]
            else: 
                name = all_element.get('Description')  
            items = {}                                                                             
            items['name'] = name
            items['value'] = value
            options.append(items)
                                                                                                                                                               
    my_data = [key for key in options if key['name'] != '' and key['value'] != ''] 
    df = pd.DataFrame(my_data)                                                                 
    
    root_xml = et.Element('friedman')                                                                                                    
    element = et.SubElement(root_xml, 'header')                                           
    child = et.SubElement(element, 'source-system')                                                         
    child.text = str('NBP')                                                              
    second_element = et.SubElement(root_xml, 'header')                                             
    child_second_element = et.SubElement(second_element, 'order-request') 
    child3 = et.SubElement(child_second_element, 'ship-to-customer')
    Order_number_ship = et.SubElement(child_second_element, 'ship-to-purchase-order-number')
    Order_number_sold = et.SubElement(child_second_element, 'sold-to-purchase-order-number')
    Order_number_ship.text = str(ship_order)
    number = et.SubElement(child3, 'number')                                       
    division = et.SubElement(child3, 'division')
    email = et.SubElement(child3, 'email')
    password = et.SubElement(child3, 'password')
    number.text = str(customer_name)                                               
    division.text = str('01')
    email.text = number.text + "@nbpmail.com"                                      
    password.text = str('LETMEIN')                                                  
    required_date = et.SubElement(child_second_element, 'required-date')             
    order_date = et.SubElement(child_second_element, 'order-date')
    required_date.text = str(date_time)
    order_date.text = str(date_time)
    child5 = et.SubElement(child_second_element, 'item-groups')
    itrem_group = et.SubElement(child5, 'item-group')
    items = et.SubElement(itrem_group, 'items', type = 'array')
    item = et.SubElement(items, 'item')
    for row in df.iterrows(): 
        element = et.SubElement(item, 'option')                                            
        child = et.SubElement(element, 'name')                                                    
        child2 = et.SubElement(element, 'value')                                       
        child.text = str(row[1]['name'])                                                        
        child2.text = str(row[1]['value'])     
    
    a_xml = et.tostring(root_xml ,pretty_print = True, encoding='UTF-8', xml_declaration=True)                                           
    with open("C:\\Users\\a.cuko\\Desktop\\DOOR\\XMLparser\\output.xml", 'wb') as f:
        f.write(a_xml)                                                                                  

#------------------------ functions Sequence ---------------------------------------------#



def main():
     translate_to_file()
     lines = read_file()
     clean_file(lines)
     create_xml()

if __name__ == "__main__":
    main()


#___________________________________ Writen by: Ardit Cuko _______________________________________#



