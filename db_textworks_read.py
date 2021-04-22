# file db_textworks_read.py
# Reads DB/TextWorks XML and assigns values to equivalent EAD tag in record_object dictionary

import xml.etree.cElementTree as ET

def populate_record_object(my_xml):
    record_object = build_empty_record_object()

    # tree = ET.ElementTree(open(input('Please enter the name of a DB/TextWorks XML file to convert: ')))
    tree = ET.parse(my_xml)
    root = tree.getroot()

    for record in root.iter():
        # print(record.tag)
        # print(record.text)
        if record.tag == '{inm}recordid':
            record_object['recordid'] = record.text
        elif record.tag  == '{inm}':
            record_object['filedesc'] = record.text
        elif record.tag  == '{inm}':
            record_object['maintenanceagency'] = record.text
        elif record.tag  == '{inm}':
            record_object['maintenancestatus'] = record.text
        elif record.tag  == '{inm}':
            record_object['maintenancehistory'] = record.text
        elif record.tag  == '{inm}':
            record_object['repository'] = record.text
        elif record.tag  == '{inm}':
            record_object['repository_persname'] = record.text
        elif record.tag  == '{inm}':
            record_object['repository_famname'] = record.text
        elif record.tag  == '{inm}':
            record_object['repository_corpname'] = record.text
        elif record.tag  == '{inm}':
            record_object['repository_name'] = record.text
        elif record.tag  == '{inm}':
            record_object['origination_persname'] = record.text
        elif record.tag  == '{inm}':
            record_object['origination_famname'] = record.text
        elif record.tag  == '{inm}':
            record_object['origination_corpname'] = record.text
        elif record.tag  == '{inm}':
            record_object['origination_name'] = record.text
        elif record.tag  == '{inm}':
            record_object['unittile'] = record.text
        elif record.tag  == '{inm}':
            record_object['unitid'] = record.text
        elif record.tag  == '{inm}':
            record_object['unitdatestructured'] = record.text
        elif record.tag == '{inm}':
            record_object['daterange'] = record.text
        elif record.tag == '{inm}':
            record_object['dateset'] = record.text
        elif record.tag == '{inm}':
            record_object['fromdate'] = record.text
        elif record.tag == '{inm}':
            record_object['todate'] = record.text
        elif record.tag == '{inm}':
            record_object['datesingle'] = record.text
        elif record.tag == '{inm}':
            record_object['physdecstructured'] = record.text
        elif record.tag == '{inm}':
            record_object['physdecstructured_coverage'] = record.text
        elif record.tag == '{inm}':
            record_object['physdecstructured_type'] = record.text
        elif record.tag == '{inm}':
            record_object['physdescstructuredtype_coverage'] = record.text
        elif record.tag == '{inm}':
            record_object['physdescstructuredtype_unittype'] = record.text
        elif record.tag == '{inm}':
            record_object['quantity'] = record.text
        elif record.tag == '{inm}':
            record_object['unittype'] = record.text
        elif record.tag == '{inm}':
            record_object['langmaterial'] = record.text
        elif record.tag == '{inm}':
            record_object['language'] = record.text
        elif record.tag == '{inm}':
            record_object['accessrestrict'] = record.text
        elif record.tag == '{inm}':
            record_object['userestrict'] = record.text
        elif record.tag == '{inm}':
            record_object['scopecontent'] = record.text
        else:
            record.text = None

        # Attributes
        # elif record.tag == '{inm}':
        #     record_object['maintenancehistory_attr_countrycode'] = record.text

    #print(record_object)
    return record_object

def build_empty_record_object():
        record_list = ['recordid',
                       'filedesc',
                       'maintenanceagency',
                       'maintenancestatus',
                       'maintenancehistory',
                       'repository',
                       'repository_persname',
                       'repository_famname',
                       'repository_corpname',
                       'repository_name',
                       'origination_persname',
                       'origination_famname',
                       'origination_corpname',
                       'origination_name',
                       'unittile',
                       'unitid',
                       'unitdatestructured',
                       'daterange',
                       'dateset',
                       'fromdate',
                       'todate',
                       'datesingle',
                       'physdecstructured',
                       'physdecstructured_coverage',
                       'physdecstructured_type',
                       'physdescstructuredtype_coverage',
                       'physdescstructuredtype_unittype',
                       'quantity',
                       'unittype',
                       'langmaterial',
                       'language',
                       'accessrestrict',
                       'userestrict',
                       'scopecontent',
                       'maintenancehistory_attr_countrycode'
                       ]
        record_object = dict(zip(record_list, [None] * len(record_list)))
        return record_object

if __name__ == "__main__":
    populate_record_object()

