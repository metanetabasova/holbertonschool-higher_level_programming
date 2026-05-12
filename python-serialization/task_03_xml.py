#!/usr/bin/python3
'''
Bu modul XML formatinda seriyalasdirma ve deserilizasiya 
funksiyalarini ehtiva edir.
'''
import xml.etree.ElementTree as etree


def serialize_to_xml(dictionary, filename):
    '''
    Python lugeti XML formatinda seriyalasdirir ve fayla yazir
    '''
    # Kok element yaradiriq <data>
    root = ET.Element("data")

    # Lugetin her bir acar-deyer cutunu alt element kimi elave edirik
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    # XML agacini yaradiriq ve fayla yaziriq
    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    '''
    XML faylini oxuyur ve onu Python lugetine cevirir.
    '''
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        # XML elementlerinden lugeti berpa edirik
        # Qeyd: XML-de her sey metn oldugu ucun butun deyerler string kimi qayidir
        return {child.tag: child.text for child in root}

    except FileNotFoundError:
        return None
