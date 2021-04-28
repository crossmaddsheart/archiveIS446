# ead_write.py
# Accepts

import xml.etree.ElementTree as ET
from datetime import date


def generate_ead(record_object):

    today = date.today()
    current_date_standard = str(today.strftime('%Y-%m'))
    current_date_text = str(today.strftime('%b %Y'))

    # record_object = populate_record_object(open(input('Enter the name of a DB/TextWorks XML file to convert: ')))
    # db_textworks_record_object = populate_record_object(open(input('Enter the name of a DB/TextWorks XML file to convert: ')))
    # This is a test record_object dict to use while ironing out EAD XML structure

    control_metadata = {'publicationstmt_addressline': ['600 S. Paulina', 'Chicago, Ill. 60612'],
                        'repository_corpname': ['Rush University Medical Center Archives', 'Chicago, Ill.'],
                        'maintenancehistory_eventdatetime': current_date_text,
                        'maintenancehistory_agent': 'DBT to EAD python script',
                        'maintenancehistory_eventdescription': 'Converted to EAD3 from DB/TextWorks XML export',
                        'maintenanceagency_agencyname': 'Rush University Medical Center Archives',
                        'recordid_attr_audience': 'external',
                        'maintenancestatus_attr_value': 'derived',
                        'maintenancehistory_eventtype_attr_value': 'created',
                        'maintenancehistory_eventdatetime_attr_standarddatetime': current_date_standard,
                        'maintenancehistory_agenttype_attr_value': 'machine',
                        }

    record_object.update(control_metadata)
    #record_object = replace_none_with_empty_str(record_object)

    # Namespace; may not be necessary
    ET.register_namespace('ead', 'http://ead3.archivists.org/schema/')

    # Establish <ead> as root element
    root = ET.Element('ead')
    root.set('xmlns', 'http://ead3.archivists.org/schema/')
    root.set('audience', 'external')

    # Create and populate <control>
    control_element = ET.Element('control')
    root.append(control_element)

    # Write <recordid> and children. <recordid> is a required element.
    recordid_element = ET.SubElement(control_element, 'recordid')
    recordid_element.text = record_object.get('recordid')

    # Write <titlestmt> and children
    if all(value is None for value in [record_object.get('titlestmt_titleproper'),
                                        record_object.get('titlestmt_subtitle'),
                                        record_object.get('titlestmt_author'),
                                        record_object.get('titlestmt_sponsor')]):
        pass
    else:
        filedesc_element = ET.SubElement(control_element, 'filedesc')
        titlestmt_element = ET.SubElement(filedesc_element, 'titlestmt')
    if record_object.get('titlestmt_titleproper') is None:
        pass
    else:
        titlestmt_titleproper_element = ET.SubElement(titlestmt_element, 'titleproper')
        titlestmt_titleproper_element.text = record_object.get('titlestmt_titleproper')
    if record_object.get('titlestmt_subtitle') is None:
        pass
    else:
        titlestmt_subtitle_element = ET.SubElement(titlestmt_element, 'subtitle')
        titlestmt_subtitle_element.text = record_object.get('titlestmt_subtitle')
    if record_object.get('titlestmt_author') is None:
        pass
    else:
        titlestmt_author_element = ET.SubElement(titlestmt_element, 'author')
        titlestmt_author_element.text = record_object.get('titlestmt_author')
    if record_object.get('titlestmt_sponsor') is None:
        pass
    else:
        titlestmt_sponsor_element = ET.SubElement(titlestmt_element, 'sponsor')
        titlestmt_sponsor_element.text = record_object.get('titlestmt_sponsor')

    # Write <publicationstmt> and children
    if all(value is None for value in [record_object.get('publicationstmt_publisher'),
                                       record_object.get('publicationstmt_date'),
                                       record_object.get('publicationstmt_addressline'),
                                       record_object.get('publicationstmt_p'),
                                       record_object.get('publicationstmt_num')]):
        pass
    else:
        publicationstmt_element = ET.SubElement(control_element, 'publicationstmt')
        if record_object.get('publicationstmt_publisher') is None:
            pass
        else:
            publicationstmt_publisher_element = ET.SubElement(publicationstmt_element, 'publisher')
            publicationstmt_publisher_element.text = record_object.get('publicationstmt_publisher')
        if record_object.get('publicationstmt_date') is None:
            pass
        else:
            publicationstmt_date_element = ET.SubElement(publicationstmt_element, 'date')
            publicationstmt_date_element.text = record_object.get('publicationstmt_date')
        if record_object.get('publicationstmt_addressline') is None:
            pass
        else:
            publicationstmt_address_element = ET.SubElement(publicationstmt_element, 'address')
            for line in range(len(record_object.get('publicationstmt_addressline'))):
                publicationstmt_addressline_element = ET.SubElement(publicationstmt_address_element, 'addressline')
                publicationstmt_addressline_element.text = str(record_object.get('publicationstmt_addressline')[line])
        if record_object.get('publicationstmt_p') is None:
            pass
        else:
            publicationstmt_p_element = ET.SubElement(publicationstmt_element, 'p')
            publicationstmt_p_element.text = record_object.get('publicationstmt_p')
        if record_object.get('publicationstmt_num') is None:
            pass
        else:
            publicationstmt_num_element = ET.SubElement(publicationstmt_element, 'num')
            publicationstmt_num_element.text = record_object.get('publicationstmt_num')

    # Write <maintenancestatus>
    maintenancestatus_element = ET.SubElement(control_element, 'maintenancestatus', attrib={})
    maintenancestatus_element.set('value', record_object.get('maintenancestatus_attr_value'))

    # Write <maintenanceagency>
    if all(value is None for value in [record_object.get('maintenanceagency_agencycode'),
                                        record_object.get('maintenanceagency_otheragencycode'),
                                        record_object.get('maintenanceagency_agencyname'),
                                        record_object.get('maintenanceagency_descriptivenote')]):
        pass
    else:
        maintenanceagency_element = ET.SubElement(control_element, 'maintenanceagency')
        maintenanceagency_element.text = record_object.get('maintenanceagency')

    # Write <maintenancehistory> and child <maintenanceevent>
    maintenancehistory_element = ET.SubElement(control_element, 'maintenancehistory')
    maintenanceevent_element = ET.SubElement(maintenancehistory_element, 'maintenanceevent')

    # Write <maintenanceevent> children
    maintenancehistory_eventtype_element = ET.SubElement(maintenanceevent_element, 'eventtype', attrib={})
    maintenancehistory_eventtype_element.set('value', record_object.get('maintenancehistory_eventtype_attr_value'))
    maintenancehistory_eventdatetime_element = ET.SubElement(maintenanceevent_element, 'eventdatetime', attrib={})
    maintenancehistory_eventdatetime_element.set('standarddatetime',
                                                  record_object.get('maintenancehistory_eventdatetime_attr_standarddatetime'))
    maintenancehistory_eventdatetime_element.text = record_object.get('maintenancehistory_eventdatetime_element')
    maintenancehistory_agenttype_element = ET.SubElement(maintenanceevent_element, 'agenttype', attrib={})
    maintenancehistory_agenttype_element.set('value', record_object.get('maintenancehistory_agenttype_attr_value'))
    maintenancehistory_agent_element = ET.SubElement(maintenanceevent_element, 'agent')
    maintenancehistory_agent_element.text = record_object.get('maintenancehistory_agent_element')
    maintenancehistory_eventdescription_element = ET.SubElement(maintenanceevent_element, 'eventdescription')
    maintenancehistory_eventdescription_element.text = record_object.get('maintenancehistory_eventdescription_element')

    # Create <archdesc> element
    archdesc_element = ET.Element('archdesc')
    root.append(archdesc_element)

    # Create <did> element
    did_element = ET.SubElement(archdesc_element, 'did')

    # Create optional <repository> element if data to populate children is present in record_object
    if all(value is None for value in [record_object.get('repository_persname'),
                                        record_object.get('repository_famname'),
                                        record_object.get('repository_corpname'),
                                        record_object.get('repository_name')]):
        pass
    else:
        repository_element = ET.SubElement(did_element, 'repository')
        if record_object.get('repository_persname') is None:
            pass
        else:
            repository_persname_element = ET.SubElement(repository_element, 'persname')
            if type(record_object.get('repository_persname')) is list:
                for part in range(len(record_object.get('repository_persname'))):
                    repository_persname_part_element = ET.SubElement(repository_persname_element, 'part')
                    repository_persname_part_element.text = str(record_object.get('repository_persname')[part])
            else:
                repository_persname_part_element = ET.SubElement(repository_persname_element, 'part')
                repository_persname_part_element.text = record_object.get('repository_persname')
        if record_object.get('repository_famname') is None:
            pass
        else:
            repository_famname_element = ET.SubElement(repository_element, 'famname')
            if type(record_object.get('repository_famname')) is list:
                for part in range(len(record_object.get('repository_famname'))):
                    repository_famname_part_element = ET.SubElement(repository_famname_element, 'part')
                    repository_famname_part_element.text = str(record_object.get('repository_famname')[part])
            else:
                repository_famname_part_element = ET.SubElement(repository_famname_element, 'part')
                repository_famname_part_element.text = record_object.get('repository_famname')
        if record_object.get('repository_corpname') is None:
            pass
        else:
            repository_corpname_element = ET.SubElement(repository_element, 'corpname')
            if type(record_object.get('repository_corpname')) is list:
                for part in range(len(record_object.get('repository_corpname'))):
                    repository_corpname_part_element = ET.SubElement(repository_corpname_element, 'part')
                    repository_corpname_part_element.text = str(record_object.get('repository_corpname')[part])
            else:
                repository_corpname_part_element = ET.SubElement(repository_corpname_element, 'part')
                repository_corpname_part_element.text = record_object.get('repository_corpname')
        if record_object.get('repository_name') is None:
            pass
        else:
            repository_name_element = ET.SubElement(repository_element, 'name')
            if type(record_object.get('repository_name')) is list:
                for part in range(len(record_object.get('repository_name'))):
                    repository_name_part_element = ET.SubElement(repository_name_element, 'part')
                    repository_name_part_element.text = str(record_object.get('repository_name')[part])
            else:
                repository_name_part_element = ET.SubElement(repository_name_element, 'part')
                repository_name_part_element.text = record_object.get('repository_name')

    # Create optional <origination> element
    if type(record_object.get('origination')) is list:
        origination_element = ET.SubElement(did_element, 'origination')
        #origination_element.set('source', record_object.get('origination_attr_source'))
        #origination_element.set('identifier', record_object.get('origination_attr_identifier'))
        for p in range(len(record_object.get('origination'))):
            origination_p_element = ET.SubElement(origination_element, 'p')
            origination_p_element.text = str(record_object.get('origination')[p])
    else:
        if record_object.get('origination') is None:
            pass
        else:
            origination_element = ET.SubElement(did_element, 'origination')
            #origination_element.set('source', record_object.get('origination_attr_source'))
            #origination_element.set('identifier', record_object.get('origination_attr_identifier'))
            origination_p_element = ET.SubElement(origination_element, 'p')
            origination_p_element.text = str(record_object.get('origination'))

    # Create optional <unittitle> element
    if record_object.get('unittitle') is None:
        pass
    else:
        unittitle_element = ET.SubElement(did_element, 'unittitle')
        unittitle_element.text = record_object.get('unittitle')

    # Create optional <unitid> element
    if record_object.get('unitid') is None:
        unitid_element = ET.SubElement(did_element, 'unitid')
        unitid_element.text = input("No unitid is present in the record. \n This value is required by ArchivesSpace. \n Please enter a unitid value to use for this record (even if it's just a placeholder): ")

    else:
        unitid_element = ET.SubElement(did_element, 'unitid')
        unitid_element.text = record_object.get('unitid')

    # Create optional <physloc> element
    if record_object.get('physloc') is None:
        pass
    else:
        physloc_element = ET.SubElement(did_element, 'physloc')
        physloc_element.text = record_object.get('physloc')

    # Create optional <unitdatestructured> element
    if all(value is None for value in [record_object.get('unitdatestructured_fromdate'),
                                        record_object.get('unitdatestructured_todate')]):
        pass
    else:
        unitdatestructured_element = ET.SubElement(did_element, 'unitdatestructured')
        #unitdatestructured_element.set('unitdatetype', record_object.get('unitdatestructured_attr_unitdatetype'))
        unitdatestructured_daterange_element = ET.SubElement(unitdatestructured_element, 'daterange')
        unitdatestructured_fromdate_element = ET.SubElement(unitdatestructured_daterange_element, 'fromdate')
        unitdatestructured_fromdate_element.text = str(record_object.get('unitdatestructured_fromdate'))
        #unitdatestructured_fromdate_element.set('localtype', record_object.get('unitdatestructured_fromdate_attr_localtype'))
        unitdatestructured_todate_element = ET.SubElement(unitdatestructured_daterange_element, 'todate')
        unitdatestructured_todate_element.text = str(record_object.get('unitdatestructured_todate'))
        #unitdatestructured_todate_element.set('localtype', record_object.get('unitdatestructured_todate_attr_localtype'))

    # Create optional <physdescset>	element if data to populate children is present in record_object

    # if type(record_object.get('physdecstructured')) is dict:
    #     physdescset_element = ET.SubElement(did_element, 'physdescset', attrib={})
    #     physdescset_element.set('coverage', record_object.get('physdecset_attr_coverage'))
    #     physdescset_element.set('physdescstructuredtype', record_object.get('physdecset_attr_type'))
    #     for pds in range(len(record_object.get('physdecstructured'))):
    #         physdecstructured_element = ET.SubElement(physdescset_element, 'physdecstructured')
    #         physdecstructured_element.text = str(record_object.get('physdecstructured')[pds])

    if all(value is None for value in [record_object.get('physdescsetstructured_quantity'),
                                       record_object.get('physdescsetstructured_unittype')]):
        pass
    else:
        physdescstructured_element = ET.SubElement(did_element, 'physdescstructured')
        if record_object.get('physdescsetstructured_quantity') is None:
            pass
        else:
            physdescsetstructured_quantity_element = ET.SubElement(physdescstructured_element, 'quantity')
            physdescsetstructured_quantity_element.text = record_object.get('physdescsetstructured_quantity')
        if record_object.get('physdescsetstructured_unittype') is None:
            pass
        else:
            physdescsetstructured_unittype = ET.SubElement(physdescstructured_element, 'unittype')
            physdescsetstructured_unittype.text = record_object.get('physdescsetstructured_unittype')

    # Create <langmaterial> element
    if record_object.get('language') is None:
        pass
    else:
        if type(record_object.get('language')) is list:
            langmaterial_element = ET.SubElement(did_element, 'langmaterial')
            for lang in range(len(record_object.get('language'))):
                languageset_element = ET.SubElement(langmaterial_element, 'langmaterial')
                language_element = ET.SubElement(languageset_element, 'language')
                language_element.text = str(record_object.get('language')[lang])
        else:
            langmaterial_element = ET.SubElement(did_element, 'langmaterial')
            language_element = ET.SubElement(langmaterial_element, 'language')
            language_element.text = record_object.get('language')

    # if record_object.get('langmaterial_descriptivenote') is None:
    #     pass
    # else:
    #     if type(record_object.get('langmaterial_descriptivenote')) is list:
    #         for note in range(len(record_object.get('langmaterial_descriptivenote'))):
    #             langmaterial_descriptivenote_element = ET.SubElement(langmaterial_element, 'descriptivenote')
    #             langmaterial_descriptivenote_element.text = str(record_object.get('langmaterial_descriptivenote')[note])
    #             # Do I need the str()?
    #     else:
    #         langmaterial_descriptivenote_element = ET.SubElement(langmaterial_element, 'descriptivenote')
    #         langmaterial_descriptivenote_element.text = record_object.get('langmaterial_descriptivenote')

    # End of <did> children

    # Create optional element <accessrestrict>
    if record_object.get('accessrestrict') is None:
        pass
    else:
        accessrestrict_element = ET.SubElement(archdesc_element, 'accessrestrict')
        accessrestrict_p_element = ET.SubElement(accessrestrict_element, 'p')
        accessrestrict_p_element.text = record_object.get('accessrestrict')

    # Create optional <accruals> element
    if type(record_object.get('accruals')) is list:
        accruals_element = ET.SubElement(archdesc_element, 'accruals')
        for p in range(len(record_object.get('accruals'))):
            accruals_p_element = ET.SubElement(accruals_element, 'p')
            accruals_p_element.text = str(record_object.get('accruals')[p])
    else:
        if record_object.get('accruals') is None:
            pass
        else:
            accruals_element = ET.SubElement(did_element, 'accruals')
            accruals_p_element = ET.SubElement(accruals_element, 'p')
            accruals_p_element.text = str(record_object.get('accruals'))

    # Create optional <otherfindaid> element
    if type(record_object.get('otherfindaid')) is list:
        otherfindaid_element = ET.SubElement(archdesc_element, 'otherfindaid')
        for p in range(len(record_object.get('otherfindaid'))):
            otherfindaid_p_element = ET.SubElement(otherfindaid_element, 'p')
            otherfindaid_p_element.text = str(record_object.get('otherfindaid')[p])
    else:
        if record_object.get('otherfindaid') is None:
            pass
        else:
            otherfindaid_element = ET.SubElement(did_element, 'otherfindaid')
            otherfindaid_p_element = ET.SubElement(otherfindaid_element, 'p')
            otherfindaid_p_element.text = str(record_object.get('otherfindaid'))

    # Create optional <relatedmaterial> element
    if type(record_object.get('relatedmaterial')) is list:
        relatedmaterial_element = ET.SubElement(archdesc_element, 'relatedmaterial')
        for p in range(len(record_object.get('relatedmaterial'))):
            relatedmaterial_p_element = ET.SubElement(relatedmaterial_element, 'p')
            relatedmaterial_p_element.text = str(record_object.get('relatedmaterial')[p])
    else:
        if record_object.get('relatedmaterial') is None:
            pass
        else:
            relatedmaterial_element = ET.SubElement(did_element, 'relatedmaterial')
            relatedmaterial_p_element = ET.SubElement(relatedmaterial_element, 'p')
            relatedmaterial_p_element.text = str(record_object.get('relatedmaterial'))

    # Create optional <separatedmaterial> element
    if type(record_object.get('separatedmaterial')) is list:
        separatedmaterial_element = ET.SubElement(archdesc_element, 'separatedmaterial')
        for p in range(len(record_object.get('separatedmaterial'))):
            separatedmaterial_p_element = ET.SubElement(separatedmaterial_element, 'p')
            separatedmaterial_p_element.text = str(record_object.get('separatedmaterial')[p])
    else:
        if record_object.get('separatedmaterial') is None:
            pass
        else:
            separatedmaterial_element = ET.SubElement(did_element, 'separatedmaterial')
            separatedmaterial_p_element = ET.SubElement(separatedmaterial_element, 'p')
            separatedmaterial_p_element.text = str(record_object.get('separatedmaterial'))

    # Create optional <otherfindaid> element
    if type(record_object.get('processinfo')) is list:
        processinfo_element = ET.SubElement(archdesc_element, 'processinfo')
        for p in range(len(record_object.get('processinfo'))):
            processinfo_p_element = ET.SubElement(processinfo_element, 'p')
            processinfo_p_element.text = str(record_object.get('processinfo')[p])
    else:
        if record_object.get('processinfo') is None:
            pass
        else:
            processinfo_element = ET.SubElement(did_element, 'processinfo')
            processinfo_p_element = ET.SubElement(processinfo_element, 'p')
            processinfo_p_element.text = str(record_object.get('processinfo'))

    # Create optional <acqinfo> element
    if type(record_object.get('acqinfo')) is list:
        acqinfo_element = ET.SubElement(archdesc_element, 'acqinfo')
        for p in range(len(record_object.get('acqinfo'))):
            acqinfo_p_element = ET.SubElement(acqinfo_element, 'p')
            acqinfo_p_element.text = str(record_object.get('acqinfo')[p])
    else:
        if record_object.get('acqinfo') is None:
            pass
        else:
            acqinfo_element = ET.SubElement(did_element, 'acqinfo')
            acqinfo_p_element = ET.SubElement(acqinfo_element, 'p')
            acqinfo_p_element.text = str(record_object.get('acqinfo'))

    # Create optional element <userestrict>
    if record_object.get('userestrict') is None:
        pass
    else:
        userestrict_element = ET.SubElement(archdesc_element, 'userestrict')
        userestrict_p_element = ET.SubElement(userestrict_element, 'p')
        userestrict_p_element.text = record_object.get('userestrict')

    # Create optional element <scopecontent>
    if record_object.get('scopecontent') is None:
        pass
    else:
        scopecontent_element = ET.SubElement(archdesc_element, 'scopecontent')
        scopecontent_p_element = ET.SubElement(scopecontent_element, 'p')
        scopecontent_p_element.text = record_object.get('scopecontent')

    # Create optional element <bioghist>
    if record_object.get('bioghist') is None:
        pass
    else:
        bioghist_element = ET.SubElement(archdesc_element, 'bioghist')
        bioghist_p_element = ET.SubElement(bioghist_element, 'p')
        bioghist_p_element.text = record_object.get('bioghist')

        # Create optional element <controlaccess>
        if record_object.get('controlaccess') is None:
            pass
        else:
            if type(record_object.get('controlaccess')) is list:
                controlaccess_element = ET.SubElement(archdesc_element, 'controlaccess')
                for subject in range(len(record_object.get('controlaccess'))):
                    controlaccess_subject_element = ET.SubElement(controlaccess_element, 'subject')
                    controlaccess_subject_element.text = str(record_object.get('controlaccess')[subject])
            else:
                controlaccess_element = ET.SubElement(archdesc_element, 'controlaccess')
                subjects = record_object.get('controlaccess')
                for line in subjects.splitlines():
                    controlaccess_subject_element = ET.SubElement(controlaccess_element, 'subject')
                    controlaccess_subject_element.text = line

    tree = ET.ElementTree(root)

    with open('ead_write_test.xml', 'wb') as files:
        tree.write(files, encoding='UTF-8', xml_declaration=True, method='xml', short_empty_elements=True)

