#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file creates and exports a XML-File
import xml.etree.ElementTree as ET # Import the package

# create the file structure
# Define the root element
data = ET.Element('empresa')
# Add 1 element (tag) called 'data'    
items = ET.SubElement(data, 'empleados')
# Add 2 element called 'empleado'
item1 = ET.SubElement(items, 'empleado')
item2 = ET.SubElement(items, 'empleado')
# Add an attribute 'id' 
item1.set('id','1')
item2.set('id','2')
# Add a value to the tag 'empleado'
item1.text = 'María'
item2.text = 'Juan'

# create a new XML file with the results
#Convert all to a string
mydata = ET.tostring(data).decode('utf-8')
#Open the file to write on
myfile = open("empresa.xml", "w")
#Write the file
myfile.write(mydata)