def replace_none_with_empty_str(some_dict):
    return { k: ('This was a None' if v is None else v) for k, v in some_dict.items() }

if __name__ == '__main__':
    record_object = {  # First, elements
                         'recordid': 'recordid',
                        # <titlestmt> children
                         'titlestmt_titleproper': 'titlestmt_titleproper',
                         'titlestmt_subtitle': 'titlestmt_subtitle',
                         'titlestmt_author': 'titlestmt_author',
                         'titlestmt_sponsor': 'titlestmt_sponsor',
                         'titleproper': 'titleproper',
                        # <publicationstmt> children
                         'publicationstmt_publisher': 'publicationstmt_publisher',
                         'publicationstmt_date': 'publicationstmt_date',
                         'publicationstmt_addressline': 'publicationstmt_addressline',
                         'publicationstmt_p': 'publicationstmt_p',
                         'publicationstmt_num': 'publicationstmt_num',
                         'repository': 'repository-test', # may not be necessary if <repository> is always entry
                         # 'repository_persname': ['repository_persname'],
                         'repository_persname': 'repository_persname', # test non-list entry
                         # 'repository_famname': ['repository_famname'],
                         'repository_famname': 'repository_famname', # test non-list entry
                         # 'repository_corpname': ['repository_corpname'],
                         'repository_corpname': 'repository_corpname', # test non-list entry
                        # target XML:
                        # <corpname source="NAF" identifier="http://id.loc.gov/authorities/names/n91102518">
                        # 					<part>Rush University Medical Center Archives/part>
                        # 				</corpname>
                        # 				<address>
                        # 					<addressline>Chicago, Ill.</addressline>
                        # 				</address>
                         'repository_name': 'repository_name',
                        # 'repository_name': ['repository_name'], # test non-list entry
                        # Do I need to add <repository><address>?
                        'maintenancehistory_eventdatetime': 'maintenancehistory_eventdatetime',
                        'maintenancehistory_agent': 'maintenancehistory_agent',
                        'maintenancehistory_eventdescription': 'maintenancehistory_eventdescription',
                        'maintenanceagency_agencycode': 'maintenanceagency_agencycode',
                        'maintenanceagency_otheragencycode': 'maintenanceagency_otheragencycode',
                        'maintenanceagency_agencyname': 'maintenanceagency_agencyname',
                        'maintenanceagency_descriptivenote': 'maintenanceagency_descriptivenote',
                        'unittitle': 'unittitle',
                        'unitid': 'unitid',
                        'unitdatestructured_fromdate': 'unitdatestructured_fromdate',
                        'unitdatestructured_todate': 'unitdatestructured_todate',
                        'physdescsetstructuredtype_unittype': 'physdescsetstructuredtype_unittype',
                        'physdescsetstructuredtype_quantity': 'physdescsetstructuredtype_quantity',
                        # 'langmaterial_descriptivenote': ['In English with some Spanish', 'The majority of the documents are written in Modern English. Roberts copies multiple passages from original manuscripts in Latin and Old English.'],
                        'langmaterial_descriptivenote': 'langmaterial_descriptivenote',
                        # 'language': ['en', 'es', 'it'],
                        'language': 'language',

                        # Next, attributes
                        # <recordid> attributes
                        'recordid_attr_instanceurl': 'recordid_attr_instanceurl',
                        'recordid_attr_altrender': 'recordid_attr_altrender',
                        'recordid_attr_audience': 'external',  # (values limited to: external, internal)
                        'recordid_attr_encodinganalog': 'recordid_attr_encodinganalog',
                        'recordid_attr_id': 'recordid_attr_id',
                        'recordid_attr_lang': 'recordid_attr_lang',
                        'recordid_attr_localtype': 'recordid_attr_localtype',
                        'recordid_attr_script': 'recordid_attr_script',
                        # attributes in <control>
                        # <maintenancestatus>
                        'maintenancestatus_attr_value': 'derived',
                        '#maintenancehistory_eventtype_attr_value': 'created',
                        'maintenancehistory_eventdatetime_attr_standarddatetime': 'maintenancehistory_eventdatetime_attr_standarddatetime',
                        'maintenancehistory_agenttype_attr_value': 'machine',
                        # <archdesc> attrubutes
                        'archdesc_attr_localtype': 'archdesc_attr_localtype',
                        'archdesc_attr_level': 'archdesc_attr_level',
                        # <repository> attributes
                        'repository_corpname_attr_source': 'repository_corpname_attr_source',
                        'repository_corpname_attr_identifier': 'repository_corpname_attr_identifier',
                        # <origination> attributes
                        'origination_attr_source': 'origination_attr_source',
                        'origination_attr_identifier': 'origination_attr_identifier',
                        # <unitdatestructured> attributes
                        'unitdatestructured_attr_unitdatetype': 'unitdatestructured_attr_unitdatetype',
                        'unitdatestructured_fromdate_attr_standarddate': 'unitdatestructured_fromdate_attr_standarddate',
                        'unitdatestructured_todate_attr_standarddate': 'unitdatestructured_todate_attr_standarddate',
                        # <scopecontent> attributes
                        'scopecontent_attr_altrender': 'scopecontent_attr_altrender',
                        'scopecontent_attr_audience': 'scopecontent_attr_audience', #(values limited to: external, internal)
                        'scopecontent_attr_encodinganalog': 'scopecontent_attr_encodinganalog',
                        'scopecontent_attr_id': 'scopecontent_attr_id',
                        'scopecontent_attr_lang': 'scopecontent_attr_lang',
                        'scopecontent_attr_localtype': 'scopecontent_attr_localtype',
                        'scopecontent_attr_script': 'scopecontent_attr_script',
                        # <userestrict> attributes
                        'userestrict_attr_altrender': 'userestrict_attr_altrender',
                        'userestrict_attr_audience': 'userestrict_attr_audience',
                        'userestrict_attr_encodinganalog': 'userestrict_attr_encodinganalog',
                        'userestrict_attr_id': 'userestrict_attr_id',
                        'userestrict_attr_lang': 'userestrict_attr_lang',
                        'userestrict_attr_localtype': 'userestrict_attr_localtype',
                        'userestrict_attr_script': 'userestrict_attr_script',
                        # <accessrestrict> attributes
                        'accessrestrict_attr_altrender': 'accessrestrict_attr_altrender',
                        'accessrestrict_attr_audience': 'accessrestrict_attr_audience',  # (values limited to: external, internal)
                        'accessrestrict_attr_encodinganalog': 'accessrestrict_attr_encodinganalog',
                        'accessrestrict_attr_id': 'accessrestrict_attr_id',
                        'accessrestrict_attr_lang': 'accessrestrict_attr_lang',
                        'accessrestrict_attr_localtype': 'accessrestrict_attr_localtype',
                        'accessrestrict_attr_script': 'accessrestrict_attr_script',
                    }

    generate_ead(record_object)